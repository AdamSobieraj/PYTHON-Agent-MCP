from dataclasses import dataclass, asdict, field
from typing import List, Dict, Any, Optional


@dataclass
class BaseMetadata:
    """
    Common fields for files and chunks.
    Defines the metadata 'backbone' in the system.
    """
    source: str                             # Mandatory URI (file:// or s3://)
    title: Optional[str] = None
    url: Optional[str] = None
    extension: Optional[str] = None
    domain: Optional[str] = "general"
    tags: List[str] = field(default_factory=list)
    page_number: Optional[int] = None

    # Original PDF page number the chunk was taken from
    pdf_page: Optional[int] = None

    # Line range of the entire source page in the original markdown file
    document_line_start: Optional[int] = None
    document_line_end: Optional[int] = None

    # Line range of this specific chunk in the markdown file
    md_start_line: Optional[int] = None
    md_end_line: Optional[int] = None

    def _clean_dict(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Helper method that removes None values from results.
        Keeps assigned values, including page_number.
        """
        return {k: v for k, v in data.items() if v is not None}


@dataclass
class FileMetadata(BaseMetadata):
    """
    Model used by Loaders (S3/Local).
    Represents the entire file before splitting.
    """
    def to_dict(self) -> Dict[str, Any]:
        return self._clean_dict(asdict(self))


@dataclass
class ChunkMetadata(BaseMetadata):
    """
    Model used by Chunkers (LangChain/NoLib).
    Represents a single vector in the Qdrant database.
    """
    phrase: str = ""                            # Fragment content
    phrase_metadata_id: str = ""                # Unique ID

    # Container for overflow/undefined data
    extra_data: Dict[str, Any] = field(default_factory=dict)

    def to_payload(self) -> Dict[str, Any]:
        """
        Generates a flat dictionary ready for insertion into Qdrant.
        """
        data = asdict(self)

        # 1. Extract and flatten extra_data
        extras = data.pop("extra_data", {})

        # 2. Remove None values (if page_number is e.g. 1, it stays in the dict)
        clean_data = self._clean_dict(data)

        # 3. Merge (Schema has priority over extras)
        return {**extras, **clean_data}