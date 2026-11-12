# Refresh a single tenant across accounts with Aurora MySQL and Amazon S3

- **URL:** https://aws.amazon.com/blogs/database/refresh-a-single-tenant-across-accounts-with-aurora-mysql-and-amazon-s3/
- **Author:** Mansi Panchal
- **Published Date:** 2026-11-11 22:08 UTC
- **Tags:** `databases`, `kv-store`, `sql`
- **Source:** AWS Database Blog

---

## Summary
Move a single tenant's data between Amazon Aurora MySQL clusters in two separate AWS accounts with no network route between them, using Aurora cloning, SELECT INTO OUTFILE S3, and LOAD DATA FROM S3. The clusters never connect, and one encrypted Amazon S3 staging bucket is their only shared touchpoint.
