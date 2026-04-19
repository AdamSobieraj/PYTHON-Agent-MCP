from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol
from urllib.parse import urlparse

from buissnes_agent.DataLoaderS3Service import DataLoaderS3Service, S3TextObject


@dataclass(frozen=True, slots=True)
class ResolvedS3Object:
    bucket_name: str
    object_key: str


class S3DocumentService(Protocol):
    def download_text(self, bucket_name: str, object_key: str) -> str: ...

    def download_text_response(
        self,
        bucket_name: str,
        object_key: str,
    ) -> S3TextObject: ...

    def download_text_range(
        self,
        bucket_name: str,
        object_key: str,
        start_byte: int,
        end_byte: int | None = None,
    ) -> S3TextObject: ...


def _build_s3_service() -> DataLoaderS3Service:
    return DataLoaderS3Service()


def parse_s3_uri(s3_uri: str) -> ResolvedS3Object:
    normalized_uri = s3_uri.strip()
    if not normalized_uri:
        raise ValueError("s3_uri must be a non-empty string.")

    parsed = urlparse(normalized_uri)
    if parsed.scheme.lower() != "s3":
        raise ValueError("s3_uri must use the s3:// scheme.")
    if not parsed.netloc:
        raise ValueError("s3_uri must include a bucket name.")

    object_key = parsed.path.lstrip("/")
    if not object_key:
        raise ValueError("s3_uri must include an object key.")

    return ResolvedS3Object(
        bucket_name=parsed.netloc,
        object_key=object_key,
    )


def _format_document_result(
    *,
    resolved_object: ResolvedS3Object,
    text_object: S3TextObject,
    requested_range: str | None = None,
) -> str:
    lines = [
        f"Source (file): s3://{resolved_object.bucket_name}/{resolved_object.object_key}",
        f"Bucket: {resolved_object.bucket_name}",
        f"Object key: {resolved_object.object_key}",
    ]

    if requested_range:
        lines.append(f"Requested range: {requested_range}")
    if text_object.content_range:
        lines.append(f"S3 content range: {text_object.content_range}")
    if text_object.content_length is not None:
        lines.append(f"Returned bytes: {text_object.content_length}")
    if text_object.etag:
        lines.append(f"ETag: {text_object.etag}")

    lines.append("Content:")
    lines.append(text_object.text.rstrip())
    return "\n".join(lines)


def fetch_markdown_document(
    *,
    s3_uri: str,
    s3_service: S3DocumentService | None = None,
) -> str:
    resolved_object = parse_s3_uri(s3_uri)
    service = s3_service or _build_s3_service()
    text_object = service.download_text_response(
        resolved_object.bucket_name,
        resolved_object.object_key,
    )
    return _format_document_result(
        resolved_object=resolved_object,
        text_object=text_object,
    )


def fetch_markdown_document_range(
    *,
    start_byte: int,
    end_byte: int | None = None,
    s3_uri: str,
    s3_service: S3DocumentService | None = None,
) -> str:
    if start_byte < 0:
        raise ValueError("start_byte must be zero or greater.")
    if end_byte is not None and end_byte < start_byte:
        raise ValueError("end_byte must be greater than or equal to start_byte.")

    resolved_object = parse_s3_uri(s3_uri)
    service = s3_service or _build_s3_service()
    text_object = service.download_text_range(
        resolved_object.bucket_name,
        resolved_object.object_key,
        start_byte,
        end_byte,
    )

    requested_range = (
        f"bytes={start_byte}-"
        if end_byte is None
        else f"bytes={start_byte}-{end_byte}"
    )
    return _format_document_result(
        resolved_object=resolved_object,
        text_object=text_object,
        requested_range=requested_range,
    )
