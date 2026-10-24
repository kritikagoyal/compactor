# Origin Range Requests: Serving large files without range-request tuning

- **URL:** https://blog.cloudflare.com/origin-range-requests/
- **Author:** Matthew Gumport
- **Published Date:** 2026-10-23 18:22 UTC
- **Tags:** `distributed-systems`, `infrastructure`
- **Source:** Cloudflare Technical Blog

---

## Summary
Naive byte-range caching can waste gigabytes of origin bandwidth on small requests. We rebuilt our cache architecture in Pingora to coordinate partial fetches automatically, cutting R2 p99 latency in half.
