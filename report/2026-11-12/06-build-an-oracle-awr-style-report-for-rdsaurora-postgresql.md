# Build an Oracle AWR-style report for RDS/Aurora PostgreSQL

- **URL:** https://aws.amazon.com/blogs/database/build-an-oracle-awr-style-report-for-rds-aurora-postgresql/
- **Author:** Tushar Rajput
- **Published Date:** 2026-11-11 18:20 UTC
- **Tags:** `databases`, `kv-store`, `sql`
- **Source:** AWS Database Blog

---

## Summary
PostgreSQL has no built-in Oracle AWR equivalent. This post shows how to build an AWR-style, snapshot-based performance report for Amazon RDS for PostgreSQL and Amazon Aurora PostgreSQL using pg_stat_statements and pg_cron, producing top-SQL, database-activity, wait-event, and load-profile reports between any two snapshot IDs, entirely in SQL.
