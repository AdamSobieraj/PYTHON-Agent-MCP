# metrics_analyzer.py

import json
import pandas as pd
from datetime import datetime, timedelta
from typing import Dict, Optional
import sys
import os


# ==============================================================================
# KONFIGURACJA
# ==============================================================================

def get_storage_type() -> str:
    """Pobierz typ storage z ENV"""
    return os.getenv("METRICS_STORAGE_TYPE", "file").lower()


# ==============================================================================
# DATA LOADING
# ==============================================================================

def load_metrics_from_file(file_path: str = None) -> pd.DataFrame:
    """Wczytaj metryki z pliku JSONL"""
    if file_path is None:
        file_path = os.getenv("RAG_METRICS_FILE", "rag_metrics.jsonl")

    metrics = []

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    metrics.append(json.loads(line))
    except FileNotFoundError:
        print(f"[ERROR] Plik {file_path} nie istnieje.", file=sys.stderr)
        return pd.DataFrame()

    if not metrics:
        print("[WARNING] Brak metryk w pliku.", file=sys.stderr)
        return pd.DataFrame()

    return _process_metrics_to_dataframe(metrics)


def load_metrics_from_postgres(
        limit: int = 1000,
        collection_name: Optional[str] = None,
        hours: Optional[int] = None
) -> pd.DataFrame:
    """Wczytaj metryki z PostgreSQL"""
    try:
        from metrics_db import MetricsRepository

        repo = MetricsRepository()
        metrics = repo.get_retrieval_metrics(
            limit=limit,
            collection_name=collection_name,
            hours=hours
        )

        if not metrics:
            print("[WARNING] Brak metryk w bazie PostgreSQL.", file=sys.stderr)
            return pd.DataFrame()

        return _process_metrics_to_dataframe(metrics)

    except Exception as e:
        print(f"[ERROR] Nie można załadować danych z PostgreSQL: {e}", file=sys.stderr)
        return pd.DataFrame()


def _process_metrics_to_dataframe(metrics: list) -> pd.DataFrame:
    """Przetwórz surowe metryki do DataFrame"""
    # Flatten nested structure
    flattened = []
    for m in metrics:
        if "retrieval" in m:  # Full RAG metrics
            flat = {**m["retrieval"]}
            if m.get("generation"):
                flat.update({f"gen_{k}": v for k, v in m["generation"].items()})
            flat["total_latency_ms"] = m.get("total_latency_ms")
        else:  # Just retrieval metrics
            flat = m
        flattened.append(flat)

    df = pd.DataFrame(flattened)

    # Convert timestamp to datetime
    if "timestamp" in df.columns:
        df["timestamp"] = pd.to_datetime(df["timestamp"])

    return df


def load_metrics(
        file_path: Optional[str] = None,
        limit: int = 1000,
        collection_name: Optional[str] = None,
        hours: Optional[int] = None
) -> pd.DataFrame:
    """
    Główna funkcja ładująca metryki (automatycznie wybiera źródło)
    """
    storage_type = get_storage_type()

    if storage_type == "postgres":
        print(f"[INFO] Ładowanie metryk z PostgreSQL...", file=sys.stderr)
        return load_metrics_from_postgres(limit, collection_name, hours)
    else:
        print(f"[INFO] Ładowanie metryk z pliku...", file=sys.stderr)
        return load_metrics_from_file(file_path)


# ==============================================================================
# ANALIZA
# ==============================================================================

def calculate_percentile(series, p):
    """Oblicz percentyl (bezpiecznie)"""
    try:
        return series.quantile(p)
    except:
        return 0


def analyze_retrieval_performance(df: pd.DataFrame) -> Dict:
    """Analiza performance retrieval"""
    if df.empty:
        return {}

    stats = {
        "total_queries": len(df),
        "avg_latency_ms": df["latency_ms"].mean(),
        "p50_latency_ms": calculate_percentile(df["latency_ms"], 0.5),
        "p95_latency_ms": calculate_percentile(df["latency_ms"], 0.95),
        "p99_latency_ms": calculate_percentile(df["latency_ms"], 0.99),
        "avg_results": df["num_results"].mean(),
        "avg_top_score": df["avg_score"].mean(),
        "queries_with_no_results": len(df[df["num_results"] == 0]),
    }

    if "collection_name" in df.columns:
        collection_stats = df.groupby("collection_name").agg({
            "latency_ms": ["mean", "count"],
            "avg_score": "mean",
            "num_results": "mean"
        }).round(2)
        stats["per_collection"] = collection_stats.to_dict()

    return stats


def print_separator(width=70):
    """Drukuj separator"""
    print("=" * width)


def print_section_header(title: str, width=70):
    """Drukuj nagłówek sekcji"""
    print("\n" + title)
    print("-" * width)


def print_dashboard(df: pd.DataFrame):
    """Wydrukuj dashboard metryk"""
    if df.empty:
        print_separator()
        print("BRAK DANYCH DO WYŚWIETLENIA")
        print_separator()
        return

    stats = analyze_retrieval_performance(df)

    print_separator()
    print("         RAG RETRIEVAL PERFORMANCE DASHBOARD")
    print(f"         Storage: {get_storage_type().upper()}")
    print_separator()

    print_section_header("OGÓLNE STATYSTYKI")
    print(f"   Total Queries:        {stats['total_queries']}")
    no_results_pct = (stats['queries_with_no_results'] / stats['total_queries'] * 100) if stats[
                                                                                              'total_queries'] > 0 else 0
    print(f"   Queries bez wyników:  {stats['queries_with_no_results']} ({no_results_pct:.1f}%)")

    print_section_header("LATENCY")
    print(f"   Average:   {stats['avg_latency_ms']:.0f} ms")
    print(f"   P50:       {stats['p50_latency_ms']:.0f} ms")
    print(f"   P95:       {stats['p95_latency_ms']:.0f} ms")
    print(f"   P99:       {stats['p99_latency_ms']:.0f} ms")

    print_section_header("QUALITY")
    print(f"   Avg Top Score:     {stats['avg_top_score']:.3f}")
    print(f"   Avg Results/Query: {stats['avg_results']:.1f}")

    if "collection_name" in df.columns:
        print_section_header("PER COLLECTION")
        collection_summary = df.groupby("collection_name").agg({
            "latency_ms": "mean",
            "avg_score": "mean",
            "num_results": "mean",
            "query": "count"
        }).rename(columns={"query": "count"}).round(2)

        for collection, row in collection_summary.iterrows():
            print(f"   {collection}:")
            print(f"      Queries: {int(row['count'])}, "
                  f"Latency: {row['latency_ms']:.0f}ms, "
                  f"Avg Score: {row['avg_score']:.3f}")

    print_section_header("ALERTS")
    alerts = []

    slow_queries = df[df["latency_ms"] > 2000]
    if len(slow_queries) > 0:
        alerts.append(f"   [WARNING] {len(slow_queries)} slow queries (>2000ms)")

    low_quality = df[df["avg_score"] < 0.5]
    if len(low_quality) > 0:
        alerts.append(f"   [WARNING] {len(low_quality)} low quality queries (score <0.5)")

    if stats['queries_with_no_results'] > 0:
        alerts.append(f"   [INFO] {stats['queries_with_no_results']} queries returned no results")

    if alerts:
        for alert in alerts:
            print(alert)
    else:
        print("   [OK] No critical issues detected")

    print_separator()

    if len(df) > 0:
        print_section_header("TOP 5 SLOWEST QUERIES")
        slowest = df.nlargest(5, "latency_ms")[["query", "latency_ms", "collection_name"]]
        for idx, row in slowest.iterrows():
            query_preview = row['query'][:60] + "..." if len(row['query']) > 60 else row['query']
            print(f"   {row['latency_ms']:.0f}ms - {query_preview} [{row['collection_name']}]")

    print_separator()


def analyze_time_range(df: pd.DataFrame, hours: int = 24) -> pd.DataFrame:
    """Analiza dla ostatnich N godzin"""
    if df.empty or "timestamp" not in df.columns:
        return df

    cutoff = datetime.now() - timedelta(hours=hours)
    recent = df[df["timestamp"] > cutoff]

    print(f"\n[INFO] Dane z ostatnich {hours}h ({len(recent)} queries)\n")
    return recent


# ==============================================================================
# CLI Usage
# ==============================================================================

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Analiza metryk RAG")
    parser.add_argument("--file", default=None, help="Plik z metrykami (tylko dla storage=file)")
    parser.add_argument("--hours", type=int, default=None, help="Analizuj ostatnie N godzin")
    parser.add_argument("--collection", default=None, help="Filtruj po collection_name")
    parser.add_argument("--limit", type=int, default=1000, help="Max rekordów z PostgreSQL")
    parser.add_argument("--export", help="Eksportuj do CSV")

    args = parser.parse_args()

    # Wczytaj dane
    df = load_metrics(
        file_path=args.file,
        limit=args.limit,
        collection_name=args.collection,
        hours=args.hours
    )

    if df.empty:
        print("[ERROR] Brak danych do analizy.")
        sys.exit(1)

    # Filtruj po czasie jeśli podano (dla file storage)
    if args.hours and get_storage_type() == "file":
        df = analyze_time_range(df, args.hours)

    # Wyświetl dashboard
    print_dashboard(df)

    # Eksport do CSV
    if args.export:
        df.to_csv(args.export, index=False)
        print(f"\n[OK] Dane wyeksportowane do {args.export}")