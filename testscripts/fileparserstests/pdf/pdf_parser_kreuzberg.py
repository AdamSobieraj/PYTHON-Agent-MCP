import io
import logging
import os
import asyncio
import concurrent.futures
from typing import List, Union

import fitz  # PyMuPDF – używany WYŁĄCZNIE do przycięcia marginesów
from langchain_core.documents import Document
from kreuzberg import extract_file, extract_bytes

from base_parser import BaseDocumentParser

logger = logging.getLogger(__name__)


class PdfParser(BaseDocumentParser):
    """
    Parser dla plików PDF oparty na bibliotece Kreuzberg.
    Ekstrahuje tekst z pliku PDF i konwertuje go na format Markdown.
    Automatycznie wykrywa zeskanowane strony i uruchamia OCR (Tesseract).

    Przed ekstrakcją przycina marginesy górny i dolny (CropBox via PyMuPDF),
    aby usunąć powtarzające się nagłówki i stopki (np. numery stron).
    """

    # Marginesy do obcięcia (w punktach typograficznych, 1 pt = 1/72 cala)
    # Standardowa strona A4 ma wysokość ok. 842 punktów.
    TOP_MARGIN_TO_CROP = 50
    BOTTOM_MARGIN_TO_CROP = 60

    def parse(self, file_source: Union[str, io.BytesIO, bytes], **kwargs) -> List[Document]:
        documents: List[Document] = []
        source_name = (
            os.path.basename(file_source)
            if isinstance(file_source, str)
            else "strumień pamięci S3"
        )

        try:
            # 1. Wczytanie pliku PDF do PyMuPDF (tylko do przycięcia marginesów)
            pdf_doc = self._open_pdf(file_source)

            # 2. Przycięcie marginesów górnego i dolnego na każdej stronie
            self._crop_margins(pdf_doc)

            # 3. Zapis przyciętego PDF do bajtów w pamięci RAM
            cropped_pdf_bytes = pdf_doc.tobytes()
            pdf_doc.close()

            # 4. Ekstrakcja treści PDF → Markdown za pomocą Kreuzberg
            result = self._run_extraction(cropped_pdf_bytes, **kwargs)

            md_text = result.content.strip()
            if not md_text:
                logger.warning(
                    "Plik PDF jest pusty lub nie udało się wyekstrahować tekstu (%s)",
                    source_name,
                )
                return documents

            # 5. Podział na strony (Kreuzberg wstawia \f między stronami)
            pages = self._split_into_pages(md_text)

            # 6. Konwersja do formatu LangChain Document
            for i, page_text in enumerate(pages):
                page_text = page_text.strip()
                if page_text:
                    documents.append(
                        Document(
                            page_content=page_text,
                            metadata={"page_number": i + 1},
                        )
                    )

            logger.info(
                "Wyekstrahowano %d stron z PDF (%s)",
                len(documents),
                source_name,
            )
            return documents

        except Exception as e:
            logger.error(
                "Błąd przetwarzania PDF na Markdown (%s): %s",
                source_name,
                e,
            )
            return []

    # ------------------------------------------------------------------
    # Wczytanie PDF (obsługa str, bytes, BytesIO)
    # ------------------------------------------------------------------

    @staticmethod
    def _open_pdf(file_source: Union[str, io.BytesIO, bytes]) -> fitz.Document:
        """Otwiera plik PDF z dysku lub pamięci RAM."""
        if isinstance(file_source, str):
            return fitz.Document(file_source)
        if isinstance(file_source, bytes):
            return fitz.Document(stream=file_source, filetype="pdf")
        if isinstance(file_source, io.BytesIO):
            return fitz.Document(stream=file_source.read(), filetype="pdf")
        raise ValueError("Nieobsługiwany typ źródła dla PDF")

    # ------------------------------------------------------------------
    # Przycinanie marginesów (usuwanie nagłówków / stopek)
    # ------------------------------------------------------------------

    def _crop_margins(self, pdf_doc: fitz.Document) -> None:
        """
        Przycina CropBox każdej strony, aby usunąć powtarzające się
        nagłówki (góra) i stopki / numery stron (dół).

        Kreuzberg (i każdy inny silnik) weźmie pod uwagę WYŁĄCZNIE
        tekst wewnątrz przyciętego prostokąta.
        """
        for page in pdf_doc:
            rect = page.rect
            new_rect = fitz.Rect(
                rect.x0,
                rect.y0 + self.TOP_MARGIN_TO_CROP,
                rect.x1,
                rect.y1 - self.BOTTOM_MARGIN_TO_CROP,
            )
            page.set_cropbox(new_rect)

    # ------------------------------------------------------------------
    # Obsługa async → sync (Kreuzberg ma API asynchroniczne)
    # ------------------------------------------------------------------

    def _run_extraction(self, pdf_bytes: bytes, **kwargs):
        """
        Uruchamia asynchroniczną ekstrakcję Kreuzberg w kontekście synchronicznym.
        Jeśli pętla zdarzeń asyncio jest już aktywna (np. Jupyter, FastAPI),
        ekstrakcja zostanie uruchomiona w osobnym wątku.
        """
        coro = self._async_extract(pdf_bytes, **kwargs)

        try:
            asyncio.get_running_loop()
            with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
                return pool.submit(asyncio.run, coro).result()
        except RuntimeError:
            return asyncio.run(coro)

    @staticmethod
    async def _async_extract(pdf_bytes: bytes, **kwargs):
        """
        Asynchroniczna ekstrakcja treści z przyciętego PDF (bajty).
        Opcjonalne kwargs: force_ocr (bool), language (str, np. 'pol').
        """
        extra = {}
        if kwargs.get("force_ocr"):
            extra["force_ocr"] = True
        if kwargs.get("language"):
            extra["language"] = kwargs["language"]

        return await extract_bytes(
            pdf_bytes, mime_type="application/pdf", **extra
        )

    # ------------------------------------------------------------------
    # Podział na strony
    # ------------------------------------------------------------------

    @staticmethod
    def _split_into_pages(md_text: str) -> List[str]:
        """
        Kreuzberg wstawia znak form-feed (\\f) jako separator stron.
        Jeśli separatory nie zostaną wykryte, cały dokument
        jest zwracany jako jedna „strona".
        """
        if "\f" in md_text:
            return md_text.split("\f")
        return [md_text]