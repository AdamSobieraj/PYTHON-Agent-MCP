import io
import json
import logging
import os
import sys
from typing import Dict, Any, Generator, Tuple

import docx
import openpyxl
import pypdf

from DataLoaderS3Service import DataLoaderS3Service
from buissnes_agent.MetadataModels import FileMetadata

logging.basicConfig(level=logging.INFO, stream=sys.stderr)
logger = logging.getLogger(__name__)

class DataLoaderS3FileLoader:
    def __init__(self, bucket_name: str, prefix: str):
        self.bucket_name = bucket_name

        # 1. Usuwamy białe znaki
        clean_prefix = prefix.strip() if prefix else ""

        # 2. Jeśli prefix jest podany, upewniamy się, że kończy się slashem "/"
        if clean_prefix:
            if not clean_prefix.endswith('/'):
                self.prefix = f"{clean_prefix}/"
            else:
                self.prefix = clean_prefix
            logger.info(f"S3FileLoader: Ustawiono filtr na folder: '{self.prefix}'")
        else:
            # 3. Jeśli prefix jest pusty -> OSTRZEŻENIE
            self.prefix = ""
            logger.warning("!!! UWAGA: Nie podano folderu (prefix). Skrypt pobierze CAŁY BUCKET !!!")

        self.s3_service = DataLoaderS3Service()

    def list_objects(self) -> Generator[str, None, None]:
        # Przekazujemy prefix do serwisu S3. AWS zwróci tylko obiekty zaczynające się od tego ciągu.
        return self.s3_service.list_objects(self.bucket_name, self.prefix)

    def load_file_with_metadata(self, s3_key: str) -> Tuple[str, Dict[str, Any]]:
        filename = os.path.basename(s3_key)
        ext = os.path.splitext(s3_key)[1].lower()

        domain_value = self._extract_domain_first(s3_key)

        # Tworzenie metadanych
        meta_obj = FileMetadata(
            source=f"s3://{self.bucket_name}/{s3_key}",
            title=filename,
            extension=ext,
            url=f"https://{self.bucket_name}.s3.amazonaws.com/{s3_key}",
            domain=domain_value,  # <--- Podstawienie dynamicznej domeny

            # Dodajemy domenę do tagów (z małych liter) dla lepszego filtrowania w bazie wektorowej
            tags=["s3_storage", "cloud", domain_value.lower()],

            page_number=None  # Cały plik, więc brak konkretnej strony
        )
        content = ""

        try:
            # --- ROUTING PO TYPIE PLIKU ---
            if ext == '.xlsx':
                content = self._process_xlsx(s3_key)

            elif ext == '.pdf':
                content = self._process_pdf(s3_key)

            elif ext == '.docx':
                content = self._process_docx(s3_key)

            else:
                # Domyślna obsługa plików tekstowych (txt, md, xml, xsd, json)
                content = self._process_text(s3_key)

            return content, meta_obj.to_dict()

        except Exception as e:
            logger.error(f"Krytyczny błąd przy pliku {s3_key}: {e}")
            return "", {}

    def _process_xlsx(self, s3_key: str) -> str:
        """
        Pobiera plik XLSX z S3 i konwertuje go na JSON String.
        """
        try:
            # Pobieramy bajty z S3
            file_bytes = self.s3_service.download_bytes(self.bucket_name, s3_key)

            # Otwieramy bajty jako plik w pamięci
            with io.BytesIO(file_bytes) as f:
                wb = openpyxl.load_workbook(f, data_only=True)
                excel_data = {}

                for sheet in wb.worksheets:
                    sheet_data = []
                    for row in sheet.iter_rows(values_only=True):
                        # Sprawdzenie czy wiersz nie jest pusty
                        if any(cell is not None for cell in row):
                            # Konwersja na string dla bezpieczeństwa (np. daty)
                            clean_row = [str(cell) if cell is not None else None for cell in row]
                            sheet_data.append(clean_row)

                    if sheet_data:
                        excel_data[sheet.title] = sheet_data

                if not excel_data:
                    return ""

                # Serializacja do JSON
                return json.dumps(excel_data, ensure_ascii=False)

        except Exception as e:
            logger.error(f"Błąd przetwarzania XLSX {s3_key}: {e}")
            return ""

    def _process_pdf(self, s3_key: str) -> str:
        """
        Pobiera PDF z S3 i ekstrahuje tekst.
        """
        try:
            file_bytes = self.s3_service.download_bytes(self.bucket_name, s3_key)

            with io.BytesIO(file_bytes) as f:
                reader = pypdf.PdfReader(f)
                text_pages = []

                for page in reader.pages:
                    extracted = page.extract_text()
                    if extracted:
                        text_pages.append(extracted)

                return "\n".join(text_pages)

        except Exception as e:
            logger.error(f"Błąd przetwarzania PDF {s3_key}: {e}")
            return ""

    def _process_docx(self, s3_key: str) -> str:
        """
        Pobiera DOCX z S3 i ekstrahuje tekst.
        """
        try:
            file_bytes = self.s3_service.download_bytes(self.bucket_name, s3_key)

            with io.BytesIO(file_bytes) as f:
                doc = docx.Document(f)
                full_text = [para.text for para in doc.paragraphs if para.text.strip()]
                return "\n".join(full_text)

        except Exception as e:
            logger.error(f"Błąd przetwarzania DOCX {s3_key}: {e}")
            return ""

    def _process_text(self, s3_key: str) -> str:
        """
        Pobiera pliki tekstowe (TXT, MD, XML, JSON, etc.) z S3.
        """
        try:
            # Dla plików tekstowych używamy download_text, który obsługuje dekodowanie utf-8
            return self.s3_service.download_text(self.bucket_name, s3_key)
        except Exception as e:
            logger.error(f"Błąd pobierania tekstu {s3_key}: {e}")
            return ""

    def _extract_domain_first(self, s3_key: str) -> str:
        """
        Zawsze pobiera GŁÓWNY (najwyższy) folder wprost z klucza S3.
        Np. dla klucza "technical/ISO20022/MDR/plik.pdf" zwróci "technical".
        """
        # Zabezpieczenie: usuwamy ewentualne ukośniki na samym początku klucza
        clean_key = s3_key.lstrip("/")
        parts = clean_key.split('/')

        if len(parts) > 1:
            # Bierzemy ZAWSZE pierwszy, najwyższy folder w hierarchii bucketa
            return parts[0]
        else:
            # Plik leży bezpośrednio w roocie bucketa, bez żadnego folderu
            return "general"