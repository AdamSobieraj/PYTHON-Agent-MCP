from typing import List
from langchain_core.documents import Document
from langchain_text_splitters import MarkdownHeaderTextSplitter

# Import interfejsu bazowego (zakładając strukturę katalogów)
from buissnes_agent.textchunker.langchain.base import ChunkingStrategy


class MarkdownHeaderStrategy(ChunkingStrategy):
    """
    ### Strategia 1: Markdown Headers (Strukturalna)

    Dzieli tekst w miejscach występowania nagłówków (#, ##, ###).
    Idealna dla dobrze sformatowanej dokumentacji technicznej.

    **Zaleta:** Zachowuje nagłówek w metadanych lub treści, co daje świetny kontekst.
    **Wada:** Jeśli sekcja pod nagłówkiem jest pusta lub gigantyczna, strategia sama z siebie tego nie poprawi.

    **Implementacja:**
    Logika została wyizolowana. Klasa nie potrzebuje zewnętrznych parametrów (chunk_size),
    ponieważ tnie strictly po strukturze dokumentu.
    """

    def split_documents(self, documents: List[Document]) -> List[Document]:
        headers_to_split_on = [("#", "Header 1"), ("##", "Header 2"), ("###", "Header 3")]
        markdown_splitter = MarkdownHeaderTextSplitter(
            headers_to_split_on=headers_to_split_on,
            strip_headers=False
        )

        final_chunks = []
        for doc in documents:
            # Dzielimy treść pojedynczej strony (doc)
            chunks = markdown_splitter.split_text(doc.page_content)
            # Ręcznie dodajemy metadane strony do nowych chunków
            for chunk in chunks:
                chunk.metadata.update(doc.metadata)
                final_chunks.append(chunk)

        return final_chunks