# What gets TOASTed in Postgres

- **URL:** https://planetscale.com/blog/what-gets-toasted-in-postgres
- **Author:** Ahmed Darwich
- **Published Date:** 2026-10-12 00:00 UTC
- **Tags:** `databases`, `mysql`, `scaling`, `sql`
- **Source:** PlanetScale Blog

---

## Summary
Postgres 19 switches TOAST compression from pglz to LZ4. LZ4 is faster, but it isn't always smaller, and some reads get slower with it.
