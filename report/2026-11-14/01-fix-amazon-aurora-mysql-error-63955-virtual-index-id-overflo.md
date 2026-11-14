# Fix Amazon Aurora MySQL error 63955: Virtual index ID overflow

- **URL:** https://aws.amazon.com/blogs/database/fix-amazon-aurora-mysql-error-63955-virtual-index-id-overflow/
- **Author:** Kartik Saini
- **Published Date:** 2026-11-13 21:10 UTC
- **Tags:** `databases`, `kv-store`, `sql`
- **Source:** AWS Database Blog

---

## Summary
An Amazon Aurora MySQL cluster can exhaust its virtual index ID limit, after which any CREATE INDEX that includes a virtual column fails with error 63955 until you rebuild the databases. This post shows how to recognize the error, why backups cannot clear it, and how to run a logical dump-and-restore migration with monitoring to catch it next time.
