import logging
import os

from interfaces.DataSaver import BaseDataSaver
from DataLoaderS3Service import DataLoaderS3Service

logger = logging.getLogger(__name__)


class S3DataSaver(BaseDataSaver):
    """
    Saves markdown files to S3.
    Only responsible for writing files - no parsing, no metadata building.
    """

    def __init__(self, bucket_name: str):
        """
        Args:
            bucket_name: S3 bucket name
        """
        self.bucket_name = bucket_name
        self.s3_service = DataLoaderS3Service()

    def save_markdown(
            self,
            source_key: str,
            markdown_content: str,
    ) -> str:
        """
        Saves markdown to S3 in folder with '_markdown' suffix.

        Args:
            source_key: Original file S3 key (e.g., "technical/file.pdf")
            markdown_content: Markdown text to save

        Returns:
            str: S3 key of saved markdown file
        """
        markdown_key = self._build_markdown_key(source_key)

        # Convert to bytes
        markdown_bytes = markdown_content.encode("utf-8")

        # Upload to S3
        self.s3_service.upload_bytes(
            bucket_name=self.bucket_name,
            key=markdown_key,
            data=markdown_bytes,
            content_type="text/markdown",
        )

        logger.info(f"Saved markdown to S3: s3://{self.bucket_name}/{markdown_key}")
        return markdown_key

    def get_markdown_url(self, markdown_key: str) -> str:
        """Generates public S3 URL for markdown file."""
        return f"https://{self.bucket_name}.s3.amazonaws.com/{markdown_key}"

    def _build_markdown_key(self, source_key: str) -> str:
        """
        Builds S3 key for markdown file.
        E.g., "technical/ISO20022/file.pdf" -> "technical/ISO20022_markdown/file.md"
        """
        filename_without_ext = os.path.splitext(os.path.basename(source_key))[0]
        s3_dir = os.path.dirname(source_key)

        markdown_dir = f"{s3_dir}_markdown" if s3_dir else "root_markdown"
        markdown_filename = f"{filename_without_ext}.md"

        return f"{markdown_dir}/{markdown_filename}"