# Performance impact of excessive logging in Amazon Aurora PostgreSQL

- **URL:** https://aws.amazon.com/blogs/database/performance-impact-of-excessive-logging-in-amazon-aurora-postgresql/
- **Author:** Baji Shaik
- **Published Date:** 2026-11-19 19:10 UTC
- **Tags:** `databases`, `kv-store`, `sql`
- **Source:** AWS Database Blog

---

## Summary
Excessive database and audit logging can quietly become a performance bottleneck in Amazon Aurora and Amazon RDS for PostgreSQL. Using a reproducible pgbench example, this post shows when logging overhead is negligible and when it cuts throughput by about three times, how to spot it with wait events and log file evidence, and how to reduce it.
