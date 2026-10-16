"""
Qdrant maintenance: list all collections.

Reads QDRANT_API / QDRANT_API_KEY from .env (or --url/--api-key overrides).

Usage:
    python -m buissnes_agent.manual_metrics.maintain_list_collections
    python -m buissnes_agent.manual_metrics.maintain_list_collections --json
    python -m buissnes_agent.manual_metrics.maintain_list_collections --url http://localhost:6333
"""
import argparse
import json
import os
import sys
from typing import Any, Dict, List, Optional

from dotenv import load_dotenv


def list_collections(
        url: str,
        api_key: Optional[str] = None,
        timeout: int = 10,
) -> List[Dict[str, Any]]:
    """Return a list of dicts: name, status, points_count, vector_size."""
    from qdrant_client import QdrantClient

    client = QdrantClient(
        url=url,
        api_key=api_key or None,
        timeout=timeout,
    )
    result: List[Dict[str, Any]] = []
    resp = client.get_collections()
    # newer qdrant-client wraps the list in a response object;
    # the lightweight listing only carries the collection names
    infos = getattr(resp, "collections", None) or resp
    for info in infos:
        name = getattr(info, "name", str(info))
        status = points = vector_size = None
        try:
            details = client.get_collection(name)
            status = getattr(getattr(details, "status", None), "value",
                             getattr(details, "status", None))
            vectors = details.config.params.vectors
            # vectors config is either a VectorParams (dense) or a dict
            vector_size = getattr(vectors, "size", None)
        except Exception:
            pass
        try:
            points = client.count(name, exact=True).count
        except Exception:
            pass
        result.append({
            "name": name,
            "status": str(status) if status is not None else "",
            "points_count": points,
            "vector_size": vector_size,
        })
    return result


def main(argv: Optional[List[str]] = None) -> int:
    load_dotenv()

    parser = argparse.ArgumentParser(
        description="List all Qdrant collections (name, status, points, dim)"
    )
    parser.add_argument(
        "--url",
        default=os.getenv("QDRANT_API", "http://localhost:6333"),
        help="Qdrant URL (default: QDRANT_API from .env or http://localhost:6333)"
    )
    parser.add_argument(
        "--api-key",
        default=os.getenv("QDRANT_API_KEY") or None,
        help="Qdrant API key (default: QDRANT_API_KEY from .env)"
    )
    parser.add_argument(
        "--json", action="store_true",
        help="print the result as JSON"
    )
    args = parser.parse_args(argv)

    try:
        collections = list_collections(args.url, api_key=args.api_key)
    except Exception as e:
        print(f"ERROR: cannot reach Qdrant at {args.url}: {e}")
        return 1

    if args.json:
        print(json.dumps(collections, indent=2, ensure_ascii=False))
        return 0

    if not collections:
        print(f"No collections in {args.url}")
        return 0

    collections.sort(key=lambda c: c["name"])
    width = max(len(c["name"]) for c in collections)
    print(f"Qdrant: {args.url} | {len(collections)} collections\n")
    print(f"{'NAME'.ljust(width)}  {'STATUS':<12}  {'POINTS':>8}  {'DIM':>6}")
    print("-" * (width + 36))
    for c in collections:
        dim = c["vector_size"] if c["vector_size"] is not None else "?"
        print(
            f"{c['name']:<{width}}  "
            f"{str(c['status']):<12}  "
            f"{str(c['points_count']):>8}  "
            f"{str(dim):>6}"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
