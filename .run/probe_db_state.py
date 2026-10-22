"""One-off: inspect rag_chunking_metrics_manual state (no secrets printed)."""
import os
import re
from collections import Counter, defaultdict

from dotenv import load_dotenv
import psycopg2

load_dotenv()
conn = psycopg2.connect(
    host=os.getenv("METRICS_DB_HOST", "localhost"),
    port=int(os.getenv("METRICS_DB_PORT", "5432")),
    dbname=os.getenv("METRICS_DB_NAME", "rag_metrics"),
    user=os.getenv("METRICS_DB_USER", "postgres"),
    password=os.getenv("METRICS_DB_PASSWORD", ""),
)
cur = conn.cursor()

# total
cur.execute("SELECT count(*), min(timestamp), max(timestamp) FROM rag_chunking_metrics_manual")
total, tmin, tmax = cur.fetchone()
print(f"TOTAL: {total}  | min_ts={tmin}  max_ts={tmax}")

# per experiment_id (strip trailing _YYYYmmdd_HHMMSS stamp)
cur.execute(
    "SELECT experiment_id, count(*), min(timestamp), max(timestamp) "
    "FROM rag_chunking_metrics_manual GROUP BY experiment_id ORDER BY experiment_id"
)
rows = cur.fetchall()
print(f"\nDISTINCT experiment_ids: {len(rows)}")
grouped = Counter()
for eid, n, a, b in rows:
    base = re.sub(r"_\d{8}_\d{6}$", "", eid)
    grouped[base] += n
    print(f"  {eid:60s} n={n:4d}  [{a} .. {b}]")

print("\nGROUPED (config -> runs):")
for base, n in sorted(grouped.items()):
    print(f"  {base:45s} records={n} (runs={n/13:.0f})")

# sanity: llm_calls for agentic non-fault runs
print("\nLLM_CALLS per strategy (non-fault), per document:")
cur.execute(
    "SELECT strategy, source, sum(COALESCE(llm_calls,0)), max(llm_calls), "
    "sum(COALESCE(fallbacks,0)), count(*) "
    "FROM rag_chunking_metrics_manual "
    "WHERE experiment_id NOT LIKE 'E4%%' GROUP BY strategy, source ORDER BY strategy, source"
)
agg = defaultdict(lambda: [0, 0, 0])
for strat, src, s, m, fb, n in cur.fetchall():
    agg[strat][0] += s or 0
    agg[strat][1] = max(agg[strat][1], m or 0)
    agg[strat][2] += fb or 0
for strat, (s, m, fb) in sorted(agg.items()):
    print(f"  {strat:18s} sum_llm_calls={s:6d}  max_llm_calls={m:4d}  sum_fallbacks={fb}")

# E4 detail
print("\nE4 runs (per experiment, per doc):")
cur.execute(
    "SELECT experiment_id, source, num_chunks, llm_calls, fallbacks, "
    "embedding_http_requests, texts_embedded, coherence, coverage "
    "FROM rag_chunking_metrics_manual WHERE experiment_id LIKE 'E4%%' "
    "ORDER BY experiment_id, source"
)
for eid, src, nc, lc, fb, ehttp, te, coh, cov in cur.fetchall():
    name = src.split("/")[-1][:28]
    print(f"  {eid[:58]:58s} {name:28s} chunks={nc:5d} llm={lc} fb={fb} "
          f"eh={ehttp} te={te} coh={coh} cov={cov}")

# config sanity: chunk_size/overlap distribution for E3
print("\nE3 configs present (strategy, size, overlap -> records):")
cur.execute(
    "SELECT strategy, chunk_size, chunk_overlap, count(*) FROM rag_chunking_metrics_manual "
    "WHERE experiment_id LIKE 'E3%%' GROUP BY 1,2,3 ORDER BY 1,2,3"
)
for strat, sz, ov, n in cur.fetchall():
    print(f"  {strat:15s} size={sz:5d} overlap={ov:4d}  n={n}")

conn.close()
