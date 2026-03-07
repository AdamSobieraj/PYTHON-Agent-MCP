import json
import logging
import os
import sys
from typing import Generator, Tuple, Dict, Any

import docx
import openpyxl
import pypdf

from buissnes_agent.MetadataModels import FileMetadata
from buissnes_agent.config_loader import settings

logging.basicConfig(level=logging.INFO, stream=sys.stderr)
logger = logging.getLogger(__name__)

class DataLoaderLocalFileLoader:
    """
    Adapter dla plików lokalnych.
    Obsługuje: TXT, MD, XML, JSON, PDF, DOCX, XLSX.
    """

    def __init__(self, directory: str):
        self.directory = os.path.abspath(directory)

    def list_objects(self) -> Generator[str, None, None]:

        allowed_exts = settings.get("chunking.allowed_extensions", [])
        ext_tuple = tuple(allowed_exts)

        if not os.path.exists(self.directory):
            logger.error(f"Katalog nie istnieje: {self.directory}")
            return

        for root, _, files in os.walk(self.directory):
            for file in files:
                ext = os.path.splitext(file)[1].lower()
                if ext in ext_tuple:
                    yield os.path.join(root, file)

    def load_file_with_metadata(self, file_path: str) -> Tuple[str, Dict[str, Any]]:
        filename = os.path.basename(file_path)
        ext = os.path.splitext(file_path)[1].lower()

        domain_value = self._extract_domain_first(file_path)

        # 1. Tworzenie obiektu metadanych (Type Safe)
        meta_obj = FileMetadata(
            source=f"file://{file_path}",
            title=filename,
            extension=ext,
            url=f"file://{file_path}",
            domain=domain_value,
            tags=["local", "filesystem"],
            page_number=None  # Cały plik, więc brak konkretnej strony
        )

        content = ""

        try:
            # --- XLSX (Excel) ---
            if ext == ".xlsx":
                content = self._process_xlsx(file_path)
            # --- PDF ---
            elif ext == ".pdf":
                content = self._process_pdf(file_path)
            # --- DOCX ---
            elif ext == ".docx":
                content = self._process_docx(file_path)
            # --- TEKSTOWE ---
            else:
                content = self._process_text(file_path)

            return content, meta_obj.to_dict()

        except Exception as e:
            logger.error(f"Krytyczny błąd przy pliku {file_path}: {e}")
            return "", {}

    def _process_xlsx(self, file_path: str) -> str:
        """
        Prywatna metoda do konwersji pliku XLSX na JSON String.
        Zachowuje strukturę arkuszy i wierszy.
        """
        try:
            # data_only=True pobiera wyliczone wartości, a nie formuły
            wb = openpyxl.load_workbook(file_path, data_only=True)
            excel_data = {}

            for sheet in wb.worksheets:
                sheet_data = []

                # Iteracja po wierszach (values_only=True zwraca krotki wartości)
                for row in sheet.iter_rows(values_only=True):
                    # Sprawdzenie, czy wiersz nie jest pusty (zawiera przynajmniej jedną wartość niebędącą None)
                    if any(cell is not None for cell in row):
                        # Konwersja każdej komórki na string (ważne dla dat i liczb)
                        # None zamieniamy na null (w JSON) lub pomijamy
                        clean_row = [str(cell) if cell is not None else None for cell in row]
                        sheet_data.append(clean_row)

                # Dodajemy arkusz do słownika tylko jeśli ma dane
                if sheet_data:
                    excel_data[sheet.title] = sheet_data

            if not excel_data:
                logger.warning(f"Plik XLSX {os.path.basename(file_path)} jest pusty lub nie zawiera danych.")
                return ""

            # Serializacja do JSON String
            # ensure_ascii=False pozwala zachować polskie znaki
            # indent=2 poprawia czytelność (opcjonalne, zwiększa rozmiar stringa)
            return json.dumps(excel_data, ensure_ascii=False)

        except Exception as e:
            logger.error(f"Błąd przetwarzania XLSX {os.path.basename(file_path)}: {e}")
            return ""

    def _process_pdf(self, file_path: str) -> str:
        """
        Prywatna metoda do ekstrakcji tekstu z pliku PDF.
        """
        try:
            reader = pypdf.PdfReader(file_path)
            text_pages = []

            for i, page in enumerate(reader.pages):
                extracted = page.extract_text()
                if extracted:
                    # Opcjonalnie: Można dodać numer strony do tekstu, co pomaga w RAG
                    # text_pages.append(f"--- Page {i+1} ---")
                    text_pages.append(extracted)

            return "\n".join(text_pages)

        except Exception as e:
            logger.error(f"Błąd przetwarzania PDF {os.path.basename(file_path)}: {e}")
            return ""

    def _process_docx(self, file_path: str) -> str:
        """
        Ekstrakcja tekstu z pliku DOCX.
        """
        try:
            doc = docx.Document(file_path)
            # Pobieramy tekst z paragrafów
            full_text = [para.text for para in doc.paragraphs if para.text.strip()]
            return "\n".join(full_text)
        except Exception as e:
            logger.error(f"Błąd parsowania DOCX {os.path.basename(file_path)}: {e}")
            return ""

    def _process_text(self, file_path: str) -> str:
        """
        Odczyt plików tekstowych (TXT, MD, XML, JSON, XSD itp.).
        """
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                return f.read()
        except Exception as e:
            logger.error(f"Błąd odczytu tekstu {os.path.basename(file_path)}: {e}")
            return ""

    def _extract_domain_first(self, file_path: str) -> str:
        """
        Pobiera nazwę domeny na podstawie ścieżki pliku.
        Domena to pierwszy katalog względem głównego folderu przeszukiwania (self.directory).
        Np. dla pliku "C:/dane/HR/umowy/2023/umowa.pdf" (gdy self.directory="C:/dane")
        zwróci "HR".
        """
        # Wyliczamy ścieżkę względną pliku w stosunku do przeszukiwanego katalogu
        rel_path = os.path.relpath(file_path, self.directory)

        # Ujednolicamy ukośniki, aby split zachowywał się tak samo na Windowsie i Linuksie
        normalized_rel_path = rel_path.replace('\\', '/')
        parts = normalized_rel_path.split('/')

        if len(parts) > 1:
            # Plik leży w jakimś podfolderze. Bierzemy folder NAJWYŻSZEGO poziomu.
            return parts[0]
        else:
            # Plik leży bezpośrednio w głównym katalogu przeszukiwania.
            # Fallback na nazwę tego głównego katalogu lub "local"
            return os.path.basename(self.directory) or "local"
