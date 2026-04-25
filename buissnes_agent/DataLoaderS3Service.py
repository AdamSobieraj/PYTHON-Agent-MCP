import logging
import os
from dataclasses import dataclass
from typing import Generator

import boto3
from dotenv import load_dotenv

from buissnes_agent.config_loader import settings

logger = logging.getLogger(__name__)

load_dotenv()


@dataclass(frozen=True, slots=True)
class S3TextObject:
    text: str
    content_length: int | None = None
    content_range: str | None = None
    etag: str | None = None


class DataLoaderS3Service:
    def __init__(self):
        self.aws_key = os.getenv('S3_AKID') or os.getenv('AWS_ACCESS_KEY_ID')
        self.aws_secret = os.getenv('S3_SK') or os.getenv('AWS_SECRET_ACCESS_KEY')
        self.aws_region = os.getenv('AWS_REGION') or os.getenv('S3_REGION') or "eu-north-1"
        self.s3_endpoint = os.getenv('S3_ENDPOINT')
        self.s3_verify = self._resolve_s3_verify()

        if not self.aws_key or not self.aws_secret:
            raise RuntimeError("Brak poświadczeń AWS w pliku .env")

        self.session = boto3.Session(
            aws_access_key_id=self.aws_key,
            aws_secret_access_key=self.aws_secret,
            region_name=self.aws_region,
        )

        client_kwargs: dict[str, object] = {'verify': self.s3_verify}
        if self.s3_endpoint:
            client_kwargs['endpoint_url'] = self.s3_endpoint

        self.s3_client = self.session.client('s3', **client_kwargs)

    @staticmethod
    def _resolve_s3_verify() -> bool | str:
        explicit_bundle = os.getenv('S3_CA_BUNDLE') or os.getenv('AWS_CA_BUNDLE')
        if explicit_bundle:
            return explicit_bundle

        return True

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

    def _decode_text(self, data: bytes, *, allow_replacement: bool = False) -> str:
        try:
            return data.decode("utf-8")
        except UnicodeDecodeError:
            if allow_replacement:
                return data.decode("utf-8", errors="replace")

            return data.decode("windows-1252")
    @staticmethod
    def _normalize_etag(etag: str | None) -> str | None:
        if not etag:
            return None
        return etag.strip('"')

    def download_text_response(
        self,
        bucket_name: str,
        object_key: str,
    ) -> S3TextObject:
        try:
            response = self.s3_client.get_object(Bucket=bucket_name, Key=object_key)
            data = response["Body"].read()
            return S3TextObject(
                text=self._decode_text(data),
                content_length=response.get("ContentLength"),
                etag=self._normalize_etag(response.get("ETag")),
            )
        except Exception as e:
            logger.error(f"S3Service Error downloading {object_key}: {e}")
            raise e

    def download_text(self, bucket_name: str, object_key: str) -> str:
        return self.download_text_response(bucket_name, object_key).text

    def download_text_range(
        self,
        bucket_name: str,
        object_key: str,
        start_byte: int,
        end_byte: int | None = None,
    ) -> S3TextObject:
        if start_byte < 0:
            raise ValueError("start_byte must be zero or greater.")
        if end_byte is not None and end_byte < start_byte:
            raise ValueError("end_byte must be greater than or equal to start_byte.")

        range_header = (
            f"bytes={start_byte}-"
            if end_byte is None
            else f"bytes={start_byte}-{end_byte}"
        )

        try:
            response = self.s3_client.get_object(
                Bucket=bucket_name,
                Key=object_key,
                Range=range_header,
            )
            data = response["Body"].read()
            return S3TextObject(
                text=self._decode_text(data, allow_replacement=True),
                content_length=response.get("ContentLength"),
                content_range=response.get("ContentRange"),
                etag=self._normalize_etag(response.get("ETag")),
            )
        except Exception as e:
            logger.error(
                "S3Service Error downloading %s with range %s: %s",
                object_key,
                range_header,
                e,
            )
            raise e

    def download_bytes(self, bucket_name: str, key: str) -> bytes:
        try:
            response = self.s3_client.get_object(Bucket=bucket_name, Key=key)
            return response['Body'].read()
        except Exception as e:
            logger.error(f"S3 Download Error (Bytes): {e}")
            raise e
