# How we halved DNS build delay and cut memory use by 85%

- **URL:** https://blog.cloudflare.com/dns-targeted-zone-builds/
- **Author:** Alex Fattouche
- **Published Date:** 2026-11-02 14:00 UTC
- **Tags:** `distributed-systems`, `infrastructure`
- **Source:** Cloudflare Technical Blog

---

## Summary
Zone setting changes used to rebuild entire DNS zones, even ones with tens of millions of records. Here is how we built a planner that picks the smallest safe build, cutting full builds by 40%, peak memory by 85%, and halving build delay.
