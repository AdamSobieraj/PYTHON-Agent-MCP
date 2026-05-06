import logging
import os
import sys
from typing import Generator, Tuple, Dict, Any, List

from langchain_core.documents import Document

from buissnes_agent.MetadataModels import FileMetadata
from buissnes_agent.config_loader import get_settings
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

        # Katalog docelowy dla plików Markdown
        self.markdown_directory = self.directory + "_markdown"

        # Inicjalizacja parserów i mapowanie rozszerzeń
        self.parsers: Dict[str, BaseDocumentParser] = {
            ".xlsx": XlsxParser(),
            ".pdf": PdfParser(),
            ".docx": DocxParser(),
            ".pptx": PptxParser(),
        }
        # Domyślny parser (obsłuży txt, json, xml, md itp.)
        self.default_parser = TextParser()
        self.settings = get_settings()

    def _get_markdown_path(self, original_file_path: str) -> str:
        """
        Tworzy ścieżkę do pliku markdown na podstawie oryginalnej ścieżki.
        Np. /dane/HR/dokument.pdf -> /dane_markdown/HR/dokument.md
        """
        # Pobierz ścieżkę względną względem głównego katalogu
        rel_path = os.path.relpath(original_file_path, self.directory)

        # Zmień rozszerzenie na .md
        base_name = os.path.splitext(rel_path)[0]
        markdown_rel_path = base_name + ".md"

        # Połącz z katalogiem docelowym
        markdown_full_path = os.path.join(self.markdown_directory, markdown_rel_path)

        return markdown_full_path

    def _save_markdown(self, documents: List[Document], markdown_path: str) -> None:
        """
        Zapisuje zawartość Markdown do pliku.
        Łączy wszystkie dokumenty z listy w jeden plik.
        """
        # Utwórz katalog, jeśli nie istnieje
        os.makedirs(os.path.dirname(markdown_path), exist_ok=True)

        # Połącz wszystkie dokumenty w jeden Markdown
        # Jeśli jest wiele stron/sekcji, rozdziel je separatorem
        markdown_content = []
        for i, doc in enumerate(documents):
            if i > 0:
                # Dodaj separator między dokumentami/stronami
                markdown_content.append("\n\n---\n\n")

            # Dodaj informację o stronie, jeśli istnieje
            if doc.metadata.get('page_number'):
                markdown_content.append(f"<!-- Page {doc.metadata['page_number']} -->\n\n")

            markdown_content.append(doc.page_content)

        # Zapisz plik
        with open(markdown_path, 'w', encoding='utf-8') as f:
            f.write(''.join(markdown_content))

        logger.info(f"Zapisano Markdown: {markdown_path}")

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

            # 4. Generowanie ścieżki dla pliku Markdown
            markdown_path = self._get_markdown_path(file_path)

            # 5. Zapis pliku Markdown
            if documents:
                self._save_markdown(documents, markdown_path)

            # 6. Dodanie ścieżki markdown do bazowych metadanych
            base_metadata['markdown_path'] = markdown_path

            # 6. Wzbogacanie o globalne metadane
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