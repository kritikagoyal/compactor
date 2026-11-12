# How Flickr modernized caching with Amazon ElastiCache for Valkey

- **URL:** https://aws.amazon.com/blogs/database/how-flickr-modernized-caching-with-amazon-elasticache-for-valkey/
- **Author:** Wilson Lam
- **Published Date:** 2026-11-11 15:54 UTC
- **Tags:** `databases`, `kv-store`, `redis`, `sql`
- **Source:** AWS Database Blog

---

## Summary
Flickr, part of SmugMug, serves over 100 million photographers. In this post, the Flickr team shares how they modernized their caching layer by migrating from Redis and Twemproxy to Amazon ElastiCache for Valkey, consolidating more than 40 clusters, enabling cluster mode and multi-AZ failover, and moving to PhpRedis, all with no end-user disruption.
