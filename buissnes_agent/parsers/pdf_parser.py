import base64
import io
import logging
import os
import sys
import time
from typing import Dict, List, Optional, Tuple, Union

from dotenv import load_dotenv
from langchain_core.documents import Document

from .base_parser import BaseDocumentParser

load_dotenv()

LLM_BASE_URL = os.getenv("LLM_BASE_URL")
LLM_MODEL = os.getenv("LLM_MODEL")
LLM_API_KEY = os.getenv("LLM_API_KEY")

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(message)s", stream=sys.stdout)

# ── Zależności ───────────────────────────────────────────────
try:
    import fitz  # PyMuPDF

    FITZ_AVAILABLE = True
except ImportError:
    FITZ_AVAILABLE = False
    logger.error("PyMuPDF (fitz) jest WYMAGANY dla tego parsera do konwersji PDF na obrazy!")

try:
    from openai import OpenAI

    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False
    logger.error("Biblioteka 'openai' jest wymagana do komunikacji z LM Studio.")


class PdfParser(BaseDocumentParser):
    """
    Parser PDF korzystający z lokalnego modelu wizyjnego w LM Studio.
    Wyposażony w zabezpieczenia przed pętleniem (stop tokens) oraz wizualny licznik postępu.
    """

    def __init__(
            self,
            temperature: float = 0.0,
            dpi_scale: float = 1.2,
            top_margin_crop: float = 50.0,
            bottom_margin_crop: float = 60.0,
            left_margin_crop: float = 0.0,
            right_margin_crop: float = 0.0,
    ):
        if not FITZ_AVAILABLE or not OPENAI_AVAILABLE:
            raise ImportError("Zainstaluj wymagania: pip install pymupdf openai")

        self.temperature = temperature
        self.dpi_scale = dpi_scale

        # Timeout na 10 minut, żeby połączenie nie zerwało się przy trudnych stronach
        self.client = OpenAI(
            base_url=LLM_BASE_URL,
            api_key=LLM_API_KEY,
            timeout=600.0
        )

        # ── Marginesy ────────────────────────────────────────────
        self._top_margin = top_margin_crop
        self._bottom_margin = bottom_margin_crop
        self._left_margin = left_margin_crop
        self._right_margin = right_margin_crop
        self._margins_enabled = any(
            [top_margin_crop, bottom_margin_crop, left_margin_crop, right_margin_crop]
        )

        logger.info(f"LM Studio Parser zainicjalizowany (URL: {LLM_BASE_URL}, Model: {LLM_MODEL}).")

        self.system_prompt = (
            "You are an expert document OCR and layout parsing assistant. "
            "Extract the text, tables, and formatting from the provided document image "
            "and output it EXACTLY as clean Markdown. "
            "Rules:\n"
            "- Preserve heading levels (#, ##, etc.)\n"
            "- Convert tables to Markdown tables.\n"
            "- Do not add ANY conversational filler (e.g., 'Here is the markdown:').\n"
            "- Stop generating immediately when you reach the end of the page content."
        )

    # ══════════════════════════════════════════════════════════════
    # INTERFEJS PUBLICZNY
    # ══════════════════════════════════════════════════════════════

    def parse(
            self,
            file_source: Union[str, io.BytesIO, bytes],
            **kwargs,
    ) -> List[Document]:

        source_name = self._get_source_name(file_source)
        documents = []

        try:
            pdf_doc, original_page_dims = self._load_and_precrop_pdf(file_source)
            total_pages = len(pdf_doc)

            # --- WYRAŹNY LOG STARTOWY ---
            logger.info("=" * 60)
            logger.info(f"ROZPOCZĘTO PRZETWARZANIE: {source_name}")
            logger.info(f"Liczba stron do przetworzenia: {total_pages}")
            logger.info("=" * 60)

            for page_idx in range(total_pages):
                page_no = page_idx + 1
                page = pdf_doc[page_idx]

                logger.info(f"\n[STRONA {page_no}/{total_pages}] Przygotowywanie obrazu...")
                start_time = time.time()

                # Konwersja strony PDF do Base64 JPEG
                base64_image = self._pdf_page_to_base64(page)
                payload_mb = len(base64_image) / (1024 * 1024)

                logger.info(
                    f"[STRONA {page_no}/{total_pages}] Wysyłanie do LM Studio (Rozmiar: {payload_mb:.2f} MB)...")

                # Zapytanie do LLM (Vision API)
                md_text = self._call_vision_llm(base64_image)

                elapsed_time = time.time() - start_time

                if md_text:
                    logger.info(
                        f"[STRONA {page_no}/{total_pages}] Zakończono sukcesem! (Czas: {elapsed_time:.1f} sek.)")

                    metadata = {
                        "page_number": page_no,
                        "total_pages": total_pages,
                        "source": source_name,
                        "parser": "lm_studio_vision",
                        "margin_top_pt": self._top_margin,
                        "margin_bottom_pt": self._bottom_margin,
                    }
                    if original_page_dims and page_no in original_page_dims:
                        metadata["original_page_width_pt"] = original_page_dims[page_no][0]
                        metadata["original_page_height_pt"] = original_page_dims[page_no][1]

                    documents.append(
                        Document(page_content=md_text.strip(), metadata=metadata)
                    )
                else:
                    logger.error(
                        f"[STRONA {page_no}/{total_pages}] Błąd! Zwrócono pusty tekst. (Czas: {elapsed_time:.1f} sek.)")

            pdf_doc.close()

            logger.info("=" * 60)
            logger.info(f"ZAKOŃCZONO PRZETWARZANIE: {source_name} (Sukces: {len(documents)}/{total_pages} stron)")
            logger.info("=" * 60)

            return documents

        except Exception as e:
            logger.error(f"Błąd parsera LM Studio ({source_name}): {e}", exc_info=True)
            return documents

    def diagnostics(self) -> Dict[str, str]:
        return {
            "engine": "LM Studio Vision",
            "model_name_requested": LLM_MODEL,
            "base_url": str(self.client.base_url),
            "dpi_scale": str(self.dpi_scale),
            "margins_enabled": str(self._margins_enabled),
        }

    # ══════════════════════════════════════════════════════════════
    # WARSTWA 1: Wczytywanie i PRE-CROP (PyMuPDF cropbox)
    # ══════════════════════════════════════════════════════════════

    def _load_and_precrop_pdf(
            self, file_source: Union[str, io.BytesIO, bytes]
    ) -> Tuple['fitz.Document', Dict[int, Tuple[float, float]]]:

        if isinstance(file_source, str):
            pdf_doc = fitz.Document(file_source)
        elif isinstance(file_source, bytes):
            pdf_doc = fitz.Document(stream=file_source, filetype="pdf")
        elif isinstance(file_source, io.BytesIO):
            file_source.seek(0)
            pdf_doc = fitz.Document(stream=file_source.read(), filetype="pdf")
        else:
            raise ValueError(f"Nieobsługiwany typ: {type(file_source)}")

        original_dims: Dict[int, Tuple[float, float]] = {}

        for page_idx, page in enumerate(pdf_doc):
            rect = page.rect
            original_dims[page_idx + 1] = (rect.width, rect.height)

            if self._margins_enabled:
                new_x0 = rect.x0 + self._left_margin
                new_y0 = rect.y0 + self._top_margin
                new_x1 = rect.x1 - self._right_margin
                new_y1 = rect.y1 - self._bottom_margin

                if (new_x1 - new_x0) > 100 and (new_y1 - new_y0) > 100:
                    new_rect = fitz.Rect(new_x0, new_y0, new_x1, new_y1)
                    page.set_cropbox(new_rect)

        return pdf_doc, original_dims

    def _pdf_page_to_base64(self, page: 'fitz.Page') -> str:
        mat = fitz.Matrix(self.dpi_scale, self.dpi_scale)
        pix = page.get_pixmap(matrix=mat, alpha=False)
        img_data = pix.tobytes("jpeg")
        return base64.b64encode(img_data).decode("utf-8")

    # ══════════════════════════════════════════════════════════════
    # WYWOŁANIE LLM (Vision API)
    # ══════════════════════════════════════════════════════════════

    def _call_vision_llm(self, base64_image: str) -> Optional[str]:
        try:
            response = self.client.chat.completions.create(
                model=LLM_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": self.system_prompt
                    },
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": "Extract all text and layout from this document page into Markdown."
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{base64_image}"
                                },
                            },
                        ],
                    }
                ],
                temperature=self.temperature,
                max_tokens=4000,
                # ZABEZPIECZENIA PRZED NIESKOŃCZONĄ PĘTLĄ HALUCYNACJI:
                top_p=0.1,  # Zmniejsza losowość do minimum
                stop=["<|im_end|>", "<|endoftext|>", "</s>", "```\n\nUser:"]  # Wymusza koniec tekstu
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"Błąd połączenia z serwerem wizyjnym (LM Studio): {e}")
            return None

    @staticmethod
    def _get_source_name(file_source: Union[str, io.BytesIO, bytes]) -> str:
        if isinstance(file_source, str):
            return os.path.basename(file_source)
        return "strumień_pamięci"