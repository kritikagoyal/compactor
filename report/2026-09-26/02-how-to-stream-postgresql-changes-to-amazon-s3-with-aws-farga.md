# How to stream PostgreSQL changes to Amazon S3 with AWS Fargate

- **URL:** https://aws.amazon.com/blogs/database/how-to-stream-postgresql-changes-to-amazon-s3-with-aws-fargate/
- **Author:** Ramdas Gutlapalli
- **Published Date:** 2026-09-25 16:25 UTC
- **Tags:** `databases`, `kv-store`, `sql`
- **Source:** AWS Database Blog

---

## Summary
In this post, we show you how to build a fully managed, event-driven change data capture (CDC) pipeline. It streams row-level changes from Amazon RDS for PostgreSQL or Amazon Aurora PostgreSQL to Amazon S3 in near real time. You deploy the entire pipeline with a single AWS CloudFormation template, and it can run in private subnets with no internet gateway without exposing resources to the public internet.
