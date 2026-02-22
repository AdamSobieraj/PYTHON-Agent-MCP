import os
import boto3
import logging
from typing import Generator
from buissnes_agent.config_loader import settings

logger = logging.getLogger(__name__)

class DataLoaderS3Service:
    def __init__(self):
        self.aws_key = os.getenv('S3_AKID') or os.getenv('AWS_ACCESS_KEY_ID')
        self.aws_secret = os.getenv('S3_SK') or os.getenv('AWS_SECRET_ACCESS_KEY')
        self.aws_region = os.getenv('AWS_REGION') or os.getenv('S3_REGION') or "eu-north-1"
        self.s3_endpoint = os.getenv('S3_ENDPOINT')

        if not self.aws_key or not self.aws_secret:
            raise RuntimeError("Brak poświadczeń AWS w pliku .env")

        self.session = boto3.Session(
            aws_access_key_id=self.aws_key,
            aws_secret_access_key=self.aws_secret,
            region_name=self.aws_region,
        )

        if self.s3_endpoint:
            self.s3_client = self.session.client('s3', endpoint_url=self.s3_endpoint)
        else:
            self.s3_client = self.session.client('s3')

    def list_objects(self, bucket_name: str, prefix: str = "") -> Generator[str, None, None]:
        """
        Zwraca klucze plików tylko z podanego prefixu (folderu).
        """
        paginator = self.s3_client.get_paginator('list_objects_v2')

        # Jeśli prefix jest pusty, to pusty string.
        prefix_arg = prefix if prefix else ""

        # Pobieramy dozwolone rozszerzenia z settings, lub ustawiamy domyślne jeśli brak
        allowed_exts = settings.get("chunking.allowed_extensions", [])
        if not allowed_exts:
            # Dodałem .xsd bo widziałem je w Twoich logach
            allowed_exts = ['.txt', '.md', '.pdf', '.docx', '.xlsx', '.xsd', '.xml', '.json']

        ext_tuple = tuple(allowed_exts)

        # Kluczowy moment: parametr Prefix filtruje pliki po stronie AWS
        # Dzięki temu nie pobieramy listy całego bucketa.
        try:
            for page in paginator.paginate(Bucket=bucket_name, Prefix=prefix_arg):
                if 'Contents' in page:
                    for obj in page['Contents']:
                        key = obj['Key']

                        # Ignorujemy sam folder (jeśli AWS zwraca go jako obiekt)
                        if key.endswith('/'):
                            continue

                        # Filtrowanie po rozszerzeniach
                        if key.lower().endswith(ext_tuple):
                            yield key
        except Exception as e:
            logger.error(f"S3Service Error listing objects: {e}")
            raise e

    def download_text(self, bucket_name: str, object_key: str) -> str:
        try:
            response = self.s3_client.get_object(Bucket=bucket_name, Key=object_key)
            data = response["Body"].read()
            try:
                return data.decode("utf-8")
            except UnicodeDecodeError:
                return data.decode("windows-1252")
        except Exception as e:
            logger.error(f"S3Service Error downloading {object_key}: {e}")
            raise e

    def download_bytes(self, bucket_name: str, key: str) -> bytes:
        try:
            response = self.s3_client.get_object(Bucket=bucket_name, Key=key)
            return response['Body'].read()
        except Exception as e:
            logger.error(f"S3 Download Error (Bytes): {e}")
            raise e