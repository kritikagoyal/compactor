# PostgreSQL large objects: Best practices for Amazon Aurora and RDS

- **URL:** https://aws.amazon.com/blogs/database/postgresql-large-objects-best-practices-for-amazon-aurora-and-rds/
- **Author:** Sachin Murkar
- **Published Date:** 2026-11-16 23:46 UTC
- **Tags:** `databases`, `kv-store`, `sql`
- **Source:** AWS Database Blog

---

## Summary
PostgreSQL large objects live outside your tables and are referenced only by an OID, so autovacuum never reclaims the orphans. This post shows how to monitor orphaned large objects on Amazon Aurora and Amazon RDS for PostgreSQL, run vacuumlo safely, set up lo_manage triggers, prevent OID exhaustion, and prepare for major version upgrades.
