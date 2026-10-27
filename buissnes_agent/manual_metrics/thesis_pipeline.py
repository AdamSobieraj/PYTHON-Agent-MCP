"""
Thesis pipeline: experiments E1-E5 -> statistics -> export, in one go.

This is a manual, opt-in orchestration (never triggered by the
normal application flow):

    python -m buissnes_agent.manual_metrics.thesis_pipeline
    python -m buissnes_agent.manual_metrics.thesis_pipeline --exp E1,E3
    python -m buissnes_agent.manual_metrics.thesis_pipeline --skip-experiments
    python -m buissnes_agent.manual_metrics.thesis_pipeline --out results/run1

Steps:
    1. run the selected experiments (E1-E4 chunking rows land in the
       metrics DB; E5 = retrieval A/B dense vs hybrid, results land in
       results/e5_results.json),
    2. load the experiment rows from the metrics DB and compute,
       per metric: mean/std/95% bootstrap CI per strategy +
       pairwise Wilcoxon tests (paired per document); E5: per-arm
       Hit@k/Recall@k/MRR + paired Wilcoxon (per query, fallbacks
       excluded),
    3. export per-metric CSV + LaTeX tables and a run log
       into the output directory.

--skip-experiments: step 1 is omitted (re-analyze data already
in the metrics database, e.g. after a previous experiment run).
"""
import argparse
import csv
import json
import os
import sys
from datetime import datetime
from typing import Any, Dict, List, Optional

# Allow both invocation styles: as a module (python -m ...) and
# directly (python buissnes_agent/manual_metrics/thesis_pipeline.py)
_PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)

from dotenv import load_dotenv

from buissnes_agent.metrics import get_repository
from buissnes_agent.manual_metrics.run_experiments import (
    RUNNERS,
    _load_experiments_config,
)
from buissnes_agent.manual_metrics.statistics import (
    bootstrap_ci,
    export_csv,
    latency_table,
    summary_table,
    to_latex_table,
    wilcoxon_test,
)

# Default metrics summarized per strategy (chapter 4: quality + cost/time)
DEFAULT_METRICS = [
    "coherence",
    "coverage",
    "over_limit_ratio",
    "avg_chunk_len",
    "std_chunk_len",
    "num_chunks",
    "chunking_ms",
    "total_ms",
]

CAPTIONS = {
    "coherence": "Semantic coherence per chunking strategy",
    "coverage": "Content coverage per chunking strategy",
    "over_limit_ratio": "Share of chunks exceeding the size limit",
    "avg_chunk_len": "Average chunk length (chars) per strategy",
    "std_chunk_len": "Std. deviation of chunk length (H5: length stability)",
    "num_chunks": "Number of chunks per document (mean) per strategy",
    "chunking_ms": "Chunking phase time (ms) per strategy",
    "embedding_ms": "Embedding phase time (ms) per strategy",
    "storage_ms": "Storage phase time (ms) per strategy",
    "total_ms": "Total processing time (ms) per strategy",
    "llm_calls": "LLM calls (agentic strategy) per document",
    "fallbacks": "Fallback count per document",
    "embedding_http_requests": "Embedding HTTP requests per document",
}


def _load_experiment_records(limit: int = 10000) -> List[Dict[str, Any]]:
    """Load manual chunking rows written by experiments (E1-E4)."""
    repo = get_repository()
    rows = repo.get_chunking_metrics_manual(limit=limit)
    return [r for r in rows if r.get("experiment_id")]


def _run_experiments(
        cfg: Dict[str, Any],
        dataset_path: str,
        names: List[str],
) -> None:
    for name in names:
        print(f"\n=== EXPERIMENT {name} ===")
        RUNNERS[name](cfg, dataset_path)


def _analyze(
        records: List[Dict[str, Any]],
        metrics: List[str],
        out_dir: str,
) -> Dict[str, Any]:
    """Per-metric summary + exports. Returns the summaries dict."""
    summaries: Dict[str, Any] = {}
    written: List[str] = []

    for metric in metrics:
        summary = summary_table(records, metric)
        summaries[metric] = summary

        csv_path = export_csv(
            summary, os.path.join(out_dir, f"{metric}_summary.csv")
        )
        written.append(csv_path)

        tex = to_latex_table(
            summary, caption=CAPTIONS.get(metric, f"Metric: {metric}")
        )
        tex_path = os.path.join(out_dir, f"{metric}_table.tex")
        with open(tex_path, "w", encoding="utf-8") as f:
            f.write(tex + "\n")
        written.append(tex_path)

        strategies = summary.get("strategies", {})
        print(
            f"[stats] {metric}: "
            + ", ".join(
                f"{name} mean={row['mean']} (n={row['n']}, "
                f"CI95 {row['ci_low']}..{row['ci_high']})"
                for name, row in strategies.items()
            )
            if strategies
            else f"[stats] {metric}: no data"
        )
        for pair, res in summary.get("wilcoxon", {}).items():
            p = res.get("p_value")
            sig = "p<0.05" if p is not None and p < 0.05 else "n.s."
            print(f"[wilcoxon] {metric}: {pair} -> {sig} (p={p})")

    return {
        "summaries": summaries,
        "written": written,
    }


# Latency fields summarized with p50/p95/p99 (chapter 4 time metrics)
DOC_LATENCY_FIELDS = ["chunking_ms", "embedding_ms", "storage_ms", "total_ms"]
QUERY_LATENCY_FIELDS = ["latency_ms", "embedding_latency_ms", "search_latency_ms"]

FIELD_LABELS = {
    "chunking_ms": "chunking",
    "embedding_ms": "embedding",
    "storage_ms": "storage",
    "total_ms": "total",
    "latency_ms": "latency",
    "embedding_latency_ms": "embedding (retrieval)",
    "search_latency_ms": "search (retrieval)",
}


def _latency_rows(table: Dict[str, Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Flatten the latency table into CSV-friendly rows."""
    rows: List[Dict[str, Any]] = []
    for group, row in table.items():
        for field, stats in row.items():
            if field in FIELD_LABELS and isinstance(stats, dict):
                rows.append(
                    {
                        "group": group,
                        "phase": field,
                        **stats,
                    }
                )
    return rows


def _latency_to_latex(
        table: Dict[str, Dict[str, Any]],
        caption: str,
        group_header: str = "Strategy",
) -> str:
    """LaTeX table: rows = (group, phase), columns = n/mean/p50/p95/p99."""
    lines = [
        r"\begin{table}[H]",
        r"\centering",
        rf"\caption{{{caption}}}",
        r"\small",
        r"\begin{tabular}{@{}llrrrrr@{}}",
        r"\toprule",
        f"\\textbf{{{group_header}}} & \\textbf{{Phase}}"
        r" & \textbf{n} & \textbf{mean (ms)}"
        r" & \textbf{p50} & \textbf{p95} & \textbf{p99} \\",
        r"\midrule",
    ]
    for group, row in table.items():
        for field, stats in row.items():
            if field not in FIELD_LABELS or not isinstance(stats, dict):
                continue
            lines.append(
                f"\\textbf{{{group}}} & {FIELD_LABELS[field]}"
                f" & {stats['n']} & {stats['mean']:.0f}"
                f" & {stats['p50']:.0f} & {stats['p95']:.0f}"
                f" & {stats['p99']:.0f} \\\\"
            )
    lines += [r"\bottomrule", r"\end{tabular}", r"\end{table}"]
    return "\n".join(lines)


def _analyze_latencies(
        records: List[Dict[str, Any]],
        out_dir: str,
) -> Dict[str, Any]:
    """
    p50/p95/p99 latency summary (chapter 4: 'p50 i p95 dla serii
    zapytan / dokumentow').

    1. documents: per-phase latencies of the experiment runs
       (rag_chunking_metrics_manual rows),
    2. queries: retrieval/generation latencies from the RAG tables
       (only when rows exist - i.e. after real A/B query series).
    """
    written: List[str] = []
    result: Dict[str, Any] = {}

    # --- 1) documents (experiments) ---
    doc_table = latency_table(records, DOC_LATENCY_FIELDS)
    result["documents"] = doc_table

    csv_path = os.path.join(out_dir, "latency_documents.csv")
    with open(csv_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f, fieldnames=["group", "phase", "n", "mean", "p50", "p95", "p99"]
        )
        writer.writeheader()
        writer.writerows(_latency_rows(doc_table))
    written.append(csv_path)

    tex_path = os.path.join(out_dir, "latency_documents_table.tex")
    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(
            _latency_to_latex(
                doc_table,
                "Processing phase latencies (ms) per chunking strategy "
                "(p50 / p95 / p99, per document)",
            )
            + "\n"
        )
    written.append(tex_path)

    print(
        "[latency] documents: "
        + ", ".join(
            f"{g}/{p} p50={doc_table[g][p]['p50']}ms p95={doc_table[g][p]['p95']}ms"
            for g in doc_table
            for p in DOC_LATENCY_FIELDS
            if doc_table[g][p]["n"]
        )
    )

    # --- 2) queries (RAG tables, when populated) ---
    repo = get_repository()
    retrieval_rows = repo.get_retrieval_metrics(limit=10000)
    generation_rows = repo.get_generation_metrics(limit=10000)

    if retrieval_rows:
        ret_table = latency_table(
            retrieval_rows, QUERY_LATENCY_FIELDS,
            group_key="collection_name", group_all="ALL",
        )
        result["queries_retrieval"] = ret_table
        tex_path = os.path.join(out_dir, "query_retrieval_latency_table.tex")
        with open(tex_path, "w", encoding="utf-8") as f:
            f.write(
                _latency_to_latex(
                    ret_table,
                    "Retrieval latencies (ms) per query series "
                    "(p50 / p95 / p99)",
                    group_header="Collection",
                )
                + "\n"
            )
        written.append(tex_path)
        print(f"[latency] queries: {len(retrieval_rows)} retrieval rows summarized")
    else:
        print("[latency] queries: no retrieval rows yet (run A/B query series first)")

    if generation_rows:
        gen_table = latency_table(
            generation_rows, ["latency_ms"], group_key=None, group_all="ALL"
        )
        result["queries_generation"] = gen_table
        tex_path = os.path.join(out_dir, "query_generation_latency_table.tex")
        with open(tex_path, "w", encoding="utf-8") as f:
            f.write(
                _latency_to_latex(
                    gen_table,
                    "Generation latencies (ms) per query series "
                    "(p50 / p95 / p99)",
                    group_header="Stack",
                )
                + "\n"
            )
        written.append(tex_path)
        print(f"[latency] queries: {len(generation_rows)} generation rows summarized")

    return {"written": written, "tables": result}


# ==============================================================================
# E5: retrieval A/B (dense vs hybrid) - analysis of results/e5_results.json
# ==============================================================================
E5_ARMS = ("dense", "hybrid")


def _analyze_e5(out_dir: str) -> Optional[Dict[str, Any]]:
    """
    E5: dense vs hybrid retrieval - per-arm quality + paired comparison.

    Reads results/e5_results.json (written by run_experiments.run_e5):
    per-query retrieved IDs already scored against the ground truth.
    Exports:
        e5_retrieval_table.tex   - Hit@k / Recall@k (95% CI) / MRR per arm
                                   + Wilcoxon p-values (paired per query),
        e5_retrieval_summary.csv - the same numbers as CSV,
        e5_latency_table.tex     - p50/p95/p99 from the metrics DB rows
                                   (strategy = dense/hybrid, E5 collection).

    Queries where a requested arm fell back to the other strategy are
    excluded from the pairing (fallbacks are counted separately).
    """
    results_path = os.path.join(_PROJECT_ROOT, "results", "e5_results.json")
    if not os.path.exists(results_path):
        print("[E5] brak results/e5_results.json - pomijam analize "
              "(najpierw uruchom eksperyment E5)")
        return None

    with open(results_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    collection = data.get("collection", "")
    top_k = data.get("top_k", 10)
    queries: List[Dict[str, Any]] = data.get("queries", [])
    written: List[str] = []

    def _fmt(value: Optional[float], digits: int = 3) -> str:
        return f"{value:.{digits}f}" if value is not None else "-"

    # --- per-arm quality (only the queries the arm ACTUALLY ran) ---
    per_arm: Dict[str, Any] = {}
    for arm in E5_ARMS:
        rows = [
            q["arms"][arm] for q in queries
            if q["arms"][arm]["strategy_used"] == arm
        ]
        recalls = [r["recall"] for r in rows if r["recall"] is not None]
        per_arm[arm] = {
            "n_ran": len(rows),
            "n_fallback": len(queries) - len(rows),
            "hit_rate": (
                sum(1 for r in rows if r["hit"]) / len(rows)
            ) if rows else None,
            "recall_mean": (sum(recalls) / len(recalls)) if recalls else None,
            "recall_ci95": bootstrap_ci(recalls) if len(recalls) >= 2 else None,
            "mrr_mean": (
                sum(r["mrr"] for r in rows) / len(rows)
            ) if rows else None,
            "search_latency_mean_ms": (
                sum(r["search_latency_ms"] for r in rows) / len(rows)
            ) if rows else None,
        }

    # --- paired comparison dense vs hybrid (fallbacks excluded) ---
    recall_pairs: List[tuple] = []
    latency_pairs: List[tuple] = []
    for q in queries:
        d, h = q["arms"]["dense"], q["arms"]["hybrid"]
        if d["strategy_used"] != "dense" or h["strategy_used"] != "hybrid":
            continue
        if d["recall"] is not None and h["recall"] is not None:
            recall_pairs.append((d["recall"], h["recall"]))
        latency_pairs.append((d["search_latency_ms"], h["search_latency_ms"]))

    def _paired_test(pairs: List[tuple]) -> Dict[str, Any]:
        if len(pairs) < 2:
            return {
                "statistic": None, "p_value": None,
                "note": f"tylko {len(pairs)} par zapytan - test pominiety",
            }
        return wilcoxon_test([p[0] for p in pairs], [p[1] for p in pairs])

    wilcoxon = {
        "recall": _paired_test(recall_pairs),
        "search_latency_ms": _paired_test(latency_pairs),
    }
    n_paired = len(latency_pairs)

    # --- LaTeX: retrieval quality ---
    lines = [
        r"\begin{table}[H]",
        r"\centering",
        rf"\caption{{E5: retrieval quality, top-{top_k} "
        rf"(corpus: {collection}, {data.get('chunks', '-')} chunks, "
        rf"{len(queries)} queries)}}",
        r"\small",
        r"\begin{tabular}{@{}lrrrl@{}}",
        r"\toprule",
        r"\textbf{Strategy} & \textbf{Hit@k}"
        r" & \textbf{Recall@k} & \textbf{MRR} & \textbf{Recall@k CI 95\%} \\",
        r"\midrule",
    ]
    for arm in E5_ARMS:
        row = per_arm[arm]
        ci = row["recall_ci95"]
        ci_str = f"[{ci[0]:.3f}; {ci[1]:.3f}]" if ci else "-"
        lines.append(
            f"\\textbf{{{arm}}} & {_fmt(row['hit_rate'])}"
            f" & {_fmt(row['recall_mean'])} & {_fmt(row['mrr_mean'])}"
            f" & {ci_str} \\\\"
        )
    lines.append(r"\midrule")
    for key, label in (
            ("recall", f"Recall@{top_k}"),
            ("search_latency_ms", "czas wyszukiwania"),
    ):
        res = wilcoxon[key]
        p = res.get("p_value")
        if p is not None:
            sig = f"p = {p:.4f}" + (
                " (istotne, $\\alpha = 0{,}05$)" if p < 0.05
                else " (n. istotne)"
            )
        else:
            sig = res.get("note", "-")
        note = f"Wilcoxon signed-rank (pary per zapytanie): {label} - {sig}"
        lines.append(rf"\multicolumn{{5}}{{@{{}}l}}{{{note}}} \\")
    lines += [r"\bottomrule", r"\end{tabular}", r"\end{table}"]

    tex_path = os.path.join(out_dir, "e5_retrieval_table.tex")
    with open(tex_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    written.append(tex_path)

    # --- CSV ---
    csv_path = os.path.join(out_dir, "e5_retrieval_summary.csv")
    with open(csv_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "strategy", "n_ran", "n_fallback", "hit_rate", "recall_mean",
            "recall_ci95_low", "recall_ci95_high", "mrr_mean",
            "search_latency_mean_ms",
        ])
        for arm in E5_ARMS:
            row = per_arm[arm]
            ci = row["recall_ci95"] or (None, None)
            writer.writerow([
                arm, row["n_ran"], row["n_fallback"],
                row["hit_rate"], row["recall_mean"],
                ci[0], ci[1],
                row["mrr_mean"], row["search_latency_mean_ms"],
            ])
    written.append(csv_path)

    # --- LaTeX: latencies from the metrics DB (strategy rows) ---
    db_table: Optional[Dict[str, Any]] = None
    try:
        repo = get_repository()
        rows_db = [
            r for r in repo.get_retrieval_metrics(
                limit=10000, collection_name=collection
            )
            if r.get("strategy") in E5_ARMS
        ]
        if rows_db:
            db_table = latency_table(
                rows_db, QUERY_LATENCY_FIELDS,
                group_key="strategy", group_all="E5",
            )
            tex_path = os.path.join(out_dir, "e5_latency_table.tex")
            with open(tex_path, "w", encoding="utf-8") as f:
                f.write(
                    _latency_to_latex(
                        db_table,
                        "E5: retrieval latencies (ms) per strategy "
                        "(p50 / p95 / p99, per query)",
                        group_header="Strategy",
                    )
                    + "\n"
                )
            written.append(tex_path)
    except Exception as e:
        print(f"[E5] odczyt metryk z bazy nieudany ({e}) - "
              f"pominam tabela latencji")

    print(
        "[E5] "
        + ", ".join(
            f"{arm}: hit={_fmt(per_arm[arm]['hit_rate'])} "
            f"recall={_fmt(per_arm[arm]['recall_mean'])} "
            f"mrr={_fmt(per_arm[arm]['mrr_mean'])} "
            f"(n={per_arm[arm]['n_ran']}, "
            f"fallback={per_arm[arm]['n_fallback']})"
            for arm in E5_ARMS
        )
    )
    for name, res in wilcoxon.items():
        p = res.get("p_value")
        sig = f"p={p:.4f}" if p is not None else res.get("note", "n/d")
        print(f"[E5][wilcoxon] {name}: {sig}")

    return {
        "experiment_id": data.get("experiment_id"),
        "collection": collection,
        "top_k": top_k,
        "n_queries": len(queries),
        "n_paired": n_paired,
        "per_arm": per_arm,
        "wilcoxon": wilcoxon,
        "db_latency": db_table,
        "written": written,
    }


def main(argv: Optional[List[str]] = None) -> int:
    load_dotenv()

    parser = argparse.ArgumentParser(
        description="Thesis pipeline: experiments -> statistics -> export"
    )
    parser.add_argument(
        "--exp", default="all",
        help="experiments to run: all or comma-separated E1,E2,E3,E4,E5 "
             "(default: all)"
    )
    parser.add_argument(
        "--config", default="config/experiments.yaml",
        help="path to experiments configuration (default: config/experiments.yaml)"
    )
    parser.add_argument(
        "--dataset", default=None,
        help="override dataset_path from the configuration"
    )
    parser.add_argument(
        "--out", default="results",
        help="output directory for CSV/LaTeX exports and the run log"
    )
    parser.add_argument(
        "--metrics", default=",".join(DEFAULT_METRICS),
        help="comma-separated metric names to summarize "
             "(default: " + ",".join(DEFAULT_METRICS) + ")"
    )
    parser.add_argument(
        "--skip-experiments", action="store_true",
        help="do not run experiments; analyze rows already in the DB"
    )
    args = parser.parse_args(argv)

    cfg = _load_experiments_config(args.config)
    dataset_path = args.dataset or cfg.get("dataset_path", "buissnes_agent/inputs")
    metrics = [m.strip() for m in args.metrics.split(",") if m.strip()]

    names = (
        list(RUNNERS) if args.exp == "all"
        else [e.strip().upper() for e in args.exp.split(",") if e.strip()]
    )
    unknown = [n for n in names if n not in RUNNERS]
    if unknown:
        print(f"Unknown experiment(s): {', '.join(unknown)} "
              f"(available: {', '.join(RUNNERS)})")
        return 1

    out_dir = args.out
    os.makedirs(out_dir, exist_ok=True)

    print(f"= THESIS PIPELINE | exp: {', '.join(names)} "
          f"| dataset: {dataset_path} | out: {out_dir} =")

    # 1) experiments
    if args.skip_experiments:
        print("\n=== EXPERIMENTS SKIPPED (--skip-experiments) ===")
    else:
        _run_experiments(cfg, dataset_path, names)

    # 2) statistics from the metrics DB (experiment rows only)
    print("\n=== STATISTICS ===")
    records = _load_experiment_records()
    result: Dict[str, Any] = {"summaries": {}, "written": []}
    if not records:
        if "E5" in names:
            print("No chunking rows in the metrics database - "
                  "skipping the E1-E4 statistics "
                  "(E5 is analyzed from results/e5_results.json).")
        else:
            print("No experiment rows in the metrics database - "
                  "run the experiments first (drop --skip-experiments).")
            return 1
    else:
        print(f"[stats] loaded {len(records)} experiment records "
              f"(experiments: {sorted({r.get('experiment_id') for r in records})})")
        result = _analyze(records, metrics, out_dir)

    # 2b) latency percentiles p50/p95/p99 (chapter 4 time metrics)
    print("\n=== LATENCY PERCENTILES (p50/p95/p99) ===")
    latency_result = (
        _analyze_latencies(records, out_dir)
        if records else {"written": [], "tables": {}}
    )

    # 2c) E5: retrieval A/B (dense vs hybrid)
    print("\n=== E5: RETRIEVAL A/B (dense vs hybrid) ===")
    e5_result = _analyze_e5(out_dir) if "E5" in names else None

    # 3) run log
    log_path = os.path.join(out_dir, "run_log.json")
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump(
            {
                "timestamp": datetime.now().isoformat(),
                "experiments": names,
                "dataset": dataset_path,
                "metrics": metrics,
                "records_analyzed": len(records),
                "summaries": result["summaries"],
                "latency": latency_result["tables"],
                "e5": e5_result,
                "exported_files": result["written"]
                + latency_result["written"]
                + (e5_result["written"] if e5_result else [])
                + [log_path],
            },
            f,
            indent=2,
            ensure_ascii=False,
        )

    n_files = (
        len(result["written"]) + len(latency_result["written"])
        + (len(e5_result["written"]) if e5_result else 0)
    )
    print(f"\n= PIPELINE DONE. {n_files + 1} files "
          f"in: {os.path.abspath(out_dir)} =")
    return 0


if __name__ == "__main__":
    sys.exit(main())
