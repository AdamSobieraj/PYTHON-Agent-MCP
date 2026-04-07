# init_metrics_db.py

import sys
import logging
from metrics_db import initialize_schema, test_connection, db_pool

logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] %(message)s',
    stream=sys.stderr
)

logger = logging.getLogger(__name__)


def main():
    """Inicjalizacja bazy danych metryk"""

    print("=" * 70)
    print("         INICJALIZACJA BAZY DANYCH METRYK RAG")
    print("=" * 70)

    # Krok 1: Test połączenia
    print("\n[1/2] Testowanie połączenia z PostgreSQL...")
    if not test_connection():
        print("\n[ERROR] Nie można połączyć się z bazą danych.")
        print("Sprawdź konfigurację w .env:")
        print("  - METRICS_DB_HOST")
        print("  - METRICS_DB_PORT")
        print("  - METRICS_DB_NAME")
        print("  - METRICS_DB_USER")
        print("  - METRICS_DB_PASSWORD")
        sys.exit(1)

    print("[OK] Połączenie z bazą działa")

    # Krok 2: Tworzenie schematu
    print("\n[2/2] Tworzenie tabel...")
    if not initialize_schema():
        print("\n[ERROR] Nie można utworzyć schematu bazy danych.")
        sys.exit(1)

    print("[OK] Tabele utworzone")

    # Podsumowanie
    print("\n" + "=" * 70)
    print("         INICJALIZACJA ZAKOŃCZONA POMYŚLNIE")
    print("=" * 70)
    print("\nUtworzono tabele:")
    print("  - rag_retrieval_metrics")
    print("  - rag_generation_metrics")
    print("  - rag_full_metrics")
    print("\nMożesz teraz uruchomić serwer:")
    print("  python MCPServer.py")
    print("\nAnaliza metryk:")
    print("  python metrics_analyzer.py")
    print("=" * 70)

    # Cleanup
    db_pool.close_all()


if __name__ == "__main__":
    main()