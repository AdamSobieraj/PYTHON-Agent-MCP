import argparse
import io
import logging
import os
import sys
from typing import List, Dict, Any, Literal

from langchain_core.documents import Document
from tqdm import tqdm

from builders.metadata_builder import MetadataBuilder
from interfaces.DataLoader import BaseDataLoader
from interfaces.DataSaver import BaseDataSaver
from loaders.DataLoaderLocal import LocalDataLoader
from loaders.DataLoaderS3 import S3DataLoader
from parsers.ParserSelector import ParserSelector
from savers.DataSaverLocal import LocalDataSaver
from savers.DataSaverS3 import S3DataSaver

logger = logging.getLogger(__name__)


class MarkDownConverter:
    """
    Main pipeline orchestrator for converting documents to Markdown.

    Pipeline steps:
        1. Load raw data (from S3 or Local)
        2. Select appropriate parser
        3. Parse to Markdown
        4. Save Markdown (to S3 or Local) with metadata

    Each step is delegated to specialized components following Single Responsibility Principle.
    """

    def __init__(
            self,
            source_type: Literal["s3", "local"],
            destination_type: Literal["s3", "local"] = None,
            **config
    ):
        """
        Args:
            source_type: Where to load files from ("s3" or "local")
            destination_type: Where to save markdown (defaults to same as source)
            **config: Configuration for source/destination

            For S3 source:
                - bucket_name (str): Bucket name
                - prefix (str, optional): Folder prefix

            For Local source:
                - directory (str): Directory path

            For S3 destination:
                - output_bucket (str, optional): Output bucket (defaults to source bucket)

            For Local destination:
                - output_directory (str, optional): Output directory (defaults to source_dir + "_markdown")
        """
        self.source_type = source_type
        self.destination_type = destination_type or source_type

        # Initialize components
        self.loader = self._create_loader(source_type, config)
        self.saver = self._create_saver(self.destination_type, config)
        self.parser_selector = ParserSelector()
        self.metadata_builder = MetadataBuilder()

        logger.info(
            f"MarkDownConverter initialized: {source_type.upper()} -> {self.destination_type.upper()}"
        )

    def _create_loader(self, source_type: str, config: Dict[str, Any]) -> BaseDataLoader:
        """Factory method for creating data loader."""
        if source_type == "s3":
            bucket_name = config.get("bucket_name")
            if not bucket_name:
                raise ValueError("S3 source requires 'bucket_name' parameter")

            prefix = config.get("prefix", "")
            return S3DataLoader(bucket_name=bucket_name, prefix=prefix)

        elif source_type == "local":
            directory = config.get("directory")
            if not directory:
                raise ValueError("Local source requires 'directory' parameter")

            return LocalDataLoader(directory=directory)

        else:
            raise ValueError(f"Unknown source type: {source_type}")

    def _create_saver(self, destination_type: str, config: Dict[str, Any]) -> BaseDataSaver:
        """Factory method for creating data saver."""
        if destination_type == "s3":
            # Use output_bucket if specified, otherwise use source bucket
            bucket_name = config.get("output_bucket") or config.get("bucket_name")
            if not bucket_name:
                raise ValueError("S3 destination requires 'bucket_name' or 'output_bucket' parameter")

            return S3DataSaver(bucket_name=bucket_name)

        elif destination_type == "local":
            # Use output_directory if specified, otherwise derive from source directory
            directory = config.get("output_directory") or config.get("directory")
            if not directory:
                raise ValueError("Local destination requires 'directory' or 'output_directory' parameter")

            return LocalDataSaver(base_directory=directory)

        else:
            raise ValueError(f"Unknown destination type: {destination_type}")

    def process_all_files(self) -> List[Dict[str, Any]]:
        """
        Processes all files from source.

        Returns:
            List of processing results with metadata
        """
        results = []
        processed_count = 0
        error_count = 0

        logger.info("Gathering list of files from source...")

        # 1. Load ALL files into a list first so we know the total count
        all_files = self.get_file_list()
        total_files = len(all_files)

        logger.info(f"Found {total_files} files. Starting processing pipeline...")

        # 2. Loop through the list using tqdm for a progress bar
        for file_key in tqdm(all_files, desc="Converting Documents", unit="file"):
            try:
                result = self.process_single_file(file_key)
                results.append(result)

                if result["status"] == "success":
                    processed_count += 1
                else:
                    error_count += 1

            except Exception as e:
                # Use tqdm.write so logs don't break the progress bar visually
                tqdm.write(f"Error processing {file_key}: {e}")
                logger.error(f"Error processing {file_key}: {e}", exc_info=True)
                results.append({
                    "file_key": file_key,
                    "status": "error",
                    "error": str(e)
                })
                error_count += 1

        logger.info(
            f"Pipeline completed. Success: {processed_count}, Errors: {error_count}"
        )

        return results

    def process_single_file(self, file_key: str) -> Dict[str, Any]:
        """
        Processes a single file through the complete pipeline.

        Pipeline steps:
            1. Load raw data
            2. Select parser
            3. Parse to Markdown
            4. Save Markdown with metadata

        Args:
            file_key: File key/path to process

        Returns:
            Dict with processing results and metadata
        """
        logger.info(f"Processing file: {file_key}")

        try:
            # STEP 1: Load raw data
            logger.debug(f"Step 1: Loading raw data for {file_key}")
            raw_data = self.loader.load_raw_data(file_key)

            # STEP 2: Select parser
            logger.debug(f"Step 2: Selecting parser for {file_key}")
            parser = self.parser_selector.get_parser(file_key)

            # STEP 3: Parse to Markdown
            logger.debug(f"Step 3: Parsing {file_key} to Markdown")
            documents = self._parse_to_markdown(file_key, raw_data, parser)

            if not documents:
                logger.warning(f"No documents generated for {file_key}")
                return {
                    "file_key": file_key,
                    "status": "empty",
                    "error": "No documents generated after parsing"
                }

            # STEP 4: Save Markdown with metadata
            logger.debug(f"Step 4: Saving Markdown and building metadata for {file_key}")
            metadata = self._save_and_build_metadata(file_key, documents)

            logger.info(f"Successfully processed {file_key}: {len(documents)} documents")

            return {
                "file_key": file_key,
                "status": "success",
                "document_count": len(documents),
                "metadata": metadata,
                "documents": documents,
            }

        except Exception as e:
            logger.error(f"Failed to process {file_key}: {e}", exc_info=True)
            return {
                "file_key": file_key,
                "status": "error",
                "error": str(e)
            }

    def _parse_to_markdown(
            self,
            file_key: str,
            raw_data: bytes,
            parser
    ) -> List[Document]:
        """
        Step 3: Parse raw data to Markdown documents.

        Args:
            file_key: File key/path
            raw_data: Raw file bytes
            parser: Selected parser instance

        Returns:
            List of Document objects with Markdown content
        """
        ext = os.path.splitext(file_key)[1].lower()

        # Some parsers need BytesIO wrapper, others work with raw bytes
        if self.parser_selector.needs_bytes_io(file_key):
            data_source = io.BytesIO(raw_data)
        else:
            data_source = raw_data

        # Parse file
        documents = parser.parse(data_source, ext=ext)

        return documents

    def _save_and_build_metadata(
            self,
            file_key: str,
            documents: List[Document]
    ) -> Dict[str, Any]:
        """
        Step 4: Save Markdown and build complete metadata.

        Args:
            file_key: Source file key/path
            documents: Parsed documents

        Returns:
            Complete metadata dictionary
        """
        # Combine documents into single markdown string
        markdown_content = self.metadata_builder.combine_documents_to_markdown(documents)

        # Save markdown
        markdown_key = self.saver.save_markdown(file_key, markdown_content)
        markdown_url = self.saver.get_markdown_url(markdown_key)

        # Extract domain
        domain = self.loader.extract_domain(file_key)

        # Build source URL
        source_url = self._build_source_url(file_key)

        # Build complete metadata
        metadata = self.metadata_builder.build_file_metadata(
            file_key=file_key,
            domain=domain,
            source_url=source_url,
            storage_type=self.source_type,
            markdown_path=markdown_key,
            markdown_url=markdown_url,
        )

        # Enrich documents with metadata
        self.metadata_builder.enrich_documents(documents, metadata)

        return metadata

    def _build_source_url(self, file_key: str) -> str:
        """Builds source URL based on source type."""
        if self.source_type == "s3":
            bucket_name = self.loader.bucket_name
            return f"s3://{bucket_name}/{file_key}"
        else:
            return f"file://{file_key}"

    def get_file_list(self) -> List[str]:
        """
        Returns list of all files to process.

        Returns:
            List of file keys/paths
        """
        return list(self.loader.list_files())


# --- CLI ENTRY POINT ---
if __name__ == "__main__":
    # 1. Setup Argument Parser
    parser = argparse.ArgumentParser(
        description="Markdown Converter Pipeline: Convert S3 or Local documents to Markdown."
    )

    # Core Arguments
    parser.add_argument("--source-type", choices=["s3", "local"], required=True,
                        help="Where to load files from")
    parser.add_argument("--dest-type", choices=["s3", "local"],
                        help="Where to save markdown (defaults to source-type)")

    # S3 Arguments
    parser.add_argument("--bucket", dest="bucket_name", help="Source S3 bucket name")
    parser.add_argument("--prefix", default="", help="Source S3 folder prefix")
    parser.add_argument("--out-bucket", dest="output_bucket", help="Output S3 bucket name")

    # Local Arguments
    parser.add_argument("--dir", dest="directory", help="Source local directory path")
    parser.add_argument("--out-dir", dest="output_directory", help="Output local directory path")

    # Logging Argument
    parser.add_argument("--debug", action="store_true", help="Enable debug level logging")

    args = parser.parse_args()

    # 2. Setup Logging
    log_level = logging.DEBUG if args.debug else logging.INFO
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)]
    )

    # 3. Build Config Dictionary
    # We use vars(args) to convert the argparse namespace to a dictionary,
    # and filter out None values so the default logic in your class works perfectly.
    config = {k: v for k, v in vars(args).items() if v is not None}

    # Remove the core args from the config dict since they are passed explicitly
    config.pop("source_type", None)
    config.pop("dest_type", None)
    config.pop("debug", None)

    # 4. Initialize and Run the Converter
    try:
        converter = MarkDownConverter(
            source_type=args.source_type,
            destination_type=args.dest_type,
            **config
        )

        results = converter.process_all_files()

        # Optional: Print a brief summary at the very end
        successes = sum(1 for r in results if r.get("status") == "success")
        errors = sum(1 for r in results if r.get("status") == "error")
        print(f"\n--- DONE ---")
        print(f"Total processed: {len(results)} | Success: {successes} | Errors: {errors}")

        if errors > 0:
            sys.exit(1)

    except Exception as e:
        logger.error(f"Pipeline failed: {e}")
        sys.exit(1)