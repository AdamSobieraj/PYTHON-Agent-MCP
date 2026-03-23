import logging
import os
import sys
from typing import Generator, Tuple, Dict, Any, List

from langchain_core.documents import Document

from buissnes_agent.MetadataModels import FileMetadata
from buissnes_agent.config_loader import settings
# Importy parserów z naszego nowego modułu
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


class DataLoaderLocalFileLoader:
    """
    Adapter dla plików lokalnych.
    Korzysta ze wzorca strategii (osobnych klas parserów) do konwersji plików na Markdown.
    """

    def __init__(self, directory: str):
        self.directory = os.path.abspath(directory)
        # Inicjalizacja parserów i mapowanie rozszerzeń
        self.parsers: Dict[str, BaseDocumentParser] = {
            ".xlsx": XlsxParser(),
            ".pdf": PdfParser(),
            ".docx": DocxParser(),
            ".pptx": PptxParser(),
        }
        # Domyślny parser (obsłuży txt, json, xml, md itp.)
        self.default_parser = TextParser()

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

    def load_file_with_metadata(self, file_path: str) -> Tuple[List[Document], Dict[str, Any]]:
        filename = os.path.basename(file_path)
        ext = os.path.splitext(file_path)[1].lower()

        domain_value = self._extract_domain_first(file_path)

        # 1. Tworzenie obiektu metadanych (Type Safe)
        # page_number zostawiamy domyślnie puste, nadpiszemy je na poziomie poszczególnych Documentów
        meta_obj = FileMetadata(
            source=f"file://{file_path}",
            title=filename,
            extension=ext,
            url=f"file://{file_path}",
            domain=domain_value,
            tags=["local", "filesystem"],
            page_number=None  # Domyślny brak strony
        )

        documents: List[Document] = []
        base_metadata = meta_obj.to_dict()

        try:
            # 2. Wybór odpowiedniego parsera
            parser = self.parsers.get(ext, self.default_parser)

            # 3. Parsowanie pliku na Markdown (przekazujemy 'ext' dla TextParsera)
            documents = parser.parse(file_path, ext=ext)

            # 4. Wzbogacanie o globalne metadane
            for doc in documents:
                # Kopiujemy bazowe metadane pliku
                merged_meta = base_metadata.copy()
                # Nadpisujemy je specyficznymi metadanymi ze strony (np. page_number z PDF)
                merged_meta.update(doc.metadata)
                # Zapisujemy połączone metadane z powrotem do dokumentu
                doc.metadata = merged_meta

            return documents, base_metadata

        except Exception as e:
            logger.error(f"Krytyczny błąd przy pliku {file_path}: {e}")
            return [], {}

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