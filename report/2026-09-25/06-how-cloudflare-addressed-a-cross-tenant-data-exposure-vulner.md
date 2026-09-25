# How Cloudflare addressed a cross-tenant data exposure vulnerability in Containers

- **URL:** https://blog.cloudflare.com/containers-cross-tenant-vulnerability/
- **Author:** Hrushikesh Deshpande
- **Published Date:** 2026-09-24 15:00 UTC
- **Tags:** `distributed-systems`, `docker`, `infrastructure`
- **Source:** Cloudflare Technical Blog

---

## Summary
External security researchers at Accomplish identified a vulnerability in Cloudflare Containers that could expose residual disk data from previous workloads. We explain how the issue worked, how we investigated it, and the steps we took to remediate it.
