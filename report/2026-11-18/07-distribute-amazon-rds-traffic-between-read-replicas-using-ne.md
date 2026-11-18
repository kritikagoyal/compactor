# Distribute Amazon RDS traffic between read replicas using Network Load Balancer

- **URL:** https://aws.amazon.com/blogs/database/distribute-amazon-rds-traffic-between-read-replicas-using-network-load-balancer/
- **Author:** Vijay Chakraborty
- **Published Date:** 2026-11-17 15:51 UTC
- **Tags:** `databases`, `kv-store`, `sql`
- **Source:** AWS Database Blog

---

## Summary
Learn how to put Amazon RDS read replicas behind a Network Load Balancer with health-aware, Availability Zone affinity routing. An AWS Lambda function keeps the load balancer target group in sync with replica IP addresses, giving clients a single stable endpoint over Direct Connect or Site-to-Site VPN without AWS PrivateLink overhead.
