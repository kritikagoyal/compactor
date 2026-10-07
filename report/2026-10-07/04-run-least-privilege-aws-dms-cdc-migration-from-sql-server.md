# Run least-privilege AWS DMS CDC migration from SQL Server

- **URL:** https://aws.amazon.com/blogs/database/run-least-privilege-aws-dms-cdc-migration-from-sql-server/
- **Author:** Aritra Biswas
- **Published Date:** 2026-10-06 15:29 UTC
- **Tags:** `databases`, `kv-store`, `sql`
- **Source:** AWS Database Blog

---

## Summary
Configure AWS DMS change data capture (CDC) from a self-managed SQL Server source without granting sysadmin to the endpoint login. This least-privilege pattern uses certificate-signed wrapper procedures, granular permissions, and AWS Secrets Manager to meet separation-of-duties requirements while preserving full CDC functionality.
