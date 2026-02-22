import os
import tempfile
from typing import List
from langchain_core.documents import Document

# Zmieniamy import bazowy na ten z Twojego projektu
from buissnes_agent.textchunker.langchain.base import ChunkingStrategy

class UnstructuredStrategy(ChunkingStrategy):
    """
    ### Strategia 3: Unstructured Library

    Wykorzystuje zewnętrzną bibliotekę do inteligentnego parsowania Markdown.
    Potrafi rozpoznać listy, tabelki i stopki lepiej niż zwykły regex.

    **Zarządzanie zasobami:**
    Biblioteka `unstructured` operuje na plikach na dysku. Ta klasa hermetyzuje (ukrywa)
    całą logikę tworzenia i usuwania plików tymczasowych (tempfile).

    **Modes:**
    - 'single': Cały tekst jako jeden element (z wyczyszczonym formatowaniem).
    - 'elements': Dzieli na logiczne elementy (Title, NarrativeText, ListItem).
    """

    def __init__(self, mode: str = "single"):
        self.mode = mode

    def split_text(self, text: str) -> List[Document]:
        # --- FIX: Lazy Import ---
        # Importujemy bibliotekę dopiero tutaj. Jeśli jej nie ma, błąd wyskoczy
        # tylko przy próbie użycia tej konkretnej strategii, a nie przy starcie całej aplikacji.
        try:
            from langchain_community.document_loaders import UnstructuredMarkdownLoader
        except ImportError:
            raise ImportError(
                "Nie znaleziono biblioteki 'unstructured'. "
                "Zainstaluj ją komendą: pip install unstructured markdown"
            )

        suffix = ".md"
        # Tworzenie pliku tymczasowego
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp_file:
            # Kodowanie UTF-8 jest kluczowe dla polskich znaków
            temp_file.write(text.encode("utf-8"))
            temp_file_path = temp_file.name

        try:
            # Ładowanie pliku przy użyciu biblioteki unstructured
            loader = UnstructuredMarkdownLoader(temp_file_path, mode=self.mode)
            return loader.load()
        except Exception as e:
            # Logowanie błędu, jeśli parsowanie się nie uda
            print(f"Błąd podczas przetwarzania przez Unstructured: {e}")
            return []
        finally:
            # Sprzątanie po sobie (usuwanie pliku tymczasowego)
            if os.path.exists(temp_file_path):
                os.remove(temp_file_path)