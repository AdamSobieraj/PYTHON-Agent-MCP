import json
import logging
import os
import sys
from typing import Any, Dict, Generator, List, Tuple

from langchain_core.documents import Document

from DataLoaderS3Service import DataLoaderS3Service

logging.basicConfig(level=logging.INFO, stream=sys.stderr)
logger = logging.getLogger(__name__)


class DataLoaderS3FileLoader:
    """
    Reads pre-converted .md files and _metadata.json files
    saved by Project 1 (MarkDownConverter pipeline).

    Responsibilities:
        - List .md files from S3 _markdown folders
        - Download markdown content
        - Download associated metadata JSON
        - Return (List[Document], Dict) to the orchestrator

    NOT responsible for:
        - Parsing PDF/DOCX/XLSX etc.
        - Converting files to Markdown
        - Saving anything to S3
    """

    def __init__(self, bucket_name: str, prefix: str):
        self.bucket_name = bucket_name
        # 1. Remove whitespace
        clean_prefix = prefix.strip() if prefix else ""
        # 2. If prefix is provided, make sure it ends with slash "/"
        if clean_prefix:
            if not clean_prefix.endswith("/"):
                self.prefix = f"{clean_prefix}/"
            else:
                self.prefix = clean_prefix
            logger.info("S3FileLoader: Filter set to folder: '%s'", self.prefix)
        else:
            # 3. If prefix is empty -> WARNING
            self.prefix = ""
            logger.warning(
                "!!! WARNING: No folder (prefix) provided. "
                "Script will scan the ENTIRE BUCKET for .md files !!!"
            )

        self.s3_service = DataLoaderS3Service()

    # ==========================================================================
    # PUBLIC INTERFACE - matches DataLoaderInterface protocol
    # ==========================================================================

    def list_objects(self) -> Generator[str, None, None]:
        """
        Returns file keys only from the given prefix (folder).
        Skips _metadata.json files - those are loaded separately per .md file.
        """
        paginator = self.s3_service.s3_client.get_paginator('list_objects_v2')

        # Key moment: the Prefix parameter filters files on the AWS side
        # Thanks to this, we don't fetch the list of the entire bucket
        try:
            for page in paginator.paginate(
                Bucket=self.bucket_name,
                Prefix=self.prefix
            ):
                if 'Contents' not in page:
                    continue

                for obj in page['Contents']:
                    key = obj['Key']

                    # Ignore the folder itself (if AWS returns it as an object)
                    if key.endswith('/'):
                        continue

                    # Skip metadata JSON files - loaded separately
                    if key.lower().endswith('_metadata.json'):
                        continue

                    # Only yield markdown files
                    if key.lower().endswith('.md'):
                        yield key

        except Exception as e:
            logger.error("S3Service Error listing objects: %s", e)
            raise

    def load_file_with_metadata(
        self,
        md_key: str
    ) -> Tuple[List[Document], Dict[str, Any]]:
        """
        Fetches the markdown file content and its metadata based on the key.

        Steps:
            1. Download .md file content from S3
            2. Download _metadata.json saved by Project 1
            3. Create Document object from markdown content
            4. Return (documents, metadata)

        Returns: (list_of_pages_as_documents, base_metadata_dict)
        """
        logger.info("S3FileLoader: Loading markdown file: %s", md_key)

        try:
            # Step 1: Download markdown content
            markdown_text = self._download_markdown(md_key)

            if not markdown_text:
                logger.warning("S3FileLoader: Empty markdown file: %s", md_key)
                return [], {}

            # Step 2: Load metadata JSON saved by Project 1
            base_metadata = self._load_metadata_json(md_key)

            # Step 3: Enrich metadata with any missing fields we can derive
            base_metadata = self._enrich_metadata(md_key, base_metadata)

            # Step 4: Create Document
            doc = Document(
                page_content=markdown_text,
                metadata=base_metadata.copy()
            )

            logger.info(
                "S3FileLoader: Successfully loaded '%s' "
                "(%d chars, %d metadata keys)",
                md_key,
                len(markdown_text),
                len(base_metadata)
            )

            return [doc], base_metadata

        except Exception as e:
            logger.error(
                "Critical error at file %s: %s",
                md_key, e
            )
            # Returns empty list instead of "", prevents errors in Orchestrator
            return [], {}

    # ==========================================================================
    # PRIVATE HELPERS
    # ==========================================================================

    def _download_markdown(self, md_key: str) -> str:
        """
        Downloads markdown file content from S3.

        Args:
            md_key: S3 key of the .md file

        Returns:
            Markdown content as string
        """
        try:
            text = self.s3_service.download_text(self.bucket_name, md_key)
            logger.debug(
                "S3FileLoader: Downloaded markdown '%s' (%d chars)",
                md_key, len(text)
            )
            return text
        except Exception as e:
            logger.error(
                "S3FileLoader: Failed to download markdown '%s': %s",
                md_key, e
            )
            raise

    def _load_metadata_json(self, md_key: str) -> Dict[str, Any]:
        """
        Downloads and parses the _metadata.json file associated
        with the given markdown file.

        Project 1 naming convention (from S3DataSaver._build_metadata_key):
            "technical/ISO20022_markdown/file.md"
         -> "technical/ISO20022_markdown/file_metadata.json"

        Args:
            md_key: S3 key of the .md file

        Returns:
            Metadata dictionary, or empty dict if not found
        """
        metadata_key = self._build_metadata_key(md_key)

        try:
            json_text = self.s3_service.download_text(
                self.bucket_name,
                metadata_key
            )
            metadata = json.loads(json_text)
            logger.debug(
                "S3FileLoader: Loaded metadata from '%s' (%d keys)",
                metadata_key, len(metadata)
            )
            return metadata

        except Exception as e:
            logger.warning(
                "S3FileLoader: Metadata not found for '%s' "
                "(expected at '%s'): %s. Using empty metadata.",
                md_key, metadata_key, e
            )
            return {}

    def _build_metadata_key(self, md_key: str) -> str:
        """
        Derives the metadata JSON S3 key from the markdown S3 key.

        Mirrors Project 1's S3DataSaver._build_metadata_key() naming:
            "technical/ISO20022_markdown/file.md"
         -> "technical/ISO20022_markdown/file_metadata.json"

        Args:
            md_key: S3 key of the .md file

        Returns:
            S3 key of the associated _metadata.json file
        """
        # Remove .md extension, append _metadata.json
        base = os.path.splitext(md_key)[0]
        return f"{base}_metadata.json"

    def _enrich_metadata(
        self,
        md_key: str,
        metadata: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Adds any metadata fields that might be missing from the JSON.
        Uses derivable information from the S3 key itself as fallback.

        Args:
            md_key: S3 key of the .md file
            metadata: Metadata loaded from _metadata.json

        Returns:
            Enriched metadata dictionary
        """
        enriched = metadata.copy()

        # Fallback: markdown_path (should already be in Project 1 metadata)
        if 'markdown_path' not in enriched:
            enriched['markdown_path'] = md_key

        # Fallback: markdown_url
        if 'markdown_url' not in enriched:
            enriched['markdown_url'] = (
                f"https://{self.bucket_name}.s3.amazonaws.com/{md_key}"
            )

        # Fallback: source (should already exist from Project 1's FileMetadata)
        if 'source' not in enriched:
            enriched['source'] = f"s3://{self.bucket_name}/{md_key}"

        # Fallback: domain
        if 'domain' not in enriched:
            enriched['domain'] = self._extract_domain_first(md_key)

        # Fallback: extension (original file extension, not .md)
        if 'extension' not in enriched:
            enriched['extension'] = '.md'

        return enriched

    def _extract_domain_first(self, s3_key: str) -> str:
        """
        Always fetches the MAIN (highest) folder directly from the S3 key.
        E.g., for key "technical/ISO20022/MDR/file.pdf" will return "technical".
        """
        # Safety: remove any leading slashes from the key
        clean_key = s3_key.lstrip("/")
        parts = clean_key.split("/")

        if len(parts) > 1:
            # Always take the FIRST, highest folder in the bucket hierarchy
            return parts[0]
        # File lies directly in the bucket root, without any folder
        return "general"