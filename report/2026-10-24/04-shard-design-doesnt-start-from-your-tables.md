# Shard design doesn't start from your tables

- **URL:** https://planetscale.com/blog/shard-groups-the-unit-of-co-location
- **Author:** Rohit Nayak
- **Published Date:** 2026-10-23 00:00 UTC
- **Tags:** `databases`, `mysql`, `scaling`
- **Source:** PlanetScale Blog

---

## Summary
Shard group design starts from your queries, not your tables. Find the key that your most important queries and transactions share, and put every table that carries that key in one group.
