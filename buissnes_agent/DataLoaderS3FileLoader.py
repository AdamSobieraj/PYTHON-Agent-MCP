import io
import logging
import os
import sys
from typing import Any, Dict, Generator, List, Tuple

from langchain_core.documents import Document

from DataLoaderS3Service import DataLoaderS3Service
from buissnes_agent.MetadataModels import FileMetadata
from buissnes_agent.parsers import (
    BaseDocumentParser,
    DocxParser,
    PdfParser,
    PptxParser,
    TextParser,
    XlsxParser,
)

logging.basicConfig(level=logging.INFO, stream=sys.stderr)
logger = logging.getLogger(__name__)


class DataLoaderS3FileLoader:
    def __init__(self, bucket_name: str, prefix: str):
        self.bucket_name = bucket_name

        clean_prefix = prefix.strip() if prefix else ""
        if clean_prefix:
            if not clean_prefix.endswith("/"):
                self.prefix = f"{clean_prefix}/"
            else:
                self.prefix = clean_prefix
            logger.info("S3FileLoader: Ustawiono filtr na folder: '%s'", self.prefix)
        else:
            self.prefix = ""
            logger.warning(
                "!!! UWAGA: Nie podano folderu (prefix). Skrypt pobierze CALY BUCKET !!!"
            )

        self.s3_service = DataLoaderS3Service()

        # Create heavy parsers only when a file with the matching extension is used.
        self.parser_factories: Dict[str, type[BaseDocumentParser]] = {
            ".xlsx": XlsxParser,
            ".pdf": PdfParser,
            ".docx": DocxParser,
            ".pptx": PptxParser,
        }
        self.parsers: Dict[str, BaseDocumentParser] = {}
        self.default_parser = TextParser()

    def list_objects(self) -> Generator[str, None, None]:
        return self.s3_service.list_objects(self.bucket_name, self.prefix)

    def save_markdown_to_s3(self, s3_key: str, documents: List[Document]) -> str:
        """
        Save parsed markdown next to the original structure with a _markdown suffix.
        """
        filename_without_ext = os.path.splitext(os.path.basename(s3_key))[0]
        s3_dir = os.path.dirname(s3_key)

        if s3_dir:
            markdown_dir = s3_dir + "_markdown"
        else:
            markdown_dir = "root_markdown"

        markdown_filename = f"{filename_without_ext}.md"
        markdown_s3_key = f"{markdown_dir}/{markdown_filename}"

        markdown_content: List[str] = []
        for index, doc in enumerate(documents):
            if index > 0:
                markdown_content.append("\n\n---\n\n")
            markdown_content.append(doc.page_content)

        full_markdown = "".join(markdown_content)

        try:
            markdown_bytes = full_markdown.encode("utf-8")
            self.s3_service.upload_bytes(
                bucket_name=self.bucket_name,
                key=markdown_s3_key,
                data=markdown_bytes,
                content_type="text/markdown",
            )

            s3_url = f"s3://{self.bucket_name}/{markdown_s3_key}"
            logger.info("Zapisano Markdown do S3: %s", s3_url)
            return s3_url
        except Exception as exc:
            logger.error("Blad podczas zapisywania Markdown do S3: %s", exc)
            raise

    def load_file_with_metadata(self, s3_key: str) -> Tuple[List[Document], Dict[str, Any]]:
        filename = os.path.basename(s3_key)
        ext = os.path.splitext(s3_key)[1].lower()
        domain_value = self._extract_domain_first(s3_key)

        meta_obj = FileMetadata(
            source=f"s3://{self.bucket_name}/{s3_key}",
            title=filename,
            extension=ext,
            url=f"https://{self.bucket_name}.s3.amazonaws.com/{s3_key}",
            domain=domain_value,
            tags=["s3_storage", "cloud", domain_value.lower()],
            page_number=None,
        )

        documents: List[Document] = []
        base_metadata = meta_obj.to_dict()

        try:
            file_bytes = self.s3_service.download_bytes(self.bucket_name, s3_key)
            parser = self._get_parser(ext)

            if ext in self.parser_factories:
                file_source = io.BytesIO(file_bytes)
            else:
                file_source = file_bytes

            documents = parser.parse(file_source, ext=ext)

            for doc in documents:
                merged_meta = base_metadata.copy()
                merged_meta.update(doc.metadata)
                doc.metadata = merged_meta

            if documents:
                markdown_s3_path = self.save_markdown_to_s3(s3_key, documents)
                base_metadata["markdown_path"] = markdown_s3_path
                base_metadata["markdown_url"] = (
                    f"https://{self.bucket_name}.s3.amazonaws.com/"
                    f"{markdown_s3_path.replace('s3://' + self.bucket_name + '/', '')}"
                )

                for doc in documents:
                    doc.metadata["markdown_path"] = markdown_s3_path
                    doc.metadata["markdown_url"] = base_metadata["markdown_url"]

            return documents, base_metadata
        except Exception as exc:
            logger.error("Krytyczny blad przy pliku %s: %s", s3_key, exc)
            return [], {}

    def _extract_domain_first(self, s3_key: str) -> str:
        clean_key = s3_key.lstrip("/")
        parts = clean_key.split("/")

        if len(parts) > 1:
            return parts[0]
        return "general"

    def _get_parser(self, ext: str) -> BaseDocumentParser:
        if ext not in self.parser_factories:
            return self.default_parser

        if ext not in self.parsers:
            logger.info("S3FileLoader: Inicjalizacja parsera dla rozszerzenia '%s'", ext)
            self.parsers[ext] = self.parser_factories[ext]()

        return self.parsers[ext]
