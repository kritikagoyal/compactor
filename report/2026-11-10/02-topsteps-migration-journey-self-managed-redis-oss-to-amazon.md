# Topstep’s migration journey: Self-managed Redis OSS to Amazon ElastiCache for Valkey

- **URL:** https://aws.amazon.com/blogs/database/topsteps-migration-journey-self-managed-redis-oss-to-amazon-elasticache-for-valkey/
- **Author:** Gbeminiyi Abolarin
- **Published Date:** 2026-11-09 16:59 UTC
- **Tags:** `databases`, `kv-store`, `redis`, `sql`
- **Source:** AWS Database Blog

---

## Summary
Topstep migrated roughly 53 million keys from self-managed Redis OSS to a fully managed, Multi-AZ Amazon ElastiCache for Valkey cluster. Using RedisShake and a single Amazon Route 53 DNS change, the team completed a blue/green cutover in seconds with no application code changes beyond a small TLS configuration update.
