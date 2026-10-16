"""
Statistical analysis of experiment results ("Statistical analysis" section):
- arithmetic mean (eq:mean),
- standard deviation (eq:std, denominator n-1),
- 95% confidence interval via bootstrap,
- Wilcoxon test (scipy) — paired per-document comparisons,
- table export: CSV / LaTeX.
"""
import csv
import math
import random
from typing import Any, Dict, List, Optional, Sequence, Tuple

from scipy import stats


def mean(values: Sequence[float]) -> float:
    """Arithmetic mean (eq:mean)."""
    if not values:
        return 0.0
    return sum(values) / len(values)


def std(values: Sequence[float]) -> float:
    """Standard deviation, unbiased version (eq:std)."""
    if len(values) < 2:
        return 0.0
    mu = mean(values)
    return math.sqrt(sum((x - mu) ** 2 for x in values) / (len(values) - 1))


def percentile(values: Sequence[float], p: float) -> float:
    """
    Percentile with linear interpolation (p in [0, 1]).
    Chapter 4 time metrics: p50 / p95 / p99 of a series.
    """
    if not values:
        return 0.0
    data = sorted(float(v) for v in values)
    if len(data) == 1:
        return data[0]
    k = (len(data) - 1) * p
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return data[int(k)]
    return data[f] * (c - k) + data[c] * (k - f)


def latency_percentiles(values: Sequence[float]) -> Dict[str, float]:
    """n / mean / p50 / p95 / p99 for one latency series."""
    if not values:
        return {"n": 0, "mean": 0.0, "p50": 0.0, "p95": 0.0, "p99": 0.0}
    return {
        "n": len(values),
        "mean": round(mean(values), 2),
        "p50": round(percentile(values, 0.50), 2),
        "p95": round(percentile(values, 0.95), 2),
        "p99": round(percentile(values, 0.99), 2),
    }


def latency_table(
        records: List[Dict[str, Any]],
        fields: Sequence[str],
        group_key: str = "strategy",
        group_all: str = "ALL",
) -> Dict[str, Dict[str, Any]]:
    """
    Latency percentiles per group (and overall).

    records: rows carrying the latency fields (ms)
    fields: latency field names (e.g. chunking_ms, total_ms)
    Returns: {group_label: {field: {n, mean, p50, p95, p99}}}
    """
    groups: List[Tuple[str, List[Dict[str, Any]]]] = [
        (group_all, records)
    ]
    labels = sorted(
        {r.get(group_key) for r in records if r.get(group_key)}
    )
    for label in labels:
        groups.append(
            (str(label), [r for r in records if r.get(group_key) == label])
        )

    table: Dict[str, Dict[str, Any]] = {}
    for label, subset in groups:
        row: Dict[str, Any] = {group_key: label}
        for field in fields:
            values = [
                float(r[field]) for r in subset if r.get(field) is not None
            ]
            row[field] = latency_percentiles(values)
        table[label] = row
    return table


def bootstrap_ci(
        values: Sequence[float],
        ci: float = 0.95,
        n_boot: int = 1000,
        seed: int = 42
) -> Tuple[float, float]:
    """
    Confidence interval for the mean via bootstrap
    (resampling with replacement, deterministic seed).
    """
    if not values:
        return (0.0, 0.0)
    n = len(values)
    if n == 1:
        v = float(values[0])
        return (v, v)

    rng = random.Random(seed)
    boot_means = []
    for _ in range(n_boot):
        sample_sum = 0.0
        for _ in range(n):
            sample_sum += values[rng.randrange(n)]
        boot_means.append(sample_sum / n)

    boot_means.sort()
    alpha = (1.0 - ci) / 2.0
    lo = boot_means[int(alpha * n_boot)]
    hi = boot_means[min(int((1.0 - alpha) * n_boot), n_boot - 1)]
    return (float(lo), float(hi))


def wilcoxon_test(a: Sequence[float], b: Sequence[float]) -> Dict[str, Any]:
    """
    Wilcoxon test (paired per document).
    a, b: metric values for two strategies over the same set of
    documents (joined by the 'source' field).
    """
    if len(a) != len(b):
        raise ValueError(
            f"Nierówne długości par: {len(a)} vs {len(b)} "
            f"(test parametryczny wymaga par per dokument)"
        )
    try:
        res = stats.wilcoxon(list(a), list(b))
        return {
            "statistic": float(res.statistic),
            "p_value": float(res.pvalue),
        }
    except ValueError:
        # all differences are zero
        return {"statistic": 0.0, "p_value": 1.0, "note": "all differences are zero"}


def _paired_values(
        records: List[Dict[str, Any]],
        strategy_a: str,
        strategy_b: str,
        metric: str
) -> Tuple[List[float], List[float]]:
    """Pairs of metric values (a, b) joined by 'source'."""
    by_source_a = {r.get("source"): r.get(metric) for r in records
                   if r.get("strategy") == strategy_a}
    by_source_b = {r.get("source"): r.get(metric) for r in records
                   if r.get("strategy") == strategy_b}

    a: List[float] = []
    b: List[float] = []
    for source in sorted(set(by_source_a) & set(by_source_b)):
        va, vb = by_source_a[source], by_source_b[source]
        if va is not None and vb is not None:
            a.append(float(va))
            b.append(float(vb))
    return a, b


def summary_table(
        records: List[Dict[str, Any]],
        metric: str,
        ci: float = 0.95,
        n_boot: int = 1000
) -> Dict[str, Any]:
    """
    Per-strategy metric summary + Wilcoxon comparisons.

    Args:
        records: records from get_chunking_metrics_manual()
        metric: metric name (key in the record, e.g. "coherence")
        ci: bootstrap confidence level (default 0.95)
        n_boot: number of bootstrap iterations

    Returns:
        dict: {metric, strategies: {...}, wilcoxon: {...}}
    """
    strategies: Dict[str, Any] = {}
    names = sorted({r.get("strategy") for r in records if r.get("strategy")})

    for name in names:
        values = [
            float(r[metric]) for r in records
            if r.get("strategy") == name and r.get(metric) is not None
        ]
        if not values:
            continue
        lo, hi = bootstrap_ci(values, ci=ci, n_boot=n_boot)
        strategies[name] = {
            "n": len(values),
            "mean": round(mean(values), 4),
            "std": round(std(values), 4),
            "ci_low": round(lo, 4),
            "ci_high": round(hi, 4),
        }

    wilcoxon: Dict[str, Any] = {}
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            a, b = _paired_values(records, names[i], names[j], metric)
            if len(a) < 2:
                continue
            key = f"{names[i]} vs {names[j]}"
            try:
                wilcoxon[key] = wilcoxon_test(a, b)
            except ValueError:
                wilcoxon[key] = {"error": "brak wspólnych par (source)"}

    return {
        "metric": metric,
        "strategies": strategies,
        "wilcoxon": wilcoxon,
    }


def export_csv(summary: Dict[str, Any], path: str) -> str:
    """Writes the per-strategy table to CSV."""
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["strategy", "n", "mean", "std", "ci_low", "ci_high"])
        for name, row in summary["strategies"].items():
            writer.writerow([
                name, row["n"], row["mean"], row["std"],
                row["ci_low"], row["ci_high"],
            ])
    return path


def to_latex_table(summary: Dict[str, Any], caption: Optional[str] = None) -> str:
    """Generates a LaTeX table (to paste into the results chapter)."""
    lines = [r"\begin{table}[H]", r"    \centering"]
    if caption:
        lines.append(f"    \\caption{{{caption}}}")
    lines.append(r"    \small")
    lines.append(r"    \begin{tabular}{@{}lrrrrr@{}}")
    lines.append(r"        \toprule")
    lines.append(
        r"        \textbf{Strategia} & \textbf{n} & \textbf{Śr.} "
        r"& \textbf{Odch.} & \textbf{CI 95\% (dolna)} "
        r"& \textbf{CI 95\% (górna)} \\"
    )
    lines.append(r"        \midrule")
    for name, row in summary["strategies"].items():
        lines.append(
            f"        {name} & {row['n']} & {row['mean']:.4f} "
            f"& {row['std']:.4f} & {row['ci_low']:.4f} & {row['ci_high']:.4f} \\\\"
        )
    lines.append(r"        \bottomrule")
    lines.append(r"    \end{tabular}")
    lines.append(r"\end{table}")
    return "\n".join(lines)
