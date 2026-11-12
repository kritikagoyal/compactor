# Automate Aurora zero-ETL recovery after global failover

- **URL:** https://aws.amazon.com/blogs/database/automate-aurora-zero-etl-recovery-after-global-failover/
- **Author:** Aritra Biswas
- **Published Date:** 2026-11-11 16:32 UTC
- **Tags:** `databases`, `kv-store`, `sql`
- **Source:** AWS Database Blog

---

## Summary
After an Amazon Aurora Global Database switchover or failover, the Aurora zero-ETL integration with Amazon Redshift keeps referencing the former primary and stops ingesting. Learn how to automate integration recreation with Amazon EventBridge and AWS Lambda so your analytics pipeline recovers without manual intervention.
