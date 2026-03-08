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

    def split_documents(self, documents: List[Document]) -> List[Document]:
        try:
            from langchain_community.document_loaders import UnstructuredMarkdownLoader
        except ImportError:
            raise ImportError("Brak unstructured. Uruchom: pip install unstructured markdown")

        final_chunks = []
        suffix = ".md"

        # Przetwarzamy KAZDĄ STRONĘ (Document) z osobna, aby przypisać jej numer do wyniku
        for doc in documents:
            with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp_file:
                temp_file.write(doc.page_content.encode("utf-8"))
                temp_file_path = temp_file.name

            try:
                loader = UnstructuredMarkdownLoader(temp_file_path, mode=self.mode)
                unstructured_docs = loader.load()

                # Dodajemy metadane ze strony (np. nr strony) do wygenerowanych chunków
                for u_doc in unstructured_docs:
                    u_doc.metadata.update(doc.metadata)
                    final_chunks.append(u_doc)
            except Exception as e:
                print(f"Błąd podczas przetwarzania przez Unstructured: {e}")
            finally:
                if os.path.exists(temp_file_path):
                    os.remove(temp_file_path)

        return final_chunks