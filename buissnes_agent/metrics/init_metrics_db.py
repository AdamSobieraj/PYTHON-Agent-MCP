import sys
import logging
from dotenv import load_dotenv

from metrics import get_repository

logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] %(message)s',
    stream=sys.stderr
)

logger = logging.getLogger(__name__)
load_dotenv()


def main():
    """Inicjalizacja bazy danych metryk (niezależnie od typu!)"""

    print("=" * 70)
    print("         INICJALIZACJA BAZY DANYCH METRYK RAG")
    print("=" * 70)

    try:
        # Factory automatycznie wybierze typ z ENV
        repository = get_repository()

        print(f"\n[INFO] Typ storage: {repository.__class__.__name__}")

        # Krok 1: Test połączenia
        print("\n[1/2] Testowanie połączenia...")
        if not repository.test_connection():
            print("\n[ERROR] Nie można połączyć się z storage.")
            print("Sprawdź konfigurację w .env")
            sys.exit(1)

        print("[OK] Połączenie działa")

        # Krok 2: Inicjalizacja schematu
        print("\n[2/2] Inicjalizacja schematu...")
        if not repository.initialize_schema():
            print("\n[ERROR] Nie można zainicjalizować schematu.")
            sys.exit(1)

        print("[OK] Schemat zainicjalizowany")

        # Podsumowanie
        print("\n" + "=" * 70)
        print("         INICJALIZACJA ZAKOŃCZONA POMYŚLNIE")
        print("=" * 70)
        print("\nMożesz teraz uruchomić:")
        print("  python MCPServer.py")
        print("\nAnaliza metryk:")
        print("  python test_view_metrics_analyzer.py")
        print("=" * 70)

    except Exception as e:
        print(f"\n[ERROR] Błąd inicjalizacji: {e}", file=sys.stderr)
        sys.exit(1)
    finally:
        # Cleanup
        try:
            repository.close()
        except:
            pass


if __name__ == "__main__":
    main()