# Automating Oracle Data Guard switchover and failover on Amazon EC2

- **URL:** https://aws.amazon.com/blogs/database/automating-oracle-data-guard-switchover-and-failover-on-amazon-ec2/
- **Author:** Sai Krishna Namburu
- **Published Date:** 2026-11-11 17:50 UTC
- **Tags:** `databases`, `kv-store`, `sql`
- **Source:** AWS Database Blog

---

## Summary
Oracle Data Guard keeps a standby database in sync for high availability and disaster recovery, but running switchover and failover by hand on Amazon EC2 is slow and error-prone. This post shows how to automate both with AWS Step Functions and AWS Lambda, running validated pre-checks, the role transition, post-checks, and RTO/RPO tracking end to end.
