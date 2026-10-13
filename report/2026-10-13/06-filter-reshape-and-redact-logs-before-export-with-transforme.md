# Filter, reshape, and redact logs before export with Transformers

- **URL:** https://blog.cloudflare.com/transformers-on-logpush/
- **Author:** Sahidya Devadoss
- **Published Date:** 2026-10-12 14:44 UTC
- **Tags:** `distributed-systems`, `infrastructure`, `sql`
- **Source:** Cloudflare Technical Blog

---

## Summary
Logpush now supports Transformers, allowing teams to filter, redact, and reshape log streams using SQL before export. Powered by Apache DataFusion and Apache Arrow, Transformers apply those changes directly to log data before it reaches the destination.
