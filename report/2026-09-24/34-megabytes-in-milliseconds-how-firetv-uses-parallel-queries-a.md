# Megabytes in milliseconds: How FireTV uses parallel queries and vertical partitioning to serve millions of customers in Amazon DynamoDB

- **URL:** https://aws.amazon.com/blogs/database/megabytes-in-milliseconds-how-firetv-uses-parallel-queries-and-vertical-partitioning-to-serve-millions-of-customers-in-amazon-dynamodb/
- **Author:** Mohit Agarwal
- **Published Date:** 2026-09-23 18:56 UTC
- **Tags:** `databases`, `kafka`, `kv-store`, `sql`
- **Source:** AWS Database Blog

---

## Summary
How Amazon FireTV redesigned its Continue Watching watch-progress data model on Amazon DynamoDB with vertical partitioning and hash-prefixed sort keys for parallel reads, removing item-size limits, cutting write costs by 97%, and keeping reads under 50 milliseconds at any profile size.
