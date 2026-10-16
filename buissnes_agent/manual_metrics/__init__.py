"""
Manually-run metrics tools (research data path).

Everything in this package is OPT-IN: it is never triggered by the
normal application flow (ingestion / chat). It is run explicitly:

- run_experiments: E1-E4 experiment runner (chapter 4)
- thesis_pipeline: experiments -> statistics -> export in one go
- statistics: mean/std/bootstrap CI/Wilcoxon + CSV/LaTeX export

Runtime (automatic) metrics live elsewhere:
- buissnes_agent/evaluation/chunk_metrics.py (used by the pipeline)
- buissnes_agent/tools/rag_metrics.py (collector used by all stacks)
"""
from .statistics import (
    bootstrap_ci,
    export_csv,
    mean,
    std,
    summary_table,
    to_latex_table,
    wilcoxon_test,
)

__all__ = [
    "mean",
    "std",
    "bootstrap_ci",
    "wilcoxon_test",
    "summary_table",
    "export_csv",
    "to_latex_table",
]
