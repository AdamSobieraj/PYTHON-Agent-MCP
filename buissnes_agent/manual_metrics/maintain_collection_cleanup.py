"""
Qdrant maintenance: delete all experiment collections (prefix "exp_").

Experiment runs (manual_metrics.run_experiments / thesis_pipeline) create
one collection per run (exp_<experiment_id>), so they accumulate.
This script removes all collections whose name starts with the given
prefix (default: "exp_").

Safety: nothing is deleted until you confirm. Use --dry-run to only
list, or --yes to skip the interactive confirmation.

Usage:
    python -m buissnes_agent.manual_metrics.maintain_collection_cleanup
    python -m buissnes_agent.manual_metrics.maintain_collection_cleanup --dry-run
    python -m buissnes_agent.manual_metrics.maintain_collection_cleanup --yes
    python -m buissnes_agent.manual_metrics.maintain_collection_cleanup --prefix exp_E3_
"""
import argparse
import os
import sys
from typing import List, Optional

from dotenv import load_dotenv


def _client_factory(url: str, api_key: Optional[str]):
    from qdrant_client import QdrantClient

    return QdrantClient(url=url, api_key=api_key or None, timeout=10)


def main(argv: Optional[List[str]] = None) -> int:
    load_dotenv()

    parser = argparse.ArgumentParser(
        description="Delete Qdrant collections with a name prefix "
                    "(default: exp_ - experiment runs)"
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
        "--prefix", default="exp_",
        help="collection name prefix to delete (default: exp_)"
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="only list the collections that would be deleted"
    )
    parser.add_argument(
        "--yes", action="store_true",
        help="skip the interactive confirmation (delete immediately)"
    )
    args = parser.parse_args(argv)

    try:
        client = _client_factory(args.url, args.api_key)
        resp = client.get_collections()
        infos = getattr(resp, "collections", None) or resp
        all_names = sorted(
            getattr(i, "name", str(i)) for i in infos
        )
    except Exception as e:
        print(f"ERROR: cannot reach Qdrant at {args.url}: {e}")
        return 1

    targets = [n for n in all_names if n.startswith(args.prefix)]
    print(f"Qdrant: {args.url}")
    print(f"Collections with prefix '{args.prefix}': {len(targets)} "
          f"(of {len(all_names)} total)")

    if not targets:
        print("Nothing to delete.")
        return 0

    for name in targets:
        print(f"  - {name}")

    if args.dry_run:
        print("\nDRY RUN - no collections deleted.")
        return 0

    if not args.yes:
        answer = input(
            f"\nDelete these {len(targets)} collections? "
            f"Type 'yes' to confirm: "
        ).strip().lower()
        if answer != "yes":
            print("Aborted - nothing deleted.")
            return 1

    errors: List[str] = []
    for name in targets:
        try:
            client.delete_collection(name)
            print(f"DELETED: {name}")
        except Exception as e:
            errors.append(f"{name}: {e}")
            print(f"FAILED: {name} ({e})")

    if errors:
        print(f"\n{len(errors)} collection(s) could not be deleted.")
        return 1

    print(f"\nDONE. {len(targets)} collections deleted.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
