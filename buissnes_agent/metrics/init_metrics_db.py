import logging
import sys

from dotenv import load_dotenv

from buissnes_agent.metrics import get_repository


logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(message)s",
    stream=sys.stderr,
)

logger = logging.getLogger(__name__)
load_dotenv()


def main():
    """Initialize the RAG metrics storage."""

    print("=" * 70)
    print("         INICJALIZACJA BAZY DANYCH METRYK RAG")
    print("=" * 70)

    repository = None
    try:
        repository = get_repository()

        print(f"\n[INFO] Typ storage: {repository.__class__.__name__}")

        print("\n[1/2] Testowanie polaczenia...")
        if not repository.test_connection():
            print("\n[ERROR] Nie mozna polaczyc sie z storage.")
            print("Sprawdz konfiguracje w .env")
            sys.exit(1)

        print("[OK] Polaczenie dziala")

        print("\n[2/2] Inicjalizacja schematu...")
        if not repository.initialize_schema():
            print("\n[ERROR] Nie mozna zainicjalizowac schematu.")
            sys.exit(1)

        print("[OK] Schemat zainicjalizowany")

        print("\n" + "=" * 70)
        print("         INICJALIZACJA ZAKONCZONA POMYSLNIE")
        print("=" * 70)
        print("\nMozesz teraz uruchomic:")
        print("  python -m buissnes_agent.mcp_server")
        print("  # albo kompatybilnie: python buissnes_agent/MCPServer.py")
        print("\nAnaliza metryk:")
        print("  python test_view_metrics_analyzer.py")
        print("=" * 70)

    except Exception as exc:
        print(f"\n[ERROR] Blad inicjalizacji: {exc}", file=sys.stderr)
        sys.exit(1)
    finally:
        if repository is not None:
            try:
                repository.close()
            except Exception:
                pass


if __name__ == "__main__":
    main()
