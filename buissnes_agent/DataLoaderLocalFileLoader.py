import json
import logging
import os
import sys
from typing import Any, Dict, Generator, List, Tuple

from langchain_core.documents import Document

from buissnes_agent.config_loader import get_settings

logging.basicConfig(level=logging.INFO, stream=sys.stderr)
logger = logging.getLogger(__name__)


class DataLoaderLocalFileLoader:
    """
    Adapter for pre-converted local markdown files.
    Reads .md files and _metadata.json files
    saved by Project 1 (MarkDownConverter pipeline).

    Reads from the _markdown directory created by Project 1's LocalDataSaver:
        source directory:   /data/HR/
        markdown directory: /data_markdown/HR/   <- reads from here

    Responsibilities:
        - List .md files from local _markdown directory
        - Read markdown content from disk
        - Read associated metadata JSON from disk
        - Return (List[Document], Dict) to the orchestrator

    NOT responsible for:
        - Parsing PDF/DOCX/XLSX etc.
        - Converting files to Markdown
        - Saving anything to disk
    """

    def __init__(self, directory: str):
        self.directory = os.path.abspath(directory)

        # Target directory for Markdown files - mirrors Project 1's LocalDataSaver
        # If user passes original dir -> append _markdown
        # If user passes _markdown dir directly -> use as is
        if self.directory.endswith("_markdown"):
            self.markdown_directory = self.directory
            logger.info(
                "LocalFileLoader: Reading directly from markdown directory: '%s'",
                self.markdown_directory
            )
        else:
            self.markdown_directory = self.directory + "_markdown"
            logger.info(
                "LocalFileLoader: Source directory '%s' -> "
                "Reading markdown from '%s'",
                self.directory,
                self.markdown_directory
            )

        if not os.path.exists(self.markdown_directory):
            logger.warning(
                "LocalFileLoader: Markdown directory does not exist: '%s'. "
                "Has Project 1 been run yet?",
                self.markdown_directory
            )

        self.settings = get_settings()

    # ==========================================================================
    # PUBLIC INTERFACE - matches DataLoaderInterface protocol
    # ==========================================================================

    def list_objects(self) -> Generator[str, None, None]:
        """
        Returns file paths only from the markdown directory.
        Skips _metadata.json files - those are loaded separately per .md file.
        """
        allowed_exts = self.settings.get("chunking.allowed_extensions", [])

        if not os.path.exists(self.markdown_directory):
            logger.error(
                "Directory does not exist: %s",
                self.markdown_directory
            )
            return

        for root, _, files in os.walk(self.markdown_directory):
            for file in files:
                # Skip metadata JSON files - loaded separately
                if file.lower().endswith('_metadata.json'):
                    continue

                # Only yield markdown files
                if file.lower().endswith('.md'):
                    yield os.path.join(root, file)

    def load_file_with_metadata(
        self,
        file_path: str
    ) -> Tuple[List[Document], Dict[str, Any]]:
        """
        Fetches the markdown file content and its metadata based on the path.

        Steps:
            1. Read .md file content from disk
            2. Read _metadata.json saved by Project 1
            3. Create Document object from markdown content
            4. Return (documents, metadata)

        Returns: (list_of_pages_as_documents, base_metadata_dict)
        """
        logger.info("LocalFileLoader: Loading markdown file: %s", file_path)

        try:
            # Step 1: Read markdown content
            markdown_text = self._read_markdown(file_path)

            if not markdown_text:
                logger.warning(
                    "LocalFileLoader: Empty markdown file: %s",
                    file_path
                )
                return [], {}

            # Step 2: Load metadata JSON saved by Project 1
            base_metadata = self._load_metadata_json(file_path)

            # Step 3: Enrich metadata with any missing fields we can derive
            base_metadata = self._enrich_metadata(file_path, base_metadata)

            # Step 4: Create Document
            doc = Document(
                page_content=markdown_text,
                metadata=base_metadata.copy()
            )

            logger.info(
                "LocalFileLoader: Successfully loaded '%s' "
                "(%d chars, %d metadata keys)",
                file_path,
                len(markdown_text),
                len(base_metadata)
            )

            return [doc], base_metadata

        except Exception as e:
            logger.error(
                "Critical error at file %s: %s",
                file_path, e
            )
            # Returns empty list instead of "", prevents errors in Orchestrator
            return [], {}

    # ==========================================================================
    # PRIVATE HELPERS
    # ==========================================================================

    def _read_markdown(self, file_path: str) -> str:
        """
        Reads markdown file content from disk.

        Args:
            file_path: Absolute path to the .md file

        Returns:
            Markdown content as string
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            logger.debug(
                "LocalFileLoader: Read markdown '%s' (%d chars)",
                file_path, len(content)
            )
            return content

        except Exception as e:
            logger.error(
                "LocalFileLoader: Failed to read markdown '%s': %s",
                file_path, e
            )
            raise

    def _load_metadata_json(self, file_path: str) -> Dict[str, Any]:
        """
        Reads and parses the _metadata.json file associated
        with the given markdown file.

        Project 1 naming convention (from LocalDataSaver._build_metadata_path):
            "/data_markdown/HR/document.md"
         -> "/data_markdown/HR/document_metadata.json"

        Args:
            file_path: Absolute path to the .md file

        Returns:
            Metadata dictionary, or empty dict if not found
        """
        metadata_path = self._build_metadata_path(file_path)

        try:
            with open(metadata_path, 'r', encoding='utf-8') as f:
                metadata = json.load(f)

            logger.debug(
                "LocalFileLoader: Loaded metadata from '%s' (%d keys)",
                metadata_path, len(metadata)
            )
            return metadata

        except FileNotFoundError:
            logger.warning(
                "LocalFileLoader: Metadata file not found for '%s' "
                "(expected at '%s'). Using empty metadata.",
                file_path, metadata_path
            )
            return {}

        except json.JSONDecodeError as e:
            logger.warning(
                "LocalFileLoader: Invalid JSON in metadata file '%s': %s. "
                "Using empty metadata.",
                metadata_path, e
            )
            return {}

        except Exception as e:
            logger.warning(
                "LocalFileLoader: Could not read metadata '%s': %s. "
                "Using empty metadata.",
                metadata_path, e
            )
            return {}

    def _build_metadata_path(self, file_path: str) -> str:
        """
        Derives the metadata JSON path from the markdown file path.

        Mirrors Project 1's LocalDataSaver._build_metadata_path() naming:
            "/data_markdown/HR/document.md"
         -> "/data_markdown/HR/document_metadata.json"

        Args:
            file_path: Absolute path to the .md file

        Returns:
            Absolute path to the associated _metadata.json file
        """
        # Remove .md extension, append _metadata.json
        base = os.path.splitext(file_path)[0]
        return f"{base}_metadata.json"

    def _enrich_metadata(
        self,
        file_path: str,
        metadata: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Adds any metadata fields that might be missing from the JSON.
        Uses derivable information from the file path itself as fallback.

        Args:
            file_path: Absolute path to the .md file
            metadata: Metadata loaded from _metadata.json

        Returns:
            Enriched metadata dictionary
        """
        enriched = metadata.copy()

        # Fallback: markdown_path
        if 'markdown_path' not in enriched:
            enriched['markdown_path'] = file_path

        # Fallback: source (should exist from Project 1's FileMetadata)
        if 'source' not in enriched:
            enriched['source'] = f"file://{file_path}"

        # Fallback: domain
        if 'domain' not in enriched:
            enriched['domain'] = self._extract_domain_first(file_path)

        # Fallback: title
        if 'title' not in enriched:
            enriched['title'] = os.path.basename(file_path)

        # Fallback: extension (of the markdown file)
        if 'extension' not in enriched:
            enriched['extension'] = '.md'

        return enriched

    def _extract_domain_first(self, file_path: str) -> str:
        """
        Fetches the domain name based on the file path.
        Domain is the first directory relative to the main search folder (self.markdown_directory).
        E.g., for file "/data_markdown/HR/contracts/2023/contract.md"
        (when self.markdown_directory="/data_markdown") will return "HR".
        """
        # Calculate relative path of the file in relation to the searched directory
        rel_path = os.path.relpath(file_path, self.markdown_directory)

        # Normalize slashes so split behaves the same on Windows and Linux
        normalized_rel_path = rel_path.replace('\\', '/')
        parts = normalized_rel_path.split('/')

        if len(parts) > 1:
            # File lies in some subdirectory. Take the HIGHEST level folder.
            return parts[0]
        else:
            # File lies directly in the main search directory.
            # Fallback to the name of that main directory or "local"
            return os.path.basename(self.markdown_directory) or "local"