import sys
import logging
from datetime import datetime, timedelta
from typing import Optional, Dict, Any, List
from dotenv import load_dotenv

from metrics import get_repository, IMetricsRepository, MetricsStats

logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] %(message)s',
    stream=sys.stderr
)

logger = logging.getLogger(__name__)
load_dotenv()


# ==============================================================================
# FORMATOWANIE I WYŚWIETLANIE
# ==============================================================================

def print_separator(width: int = 70):
    """Drukuj separator"""
    print("=" * width)


def print_section_header(title: str, width: int = 70):
    """Drukuj nagłówek sekcji"""
    print("\n" + title)
    print("-" * width)


# ==============================================================================
# DASHBOARD - GŁÓWNA ANALIZA
# ==============================================================================

def print_dashboard(
        repository: IMetricsRepository,
        hours: Optional[int] = None,
        collection_name: Optional[str] = None,
        limit: int = 1000
):
    """
    Wyświetl dashboard metryk RAG (niezależnie od typu bazy!)

    Args:
        repository: Instancja IMetricsRepository
        hours: Zakres czasowy (None = wszystkie dane)
        collection_name: Filtruj po kolekcji
        limit: Max rekordów do analizy
    """

    # Pobierz dane przez interfejs
    try:
        stats = repository.get_aggregated_stats(
            hours=hours or 24,
            collection_name=collection_name
        )

        raw_metrics = repository.get_retrieval_metrics(
            limit=limit,
            collection_name=collection_name,
            hours=hours
        )

    except Exception as e:
        print_separator()
        print(f"BŁĄD POBIERANIA DANYCH: {e}")
        print_separator()
        logger.error(f"Error loading metrics: {e}")
        return

    # Sprawdź czy są dane
    if stats.total_queries == 0:
        print_separator()
        print("BRAK DANYCH DO WYŚWIETLENIA")
        if hours:
            print(f"(w ciągu ostatnich {hours} godzin)")
        if collection_name:
            print(f"(dla kolekcji: {collection_name})")
        print_separator()
        return

    # ===== NAGŁÓWEK =====
    print_separator()
    print("         RAG RETRIEVAL PERFORMANCE DASHBOARD")
    print(f"         Storage: {repository.__class__.__name__}")
    print_separator()

    # ===== OGÓLNE STATYSTYKI =====
    print_section_header("OGÓLNE STATYSTYKI")
    print(f"   Total Queries:        {stats.total_queries}")

    no_results_pct = (
        (stats.queries_no_results / stats.total_queries * 100)
        if stats.total_queries > 0 else 0
    )
    print(f"   Queries bez wyników:  {stats.queries_no_results} ({no_results_pct:.1f}%)")

    if hours:
        print(f"   Zakres czasowy:       ostatnie {hours}h")
    if collection_name:
        print(f"   Kolekcja:             {collection_name}")

    # ===== LATENCY =====
    print_section_header("LATENCY")
    print(f"   Average:   {stats.avg_latency_ms:.0f} ms")
    print(f"   P50:       {stats.p50_latency_ms:.0f} ms")
    print(f"   P95:       {stats.p95_latency_ms:.0f} ms")
    print(f"   P99:       {stats.p99_latency_ms:.0f} ms")

    # ===== QUALITY =====
    print_section_header("QUALITY")
    print(f"   Avg Top Score:     {stats.avg_score:.3f}")
    print(f"   Avg Results/Query: {stats.avg_results:.1f}")

    # ===== PER COLLECTION (jeśli dostępne) =====
    if stats.per_collection and not collection_name:
        print_section_header("PER COLLECTION")
        _print_collection_stats(stats.per_collection)

    # ===== ALERTS =====
    print_section_header("ALERTS")
    alerts = _generate_alerts(stats, raw_metrics)

    if alerts:
        for alert in alerts:
            print(alert)
    else:
        print("   [OK] No critical issues detected")

    # ===== TOP SLOWEST QUERIES =====
    if raw_metrics:
        print_section_header("TOP 5 SLOWEST QUERIES")
        _print_slowest_queries(raw_metrics)

    print_separator()


def _print_collection_stats(per_collection: Dict[str, Any]):
    """Wydrukuj statystyki per collection"""
    # Format zależy od tego jak repository zwraca dane
    # Dla Postgres: zagnieżdżony dict
    # Dla File: może być inaczej

    if not per_collection:
        print("   Brak danych")
        return

    for collection, metrics in per_collection.items():
        if isinstance(metrics, dict):
            count = metrics.get('count', 0)
            latency = metrics.get('latency_ms', {}).get('mean', 0)
            score = metrics.get('avg_score', {}).get('mean', 0)

            print(f"   {collection}:")
            print(f"      Queries: {int(count)}, "
                  f"Latency: {latency:.0f}ms, "
                  f"Avg Score: {score:.3f}")


def _generate_alerts(stats: MetricsStats, raw_metrics: List[Dict]) -> List[str]:
    """Generuj alerty na podstawie metryk"""
    alerts = []

    # Alert 1: Wolne zapytania
    slow_queries = [m for m in raw_metrics if m.get('latency_ms', 0) > 2000]
    if slow_queries:
        alerts.append(
            f"   [WARNING] {len(slow_queries)} slow queries (>2000ms)"
        )

    # Alert 2: Niska jakość wyników
    low_quality = [m for m in raw_metrics if m.get('avg_score', 1) < 0.5]
    if low_quality:
        alerts.append(
            f"   [WARNING] {len(low_quality)} low quality queries (score <0.5)"
        )

    # Alert 3: Brak wyników
    if stats.queries_no_results > 0:
        alerts.append(
            f"   [INFO] {stats.queries_no_results} queries returned no results"
        )

    # Alert 4: Bardzo wysoki P99
    if stats.p99_latency_ms > 5000:
        alerts.append(
            f"   [WARNING] Very high P99 latency ({stats.p99_latency_ms:.0f}ms)"
        )

    # Alert 5: Niska średnia score
    if stats.avg_score < 0.6:
        alerts.append(
            f"   [WARNING] Low average score ({stats.avg_score:.3f})"
        )

    return alerts


def _print_slowest_queries(raw_metrics: List[Dict], top_n: int = 5):
    """Wydrukuj N najwolniejszych zapytań"""
    # Sortuj po latency
    sorted_metrics = sorted(
        raw_metrics,
        key=lambda x: x.get('latency_ms', 0),
        reverse=True
    )

    for i, metric in enumerate(sorted_metrics[:top_n], 1):
        query = metric.get('query', 'Unknown')
        latency = metric.get('latency_ms', 0)
        collection = metric.get('collection_name', 'Unknown')

        query_preview = query[:60] + "..." if len(query) > 60 else query
        print(f"   {i}. {latency:.0f}ms - {query_preview} [{collection}]")


# ==============================================================================
# EKSPORT DO CSV/JSON
# ==============================================================================

def export_to_csv(
        repository: IMetricsRepository,
        output_file: str,
        hours: Optional[int] = None,
        collection_name: Optional[str] = None,
        limit: int = 10000
):
    """
    Eksportuj metryki do CSV

    Args:
        repository: Instancja repository
        output_file: Ścieżka do pliku wyjściowego
        hours: Filtruj po czasie
        collection_name: Filtruj po kolekcji
        limit: Max rekordów
    """
    try:
        import pandas as pd
    except ImportError:
        print("[ERROR] Pandas nie jest zainstalowany. Użyj: pip install pandas")
        return False

    try:
        raw_metrics = repository.get_retrieval_metrics(
            limit=limit,
            collection_name=collection_name,
            hours=hours
        )

        if not raw_metrics:
            print("[WARNING] Brak danych do eksportu")
            return False

        df = pd.DataFrame(raw_metrics)
        df.to_csv(output_file, index=False)

        print(f"[OK] Wyeksportowano {len(raw_metrics)} rekordów do {output_file}")
        return True

    except Exception as e:
        print(f"[ERROR] Błąd eksportu: {e}")
        logger.error(f"Export error: {e}")
        return False


def export_to_json(
        repository: IMetricsRepository,
        output_file: str,
        hours: Optional[int] = None,
        collection_name: Optional[str] = None,
        limit: int = 10000
):
    """Eksportuj metryki do JSON"""
    import json

    try:
        raw_metrics = repository.get_retrieval_metrics(
            limit=limit,
            collection_name=collection_name,
            hours=hours
        )

        if not raw_metrics:
            print("[WARNING] Brak danych do eksportu")
            return False

        # Konwersja datetime do string
        for metric in raw_metrics:
            if 'timestamp' in metric and isinstance(metric['timestamp'], datetime):
                metric['timestamp'] = metric['timestamp'].isoformat()

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(raw_metrics, f, indent=2, ensure_ascii=False)

        print(f"[OK] Wyeksportowano {len(raw_metrics)} rekordów do {output_file}")
        return True

    except Exception as e:
        print(f"[ERROR] Błąd eksportu: {e}")
        logger.error(f"Export error: {e}")
        return False


# ==============================================================================
# INTERACTIVE MODE
# ==============================================================================

def interactive_mode(repository: IMetricsRepository):
    """Interaktywny tryb analizy"""
    print("\n" + "=" * 70)
    print("         INTERACTIVE METRICS ANALYZER")
    print("=" * 70)

    while True:
        print("\nOpcje:")
        print("  1. Pokaż dashboard (ostatnie 24h)")
        print("  2. Pokaż dashboard (custom zakres)")
        print("  3. Filtruj po kolekcji")
        print("  4. Eksportuj do CSV")
        print("  5. Eksportuj do JSON")
        print("  6. Statystyki (raw)")
        print("  0. Wyjście")

        choice = input("\nWybierz opcję: ").strip()

        if choice == "0":
            print("Do widzenia!")
            break

        elif choice == "1":
            print_dashboard(repository, hours=24)

        elif choice == "2":
            hours_input = input("Podaj liczbę godzin (lub ENTER dla wszystkich): ").strip()
            hours = int(hours_input) if hours_input else None
            print_dashboard(repository, hours=hours)

        elif choice == "3":
            collection = input("Podaj nazwę kolekcji: ").strip()
            hours_input = input("Podaj liczbę godzin (lub ENTER dla 24h): ").strip()
            hours = int(hours_input) if hours_input else 24
            print_dashboard(repository, hours=hours, collection_name=collection)

        elif choice == "4":
            output = input("Nazwa pliku CSV (domyślnie: metrics_export.csv): ").strip()
            output = output or "metrics_export.csv"
            hours_input = input("Liczba godzin (ENTER = wszystkie): ").strip()
            hours = int(hours_input) if hours_input else None
            export_to_csv(repository, output, hours=hours)

        elif choice == "5":
            output = input("Nazwa pliku JSON (domyślnie: metrics_export.json): ").strip()
            output = output or "metrics_export.json"
            hours_input = input("Liczba godzin (ENTER = wszystkie): ").strip()
            hours = int(hours_input) if hours_input else None
            export_to_json(repository, output, hours=hours)

        elif choice == "6":
            hours_input = input("Liczba godzin (domyślnie: 24): ").strip()
            hours = int(hours_input) if hours_input else 24
            stats = repository.get_aggregated_stats(hours=hours)
            print("\nRaw Stats:")
            print(stats)

        else:
            print("[ERROR] Nieprawidłowa opcja")


# ==============================================================================
# CLI INTERFACE
# ==============================================================================

def main():
    """Główna funkcja CLI"""
    import argparse

    parser = argparse.ArgumentParser(
        description="Analiza metryk RAG (niezależnie od typu bazy)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Przykłady użycia:

  # Podstawowy dashboard (ostatnie 24h)
  python test_view_metrics_analyzer.py

  # Dashboard dla ostatnich 48h
  python test_view_metrics_analyzer.py --hours 48

  # Filtruj po kolekcji
  python test_view_metrics_analyzer.py --collection my_collection --hours 24

  # Eksport do CSV
  python test_view_metrics_analyzer.py --export metrics.csv --hours 168

  # Eksport do JSON
  python test_view_metrics_analyzer.py --export-json metrics.json

  # Tryb interaktywny
  python test_view_metrics_analyzer.py --interactive

  # Użyj innego storage niż w .env
  python test_view_metrics_analyzer.py --storage-type file --hours 24
        """
    )

    parser.add_argument(
        "--hours",
        type=int,
        default=24,
        help="Zakres czasowy w godzinach (domyślnie: 24)"
    )

    parser.add_argument(
        "--collection",
        default=None,
        help="Filtruj po nazwie kolekcji"
    )

    parser.add_argument(
        "--limit",
        type=int,
        default=1000,
        help="Maksymalna liczba rekordów (domyślnie: 1000)"
    )

    parser.add_argument(
        "--export",
        help="Eksportuj dane do pliku CSV"
    )

    parser.add_argument(
        "--export-json",
        help="Eksportuj dane do pliku JSON"
    )

    parser.add_argument(
        "--storage-type",
        choices=["postgres", "file"],
        default=None,
        help="Typ storage (nadpisuje .env)"
    )

    parser.add_argument(
        "--interactive",
        action="store_true",
        help="Uruchom w trybie interaktywnym"
    )

    parser.add_argument(
        "--raw-stats",
        action="store_true",
        help="Pokaż surowe statystyki (bez formatowania)"
    )

    args = parser.parse_args()

    # ===== INICJALIZACJA REPOSITORY =====
    try:
        if args.storage_type:
            from metrics import create_repository
            repository = create_repository(args.storage_type)
        else:
            repository = get_repository()

        logger.info(f"Używam repository: {repository.__class__.__name__}")

        # Test połączenia
        if not repository.test_connection():
            print("[ERROR] Nie można połączyć się z storage metryk")
            print("Sprawdź konfigurację w .env")
            sys.exit(1)

    except Exception as e:
        print(f"[ERROR] Błąd inicjalizacji repository: {e}")
        logger.error(f"Repository init error: {e}")
        sys.exit(1)

    # ===== WYKONAJ AKCJĘ =====
    try:
        if args.interactive:
            # Tryb interaktywny
            interactive_mode(repository)

        elif args.export:
            # Eksport do CSV
            success = export_to_csv(
                repository,
                args.export,
                hours=args.hours,
                collection_name=args.collection,
                limit=args.limit
            )
            sys.exit(0 if success else 1)

        elif args.export_json:
            # Eksport do JSON
            success = export_to_json(
                repository,
                args.export_json,
                hours=args.hours,
                collection_name=args.collection,
                limit=args.limit
            )
            sys.exit(0 if success else 1)

        elif args.raw_stats:
            # Surowe statystyki
            stats = repository.get_aggregated_stats(
                hours=args.hours,
                collection_name=args.collection
            )
            print("\n" + "=" * 70)
            print("RAW STATISTICS")
            print("=" * 70)
            print(stats)
            print("=" * 70)

        else:
            # Domyślnie: dashboard
            print_dashboard(
                repository,
                hours=args.hours,
                collection_name=args.collection,
                limit=args.limit
            )

    except KeyboardInterrupt:
        print("\n\n[INFO] Przerwano przez użytkownika")
        sys.exit(0)

    except Exception as e:
        print(f"\n[ERROR] Nieoczekiwany błąd: {e}")
        logger.error(f"Unexpected error: {e}", exc_info=True)
        sys.exit(1)

    finally:
        # Cleanup
        try:
            repository.close()
        except:
            pass


if __name__ == "__main__":
    main()

# Description
#Tryb interaktywny (--interactive)
# Bash
#
# python test_view_metrics_analyzer.py --interactive
# Eksport do JSON (oprócz CSV)
# Bash
#
# python test_view_metrics_analyzer.py --export-json metrics.json --hours 48
# Surowe statystyki (--raw-stats)
# Bash
#
# python test_view_metrics_analyzer.py --raw-stats --hours 24
# Nadpisanie typu storage z CLI
# Bash
#
# python test_view_metrics_analyzer.py --storage-type file --hours 24
# ✅ Przykłady użycia
# Bash
#
# # Dashboard dla ostatnich 24h (domyślnie)
# python test_view_metrics_analyzer.py
#
# # Dashboard dla ostatnich 7 dni
# python test_view_metrics_analyzer.py --hours 168
#
# # Filtruj po kolekcji
# python test_view_metrics_analyzer.py --collection iso_standards --hours 48
#
# # Eksport do CSV (ostatnie 30 dni)
# python test_view_metrics_analyzer.py --export report.csv --hours 720
#
# # Eksport do JSON
# python test_view_metrics_analyzer.py --export-json data.json --hours 24
#
# # Tryb interaktywny (menu)
# python test_view_metrics_analyzer.py --interactive
#
# # Wymuś użycie pliku zamiast Postgres
# python test_view_metrics_analyzer.py --storage-type file
#
# # Kombinacja filtrów
# python test_view_metrics_analyzer.py --collection iso --hours 12 --limit 500

