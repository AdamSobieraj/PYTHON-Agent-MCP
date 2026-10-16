"""
Chunking quality metrics (runtime, automatic).

Note: the manually-run tools (statistics, experiment runner,
thesis pipeline) have moved to buissnes_agent.manual_metrics.
The statistics names below are re-exported for backward
compatibility of old import paths.
"""
from .chunk_metrics import ChunkingQuality, compute_chunk_metrics

# Backward compatibility (moved to manual_metrics)
from buissnes_agent.manual_metrics.statistics import (
    bootstrap_ci,
    export_csv,
    mean,
    std,
    summary_table,
    to_latex_table,
    wilcoxon_test,
)

__all__ = [
    "ChunkingQuality",
    "compute_chunk_metrics",
    "mean",
    "std",
    "bootstrap_ci",
    "wilcoxon_test",
    "summary_table",
    "export_csv",
    "to_latex_table",
]
