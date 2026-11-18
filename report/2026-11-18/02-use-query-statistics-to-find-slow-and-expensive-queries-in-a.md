# Use query statistics to find slow and expensive queries in Aurora DSQL

- **URL:** https://aws.amazon.com/blogs/database/use-query-statistics-to-find-slow-and-expensive-queries-in-aurora-dsql/
- **Author:** Rakesh Reddy Kondakindi
- **Published Date:** 2026-11-17 21:09 UTC
- **Tags:** `databases`, `kv-store`, `sql`
- **Source:** AWS Database Blog

---

## Summary
When a code change slows your application, Amazon Aurora DSQL query statistics help you find the slow and expensive queries behind it, down to the exact SQL statement. This post walks through a performance investigation that pinpoints a missing index, fixes it with an asynchronous index build, and measures the improvement in latency and DPU cost.
