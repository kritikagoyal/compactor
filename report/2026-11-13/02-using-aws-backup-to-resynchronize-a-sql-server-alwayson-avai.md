# Using AWS Backup to resynchronize a SQL Server AlwaysOn Availability Group

- **URL:** https://aws.amazon.com/blogs/database/using-aws-backup-to-resynchronize-a-sql-server-alwayson-availability-group/
- **Author:** Gabriel Pereira
- **Published Date:** 2026-11-12 18:37 UTC
- **Tags:** `databases`, `kv-store`, `sql`
- **Source:** AWS Database Blog

---

## Summary
Learn how to use AWS Backup to rebuild a failed secondary replica in a SQL Server AlwaysOn Availability Group on Amazon EC2. We walk through capturing an application-consistent snapshot, restoring the EC2 instance, rejoining the Availability Group, and handling a broken LSN chain to reduce recovery time compared to a manual backup and restore.
