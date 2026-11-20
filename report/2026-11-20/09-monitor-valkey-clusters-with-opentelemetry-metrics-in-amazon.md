# Monitor Valkey clusters with OpenTelemetry metrics in Amazon ElastiCache

- **URL:** https://aws.amazon.com/blogs/database/monitor-valkey-clusters-with-opentelemetry-metrics-in-amazon-elasticache/
- **Author:** Paul Ross
- **Published Date:** 2026-11-19 18:39 UTC
- **Tags:** `databases`, `kv-store`, `redis`, `sql`
- **Source:** AWS Database Blog

---

## Summary
Amazon ElastiCache for Valkey now offers OpenTelemetry metrics, detailed monitoring, ElastiCache Insights, and PromQL. This post walks through one troubleshooting path: turn on detailed monitoring, find a hot shard, query with PromQL, catch a short latency spike, and create one alarm that watches every node.
