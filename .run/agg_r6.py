"""One-off: aggregate rag_chunking_metrics_manual for the r6.tex rewrite.

- reconstructs absolute llm_calls/fallbacks for agentic rows (rows written
  before the counter fix store cross-document deltas; the true value for a
  document is the running sum of the stored deltas in timestamp order);
- computes E1 quality / E2 cost-time / E3 ablation / E4 fault stats and
  paired Wilcoxon tests (r4 methodology: bootstrap B=1000, seed 42,
  paired per document, alpha=0.05).

Prints tables; dumps .run/r6_agg.json. No secrets are printed.
"""
import json
import os
import re
import random
from collections import defaultdict

from dotenv import load_dotenv
import psycopg2
from scipy import stats as sps

load_dotenv()
conn = psycopg2.connect(
    host=os.getenv("METRICS_DB_HOST", "localhost"),
    port=int(os.getenv("METRICS_DB_PORT", "5432")),
    dbname=os.getenv("METRICS_DB_NAME", "rag_metrics"),
    user=os.getenv("METRICS_DB_USER", "postgres"),
    password=os.getenv("METRICS_DB_PASSWORD", ""),
)
cur = conn.cursor()

COLS = ["experiment_id", "strategy", "source", "num_chunks",
        "avg_chunk_len", "std_chunk_len", "empty_chunks",
        "too_short_chunks", "over_limit_chunks", "over_limit_ratio",
        "coverage", "coherence", "embedding_http_requests",
        "texts_embedded", "llm_calls", "fallbacks",
        "chunking_ms", "embedding_ms", "storage_ms", "total_ms",
        "timestamp"]
cur.execute("SELECT " + ", ".join(COLS) + " FROM rag_chunking_metrics_manual")
recs = [dict(zip(COLS, row)) for row in cur.fetchall()]
conn.close()

for r in recs:
    r["cfg"] = re.sub(r"_\d{8}_\d{6}$", "", r["experiment_id"])
    r["stamp"] = r["experiment_id"][len(r["cfg"]) + 1:]

# run ordinal per config (each config was run twice)
run_min = defaultdict(lambda: defaultdict(lambda: None))
for r in recs:
    t = run_min[r["cfg"]][r["stamp"]]
    if t is None or r["timestamp"] < t:
        run_min[r["cfg"]][r["stamp"]] = r["timestamp"]
run_rank = {}
for cfg, by_stamp in run_min.items():
    for i, s in enumerate(sorted(by_stamp, key=by_stamp.get)):
        run_rank[(cfg, s)] = i
for r in recs:
    r["run"] = run_rank[(r["cfg"], r["stamp"])]

# --- reconstruct absolute strategy counters for agentic rows
runs = defaultdict(list)
for r in recs:
    runs[(r["cfg"], r["stamp"])].append(r)
for rs in runs.values():
    rs.sort(key=lambda r: (r["timestamp"], r["source"]))
    if rs[0]["strategy"] == "agentic":
        a_l = a_f = 0
        for r in rs:
            a_l += r["llm_calls"] or 0
            a_f += r["fallbacks"] or 0
            r["llm_abs"], r["fb_abs"] = a_l, a_f
    else:
        for r in rs:
            r["llm_abs"] = r["llm_calls"] or 0
            r["fb_abs"] = r["fallbacks"] or 0

# --- stats helpers
def mean(v):
    return sum(v) / len(v)

def std(v):
    m = mean(v)
    return (sum((x - m) ** 2 for x in v) / (len(v) - 1)) ** 0.5

def boot_ci(v, B=1000, seed=42):
    rnd = random.Random(seed)
    n = len(v)
    means = sorted(sum(rnd.choice(v) for _ in range(n)) / n for _ in range(B))
    return means[24], means[974]

def pct(v, p):
    s = sorted(v)
    k = (len(s) - 1) * p / 100.0
    f = int(k)
    c = min(f + 1, len(s) - 1)
    return s[f] + (s[c] - s[f]) * (k - f)

def stat3(v):
    m = mean(v)
    s = std(v)
    lo, hi = boot_ci(v)
    return {"mean": round(m, 4), "std": round(s, 4),
            "ci_lo": round(lo, 4), "ci_hi": round(hi, 4)}

def fmt3(v, nd=4):
    d = stat3(v)
    return (f"{d['mean']:.{nd}f} ± {d['std']:.{nd}f} "
            f"[{d['ci_lo']:.{nd}f}; {d['ci_hi']:.{nd}f}]")

def wilcox(a, b):
    try:
        return sps.wilcoxon(a, b).pvalue
    except ValueError:
        return None  # no non-zero differences

def paired(cfg_a, cfg_b, metric):
    da, db = {}, {}
    for r in recs:
        if r["cfg"] == cfg_a:
            da[(r["run"], r["source"])] = r[metric]
        elif r["cfg"] == cfg_b:
            db[(r["run"], r["source"])] = r[metric]
    common = sorted(set(da) & set(db))
    return [da[k] for k in common], [db[k] for k in common], len(common)

out = {"n_records": len(recs), "n_configs": len(run_min),
       "n_runs": sum(len(v) for v in run_min.values())}
print(f"records: {len(recs)} | configs: {len(run_min)} "
      f"| runs: {sum(len(v) for v in run_min.values())}")
print("configs:")
for cfg in sorted(run_min):
    print(f"   {cfg:45s} runs={len(run_min[cfg])} "
          f"records={sum(1 for r in recs if r['cfg'] == cfg)}")

# ---------------- E1: quality ----------------
STRATS = ["agentic", "fixedSize", "sentenceBased", "semanticChunker"]
e1cfg = {s: f"E1_{s}_600_100" for s in STRATS}
print("\n=== E1 quality (per strategy; 2 runs x 13 docs = 26 records) ===")
e1_out = {}
for s in STRATS:
    rs = [r for r in recs if r["cfg"] == e1cfg[s]]
    print(f"\n-- {s}")
    row = {"n": len(rs)}
    for k in ("num_chunks", "avg_chunk_len", "std_chunk_len",
              "over_limit_ratio", "too_short_chunks", "coverage",
              "coherence"):
        vals = [r[k] for r in rs if r[k] is not None]
        row[k] = stat3(vals)
        print(f"   {k:18s} {fmt3(vals)}")
    for run_i in (0, 1):
        rr = [r for r in rs if r["run"] == run_i]
        pr = {
            "chunks": sum(r["num_chunks"] for r in rr),
            "texts_embedded": sum(r["texts_embedded"] for r in rr),
            "http_requests": sum(r["embedding_http_requests"] for r in rr),
            "llm_calls": sum(r["llm_abs"] for r in rr),
            "fallbacks": sum(r["fb_abs"] for r in rr),
            "total_ms_sum": round(sum(r["total_ms"] for r in rr)),
        }
        row[f"run{run_i}_totals"] = pr
        print(f"   run{run_i}: {pr}")
    e1_out[s] = row

# ---------------- E2: cost & time ----------------
e2cfg = {s: f"E2_{s}_600_100" for s in STRATS}
print("\n=== E2 cost/time (per strategy; 26 records) ===")
e2_out = {}
for s in STRATS:
    rs = [r for r in recs if r["cfg"] == e2cfg[s]]
    print(f"\n-- {s}")
    row = {"n": len(rs)}
    for k in ("chunking_ms", "embedding_ms", "storage_ms", "total_ms"):
        vals = [r[k] for r in rs]
        row[k] = {"mean": round(mean(vals), 1), "std": round(std(vals), 1),
                  "p50": round(pct(vals, 50), 1), "p95": round(pct(vals, 95), 1)}
        s0 = sum(r[k] for r in rs if r["run"] == 0) / 1000
        s1 = sum(r[k] for r in rs if r["run"] == 1) / 1000
        print(f"   {k:14s} mean={mean(vals):10.1f} p50={pct(vals, 50):10.1f} "
              f"p95={pct(vals, 95):12.1f}  (sum/run: {s0:.1f} s / {s1:.1f} s)")
    for run_i in (0, 1):
        rr = [r for r in rs if r["run"] == run_i]
        pr = {
            "texts_embedded": sum(r["texts_embedded"] for r in rr),
            "http_requests": sum(r["embedding_http_requests"] for r in rr),
            "llm_calls": sum(r["llm_abs"] for r in rr),
            "fallbacks": sum(r["fb_abs"] for r in rr),
            "total_ms_sum": round(sum(r["total_ms"] for r in rr)),
        }
        row[f"run{run_i}_totals"] = pr
    e2_out[s] = row

# ---------------- E3: ablation ----------------
e3cfgs = sorted(c for c in run_min if c.startswith("E3_"))
print("\n=== E3 ablation (per config; 26 records) ===")
e3_out = {}
for cfg in e3cfgs:
    parts = cfg.split("_")
    s, size, ov = parts[1], int(parts[2]), int(parts[3])
    rs = [r for r in recs if r["cfg"] == cfg]
    coh = [r["coherence"] for r in rs if r["coherence"] is not None]
    d = {
        "num_chunks_per_doc": round(mean([r["num_chunks"] for r in rs]), 1),
        "avg_chunk_len": round(mean([r["avg_chunk_len"] for r in rs]), 1),
        "std_chunk_len": round(mean([r["std_chunk_len"] for r in rs]), 1),
        "over_limit_ratio": round(mean([r["over_limit_ratio"] for r in rs]), 4),
        "coverage": round(mean([r["coverage"] for r in rs]), 4),
        "coherence": round(mean(coh), 4),
        "chunking_ms": round(mean([r["chunking_ms"] for r in rs]), 0),
        "total_ms": round(mean([r["total_ms"] for r in rs]), 0),
    }
    e3_out[cfg] = d
    print(f"   {cfg:34s} chunks/doc={d['num_chunks_per_doc']:7.1f} "
          f"len={d['avg_chunk_len']:7.1f} std={d['std_chunk_len']:7.1f} "
          f"over={d['over_limit_ratio']:.4f} cov={d['coverage']:.4f} "
          f"coh={d['coherence']:.4f} tot_ms={d['total_ms']:8.0f}")

# ---------------- E4: fault resilience ----------------
print("\n=== E4 fault runs (per run; 13 docs) ===")
e4_out = {}
for cfg in sorted(c for c in run_min if c.startswith("E4_")):
    e4_out[cfg] = []
    for run_i in sorted({r["run"] for r in recs if r["cfg"] == cfg}):
        rs = [r for r in recs if r["cfg"] == cfg and r["run"] == run_i]
        coh = [r["coherence"] for r in rs if r["coherence"] is not None]
        pr = {
            "docs": len(rs),
            "llm_calls": sum(r["llm_abs"] for r in rs),
            "fallbacks": sum(r["fb_abs"] for r in rs),
            "chunks": sum(r["num_chunks"] for r in rs),
            "texts_embedded": sum(r["texts_embedded"] for r in rs),
            "http_requests": sum(r["embedding_http_requests"] for r in rs),
            "coverage": round(mean([r["coverage"] for r in rs]), 4),
            "coherence": round(mean(coh), 4) if coh else None,
            "chunking_ms": round(mean([r["chunking_ms"] for r in rs]), 0),
            "embedding_ms": round(mean([r["embedding_ms"] for r in rs]), 0),
            "total_ms": round(mean([r["total_ms"] for r in rs]), 0),
        }
        e4_out[cfg].append(pr)
        print(f"   {cfg:45s} run{run_i} {pr}")

# ---------------- Wilcoxon ----------------
print("\n=== Wilcoxon E1 (paired per doc x run) ===")
w1 = {}
for i, a in enumerate(STRATS):
    for b in STRATS[i + 1:]:
        w1[f"{a} vs {b}"] = {}
        for m in ("coherence", "coverage", "avg_chunk_len", "std_chunk_len",
                  "num_chunks", "over_limit_ratio"):
            x, y, n = paired(e1cfg[a], e1cfg[b], m)
            p = wilcox(x, y)
            w1[f"{a} vs {b}"][m] = {"p": None if p is None else round(p, 5),
                                    "n": n}
            ps = "n/a" if p is None else f"{p:.5f}"
            ns = " (n.s.)" if (p is None or p >= 0.05) else ""
            print(f"   {a:16s} vs {b:16s} {m:16s} n={n:2d} p={ps}{ns}")

print("\n=== Wilcoxon E2 (paired per doc x run) ===")
w2 = {}
for i, a in enumerate(STRATS):
    for b in STRATS[i + 1:]:
        w2[f"{a} vs {b}"] = {}
        for m in ("chunking_ms", "embedding_ms", "storage_ms", "total_ms"):
            x, y, n = paired(e2cfg[a], e2cfg[b], m)
            p = wilcox(x, y)
            w2[f"{a} vs {b}"][m] = {"p": None if p is None else round(p, 5),
                                    "n": n}
            ps = "n/a" if p is None else f"{p:.5f}"
            ns = " (n.s.)" if (p is None or p >= 0.05) else ""
            print(f"   {a:16s} vs {b:16s} {m:16s} n={n:2d} p={ps}{ns}")

out["e1"] = e1_out
out["e2"] = e2_out
out["e3"] = e3_out
out["e4"] = e4_out
out["wilcoxon_e1"] = w1
out["wilcoxon_e2"] = w2

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "r6_agg.json"), "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
print("\nwritten: .run/r6_agg.json")
