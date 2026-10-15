# Inside Hyperdrive: How we solved a rare Hyperdrive MySQL caching bug

- **URL:** https://blog.cloudflare.com/hyperdrive-mysql/
- **Author:** Pranoy Dutta
- **Published Date:** 2026-10-14 13:00 UTC
- **Tags:** `distributed-systems`, `infrastructure`, `sql`
- **Source:** Cloudflare Technical Blog

---

## Summary
While adding MySQL support to Hyperdrive, we found a subtle protocol bug when caching query results. Here is how we tracked down a 0.001% rate error and made Hyperdrive MySQL generally available.
