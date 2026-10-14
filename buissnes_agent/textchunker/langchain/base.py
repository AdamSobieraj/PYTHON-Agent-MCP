from abc import ABC, abstractmethod
from typing import List
from langchain_core.documents import Document


class ChunkingStrategy(ABC):
    """
    ### Abstract Class: Strategy Interface

    Defines the contract that every text-splitting method must fulfill.
    This way the main class (LangChainChunker) does not need to know the implementation
    details (e.g. whether AI or regular expressions are used), it only calls the `split_text` method.

    **Extension:**
    This is the foundation of the Strategy pattern. If we ever want to add, for example,
    Python code splitting, we only need to add a new class inheriting from ChunkingStrategy,
    without modifying the main engine.
    """

    @abstractmethod
    def split_documents(self, documents: List[Document]) -> List[Document]:
        """
        Method responsible for logically splitting the text into smaller fragments (Document objects).
        Each strategy implements this method in its own way.
        """
        pass