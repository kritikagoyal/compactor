# Improve RDS Proxy multiplexing for PostgreSQL, Part 1: Common causes

- **URL:** https://aws.amazon.com/blogs/database/improve-rds-proxy-multiplexing-for-postgresql-part-1-common-causes/
- **Author:** Pavel Rabinovich
- **Published Date:** 2026-11-13 21:08 UTC
- **Tags:** `databases`, `kv-store`, `sql`
- **Source:** AWS Database Blog

---

## Summary
RDS Proxy multiplexes many client connections across a small pool of database connections, but connection pinning, pool fragmentation, and uncommitted transactions can silently disable that benefit for PostgreSQL workloads. Part 1 shows how to recognize each condition with Amazon CloudWatch metrics and the fix that restores multiplexing.
