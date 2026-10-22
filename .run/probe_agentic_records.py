"""One-off: raw per-record llm_calls/fallbacks for agentic + E4 runs."""
import os
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

print("=== agentic E1/E2: all records (exp_id, source, llm_calls, fallbacks) ===")
cur.execute(
    "SELECT experiment_id, source, llm_calls, fallbacks, num_chunks, timestamp "
    "FROM rag_chunking_metrics_manual "
    "WHERE strategy = 'agentic' AND experiment_id NOT LIKE 'E4%%' "
    "ORDER BY experiment_id, source"
)
for eid, src, lc, fb, nc, ts in cur.fetchall():
    name = src.split("/")[-1][:30]
    print(f"  {eid[3:24]:21s} {name:30s} llm={lc!s:>6} fb={fb!s:>4} chunks={nc:>6}  {ts}")

print("\n=== E4_llm_failure: all records ===")
cur.execute(
    "SELECT experiment_id, source, llm_calls, fallbacks, num_chunks, "
    "embedding_http_requests, texts_embedded, timestamp "
    "FROM rag_chunking_metrics_manual WHERE experiment_id LIKE 'E4_llm_failure%%' "
    "ORDER BY experiment_id, source"
)
for eid, src, lc, fb, nc, ehttp, te, ts in cur.fetchall():
    name = src.split("/")[-1][:30]
    print(f"  {eid[3:24]:21s} {name:30s} llm={lc!s:>6} fb={fb!s:>4} chunks={nc:>6} "
          f"eh={ehttp} te={te}  {ts}")

print("\n=== E4_llm_failure summary per run ===")
cur.execute(
    "SELECT experiment_id, count(*), sum(COALESCE(llm_calls,0)), "
    "sum(COALESCE(fallbacks,0)), min(timestamp), max(timestamp) "
    "FROM rag_chunking_metrics_manual WHERE experiment_id LIKE 'E4_llm_failure%%' "
    "GROUP BY experiment_id ORDER BY experiment_id"
)
for r in cur.fetchall():
    print(" ", r)

print("\n=== E4_embedding_failure summary per run ===")
cur.execute(
    "SELECT experiment_id, count(*), sum(COALESCE(fallbacks,0)), "
    "sum(COALESCE(texts_embedded,0)), sum(COALESCE(embedding_http_requests,0)), "
    "min(timestamp), max(timestamp) "
    "FROM rag_chunking_metrics_manual WHERE experiment_id LIKE 'E4_embedding_failure%%' "
    "GROUP BY experiment_id ORDER BY experiment_id"
)
for r in cur.fetchall():
    print(" ", r)

print("\n=== distinct source documents ===")
cur.execute("SELECT DISTINCT source FROM rag_chunking_metrics_manual ORDER BY source")
for (s,) in cur.fetchall():
    print("  ", s)
conn.close()
