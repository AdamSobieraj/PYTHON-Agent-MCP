import io
import logging
import os
import sys
from typing import Dict, Any, Generator, Tuple, List

from langchain_core.documents import Document

from DataLoaderS3Service import DataLoaderS3Service
from buissnes_agent.MetadataModels import FileMetadata
# Importujemy nasze moduły parserów
from buissnes_agent.parsers import (
    BaseDocumentParser,
    XlsxParser,
    DocxParser,
    PdfParser,
    TextParser,
    PptxParser
)

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

        # Inicjalizacja parserów i mapowanie rozszerzeń
        self.parsers: Dict[str, BaseDocumentParser] = {
            ".xlsx": XlsxParser(),
            ".pdf": PdfParser(),
            ".docx": DocxParser(),
            ".pptx": PptxParser(),
        }
        # Domyślny parser dla tekstów (TXT, JSON, XML, itd.)
        self.default_parser = TextParser()

    def list_objects(self) -> Generator[str, None, None]:
        # Przekazujemy prefix do serwisu S3. AWS zwróci tylko obiekty zaczynające się od tego ciągu.
        return self.s3_service.list_objects(self.bucket_name, self.prefix)

    def save_markdown_to_s3(self, s3_key: str, documents: List[Document]) -> str:
        """
        Zapisuje dokumenty Markdown do S3 w folderze o takiej samej nazwie jak oryginalny + '_markdown'.

        Args:
            s3_key: Klucz S3 pliku źródłowego (np. "technical/ISO20022/plik.pdf")
            documents: Lista dokumentów z zawartością Markdown

        Returns:
            Klucz S3 zapisanego pliku Markdown (ścieżka w S3)
        """
        # Pobierz nazwę pliku bez rozszerzenia
        filename_without_ext = os.path.splitext(os.path.basename(s3_key))[0]

        # Pobierz ścieżkę folderów z klucza S3
        s3_dir = os.path.dirname(s3_key)

        # Dodaj suffix '_markdown' do struktury folderów
        if s3_dir:
            # Jeśli jest struktura folderów, dodaj '_markdown' na końcu
            markdown_dir = s3_dir + "_markdown"
        else:
            # Jeśli plik był w głównym katalogu bucketa
            markdown_dir = "root_markdown"

        # Ścieżka do pliku Markdown w S3
        markdown_filename = f"{filename_without_ext}.md"
        markdown_s3_key = f"{markdown_dir}/{markdown_filename}"

        # Połącz wszystkie dokumenty w jeden string Markdown
        markdown_content = []
        for i, doc in enumerate(documents):
            if i > 0:
                markdown_content.append("\n\n---\n\n")  # Separator między stronami/sekcjami
            markdown_content.append(doc.page_content)

        full_markdown = "".join(markdown_content)

        # Zapisz do S3
        try:
            markdown_bytes = full_markdown.encode('utf-8')
            self.s3_service.upload_bytes(
                bucket_name=self.bucket_name,
                key=markdown_s3_key,
                data=markdown_bytes,
                content_type='text/markdown'
            )

            s3_url = f"s3://{self.bucket_name}/{markdown_s3_key}"
            logger.info(f"✓ Zapisano Markdown do S3: {s3_url}")
            return s3_url

        except Exception as e:
            logger.error(f"Błąd podczas zapisywania Markdown do S3: {e}")
            raise

    def load_file_with_metadata(self, s3_key: str) -> Tuple[List[Document], Dict[str, Any]]:
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

        documents: List[Document] = []
        base_metadata = meta_obj.to_dict()

        try:
            # 1. Pobieramy bajty z chmury do pamięci RAM
            file_bytes = self.s3_service.download_bytes(self.bucket_name, s3_key)

            # 2. Wybieramy odpowiedni parser
            parser = self.parsers.get(ext, self.default_parser)

            # 3. Parsowanie - w zależności od formatu wysyłamy bajty lub strumień (BytesIO)
            # TextParser poradzi sobie z czystymi bajtami. Pozostałe (openpyxl, docx, pypdf) potrzebują BytesIO
            if ext in self.parsers:
                file_source = io.BytesIO(file_bytes)
            else:
                file_source = file_bytes

            # 4. Magia dzieje się tutaj - parser przetwarza plik w pamięci i oddaje Markdown
            documents = parser.parse(file_source, ext=ext)

            # 5. Wzbogacamy strony o metadane globalne S3
            for doc in documents:
                merged_meta = base_metadata.copy()
                merged_meta.update(doc.metadata)
                doc.metadata = merged_meta

            # 6. Zapisz Markdown do S3 i dodaj ścieżkę do metadanych
            if documents:
                markdown_s3_path = self.save_markdown_to_s3(s3_key, documents)
                # Dodaj ścieżkę do Markdown w metadanych
                base_metadata['markdown_path'] = markdown_s3_path
                base_metadata[
                    'markdown_url'] = f"https://{self.bucket_name}.s3.amazonaws.com/{markdown_s3_path.replace('s3://' + self.bucket_name + '/', '')}"

                for doc in documents:
                    doc.metadata['markdown_path'] = markdown_s3_path
                    doc.metadata['markdown_url'] = base_metadata['markdown_url']

            return documents, base_metadata

        except Exception as e:
            logger.error(f"Krytyczny błąd przy pliku {s3_key}: {e}")
            return [], {}  # <--- POPRAWKA: Zwraca pustą listę zamiast "", zapobiega błędom w Orkiestratorze

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