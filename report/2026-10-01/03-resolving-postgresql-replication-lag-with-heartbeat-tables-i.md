# Resolving PostgreSQL replication lag with heartbeat tables in change data capture scenarios

- **URL:** https://aws.amazon.com/blogs/database/resolving-postgresql-replication-lag-with-heartbeat-tables-in-change-data-capture-scenarios/
- **Author:** Donghua Luo
- **Published Date:** 2026-09-30 16:47 UTC
- **Tags:** `databases`, `distributed-systems`, `kv-store`, `sql`
- **Source:** AWS Database Blog

---

## Summary
Replication lag during a change data capture (CDC) migration can be counterintuitive: the source is busy, yet replication falls behind and WAL piles up. This post shows how to resolve PostgreSQL replication lag with heartbeat tables using AWS DMS or Debezium, and how to monitor replication slot health with Amazon CloudWatch and SQL diagnostics.
