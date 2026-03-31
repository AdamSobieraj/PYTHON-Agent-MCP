import io
import logging
import os
from typing import List, Union

import fitz  # PyMuPDF
import pymupdf4llm
from langchain_core.documents import Document
from base_parser import BaseDocumentParser

logger = logging.getLogger(__name__)


class PdfParser(BaseDocumentParser):
    """
    Parser dla plików PDF oparty na PyMuPDF4LLM.
    Rozpoznaje układ strony (layout), ekstrahuje tabele, listy i nagłówki,
    a następnie konwertuje wszystko na piękny Markdown.
    """

    def parse(self, file_source: Union[str, io.BytesIO, bytes], **kwargs) -> List[Document]:
        documents = []
        source_name = os.path.basename(file_source) if isinstance(file_source, str) else "strumień pamięci S3"

        # Konfiguracja marginesów do obcięcia (w punktach typograficznych)
        # Standardowa strona A4 ma wysokość ok. 842 punktów.
        # Zwykle 50-70 punktów wystarcza na usunięcie stopki.
        BOTTOM_MARGIN_TO_CROP = 60

        # Jeśli jest też powtarzający się nagłówek na górze, możesz odciąć górę:
        TOP_MARGIN_TO_CROP = 50

        try:
            # 1. Wczytanie pliku PDF z obsługą pamięci RAM i dysku lokalnego
            if isinstance(file_source, str):
                # Z dysku (Local Loader)
                pdf_doc = fitz.Document(file_source)
            elif isinstance(file_source, bytes):
                # Surowe bajty (S3 Loader)
                pdf_doc = fitz.Document(stream=file_source, filetype="pdf")
            elif isinstance(file_source, io.BytesIO):
                # Strumień pamięci (S3 Loader)
                pdf_doc = fitz.Document(stream=file_source.read(), filetype="pdf")
            else:
                raise ValueError("Nieobsługiwany typ źródła dla PDF")

            # 1.5 Usuwanie stopek (przycinanie Cropbox'a przed analizą LLM)
            for page in pdf_doc:
                rect = page.rect  # Pobierz obecne wymiary strony (x0, y0, x1, y1)

                # Definiujemy nowy prostokąt odcinając dół (zmniejszamy y1)
                # Opcjonalnie odcinając górę (zwiększamy y0)
                new_rect = fitz.Rect(
                    rect.x0,
                    rect.y0 + TOP_MARGIN_TO_CROP,  # Zmień na: rect.y0 + TOP_MARGIN_TO_CROP jeśli chcesz uciąć też nagłówek
                    rect.x1,
                    rect.y1 - BOTTOM_MARGIN_TO_CROP
                )

                # Ustawiamy nowy obszar roboczy strony.
                # pymupdf4llm weźmie pod uwagę TYLKO tekst wewnątrz tego prostokąta.
                page.set_cropbox(new_rect)

            # 2. Magia konwersji: generujemy Markdown z podziałem na strony
            # page_chunks=True zwraca listę słowników, gdzie każdy słownik to jedna strona
            md_pages = pymupdf4llm.to_markdown(doc=pdf_doc, page_chunks=True)

            # 3. Konwersja do formatu LangChain Document
            for i, page_data in enumerate(md_pages):
                # page_data["text"] zawiera gotowy kod Markdown dla danej strony
                md_text = page_data.get("text", "").strip()

                if md_text:
                    doc = Document(
                        page_content=md_text,
                        metadata={"page_number": i + 1}
                    )
                    documents.append(doc)

            # 4. Zwolnienie pamięci (bardzo ważne przy dużych PDF-ach!)
            pdf_doc.close()

            return documents

        except Exception as e:
            logger.error(f"Błąd przetwarzania PDF na Markdown ({source_name}): {e}")
            return []


'''
UWAGA

Wartość 60 użyta w kodzie to punkty (1 punkt = 1/72 cala). Standardowa strona A4 ma wysokość 842 punkty.
Wartość pomiędzy 50 a 80 zazwyczaj idealnie "zjada" numerację stron i stopkę, nie ucinając jednocześnie właściwego 
tekstu dokumentu. Jeśli stopka jest wyjątkowo wysoka, można po prostu zwiększyć tę liczbę (np. do 100).

Aby przekształcić pliki PDF na prawdziwy format Markdown (z zachowaniem nagłówków, pogrubień, list, 
a przede wszystkim tabel), musimy porzucić bibliotekę pypdf. Narzędzie to potrafi jedynie "wypluć" 
ciąg czystego tekstu i nie rozumie układu strony (layoutu).

Obecnie najlepszym i najszybszym standardem branżowym do konwersji PDF na Markdown pod systemy RAG 
jest biblioteka pymupdf4llm (stworzona przez twórców PyMuPDF).

Co najważniejsze – biblioteka ta posiada wbudowaną funkcję page_chunks=True, która idealnie dzieli PDF na strony, 
co perfekcyjnie pasuje do naszej logiki LangChain (1 strona = 1 obiekt Document). 

Obsługuje też odczyt plików prosto z pamięci RAM (dla S3).

PyMuPDF (fitz) jest napisany w C++. Jest to jeden z najszybszych silników do manipulacji plikami PDF w świecie Pythona.
Pobranie i sparsowanie pliku z AWS S3 w locie będzie działać błyskawicznie.

Nagłówki: Duże, pogrubione teksty zostaną zamienione na tagi ## i ###, dzięki czemu podczas chunkowania 
(np. używając MarkdownHeaderTextSplitter z LangChain) będzie można precyzyjnie dzielić PDF po logicznych 
sekcjach (rozdziałach), a nie w losowych miejscach w połowie zdania.
'''