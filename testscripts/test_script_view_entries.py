import os
import sys
import logging
import json  # <--- Dodano do pretty-printingu JSONa

from dotenv import load_dotenv
from buissnes_agent.config_loader import get_settings

# Upewnij się, że ten import pasuje do struktury Twojego projektu
from buissnes_agent.QdrantDatabaseStore import QdrantDatabaseStore

# Konfiguracja logowania
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger("DB-Viewer")

# Ładowanie zmiennych środowiskowych
load_dotenv()
settings = get_settings()

def view_entries(limit: int = 5):
    """
    Pobiera i wyświetla N ostatnich wpisów z kolekcji Qdrant.
    Wyświetla PEŁNY PAYLOAD (wszystkie metadane) w formacie JSON.
    """

    # 1. Pobieranie konfiguracji z .env
    qdrant_url = os.getenv("QDRANT_API")
    qdrant_key = os.getenv("QDRANT_API_KEY")
    collection_name = settings.get("vector_db.collection_name")
    # collection_name = "my_custom_collection_v2"

    if not qdrant_url:
        logger.error("Brak QDRANT_API w pliku .env")
        return

    # 2. Inicjalizacja Twojej klasy Store
    vector_size = 1536
    try:
        store = QdrantDatabaseStore(
            url=qdrant_url,
            api_key=qdrant_key,
            collection_name=collection_name,
            vector_size=vector_size
        )
    except Exception as e:
        logger.error(f"Nie udało się połączyć z Qdrant: {e}")
        return

    print(f"\n--- PRZEGLĄDANIE KOLEKCJI: {collection_name} ---")
    try:
        count = store.count()
        print(f"Ilość dokumentów w bazie: {count}")
    except Exception:
        print("Nie udało się pobrać licznika dokumentów.")

    print(f"Pobieranie {limit} wpisów...\n")

    try:
        # 3. Użycie metody SCROLL z klienta Qdrant
        records, next_page_offset = store.client.scroll(
            collection_name=collection_name,
            limit=limit,
            with_payload=True,
            with_vectors=False
        )

        if not records:
            print("Brak wpisów w bazie.")
            return

        # 4. Wyświetlanie wyników
        for i, record in enumerate(records, 1):
            payload = record.payload

            print(f"[{i}] Qdrant UUID: {record.id}")
            print("PEŁNE DANE (PAYLOAD):")

            # json.dumps sformatuje słownik payloadu w czytelną strukturę
            # ensure_ascii=False pozwala wyświetlać polskie znaki
            print(json.dumps(payload, indent=4, ensure_ascii=False))

            print("-" * 80)

    except Exception as e:
        logger.error(f"Błąd podczas pobierania danych: {e}")

    # 5. Podsumowanie bazy (rozmiar i liczba chunków)
    print_db_summary(store, collection_name, vector_size)


def print_db_summary(store, collection_name: str, vector_size: int):
    """
    Wyświetla podsumowanie bazy danych:
    - liczbę chunków (punktów),
    - rozmiar bazy w bajtach (payload + wektory) oraz rozmiar w formie czytelnej.
    """
    print(f"\n{'=' * 80}")
    print(f"PODSUMOWANIE BAZY DANYCH: {collection_name}")
    print(f"{'=' * 80}")

    def human(n: float) -> str:
        for unit in ['B', 'KB', 'MB', 'GB', 'TB', 'PB']:
            if n < 1024.0 or unit == 'PB':
                return f"{int(n)} B" if unit == 'B' else f"{n:,.2f} {unit}"
            n /= 1024.0

    try:
        # Liczba chunków (punktów) w kolekcji
        points_count = store.count()

        if points_count == 0:
            print("Liczba chunków:      0")
            print("Rozmiar bazy:        0 B (baza pusta)")
            print(f"{'=' * 80}")
            return

        # Rozmiar payloadów — przeliczamy, przeskanowując wszystkie wpisy
        payload_bytes = 0
        offset = None
        page_size = 1000
        while True:
            records, offset = store.client.scroll(
                collection_name=collection_name,
                limit=page_size,
                offset=offset,
                with_payload=True,
                with_vectors=False
            )
            for record in records:
                payload_bytes += len(json.dumps(record.payload, ensure_ascii=False).encode('utf-8'))
            if offset is None:
                break

        # Rozmiar wektorów — znany: liczba punktów * wymiar * 4 bajty (float32)
        vector_bytes = points_count * vector_size * 4
        total_bytes = payload_bytes + vector_bytes

        print(f"Liczba chunków:        {points_count:,}")
        print(f"Rozmiar payloadów:     {human(payload_bytes)} ({payload_bytes:,} B)")
        print(f"Rozmiar wektorów:      {human(vector_bytes)} ({vector_bytes:,} B)")
        print(f"ŁĄCZNY ROZMIAR BAZY:   {human(total_bytes)} ({total_bytes:,} B)")
        print(f"{'=' * 80}")

    except Exception as e:
        logger.error(f"Błąd podczas generowania podsumowania bazy: {e}")


if __name__ == "__main__":
    # Obsługa argumentu z linii poleceń
    qty = 1000
    if len(sys.argv) > 3:
        try:
            qty = int(sys.argv[1])
        except ValueError:
            print("Podaj poprawną liczbę całkowitą.")
            sys.exit(1)

    view_entries(qty)