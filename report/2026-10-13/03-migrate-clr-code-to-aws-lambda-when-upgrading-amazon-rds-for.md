# Migrate CLR code to AWS Lambda when upgrading Amazon RDS for SQL Server to 2025

- **URL:** https://aws.amazon.com/blogs/database/migrate-clr-code-to-aws-lambda-when-upgrading-amazon-rds-for-sql-server-to-2025/
- **Author:** Raunak Gupta
- **Published Date:** 2026-10-12 16:11 UTC
- **Tags:** `databases`, `kv-store`, `sql`
- **Source:** AWS Database Blog

---

## Summary
After upgrading Amazon RDS for SQL Server to 2017 or later, CLR strict security leaves user-defined CLR assemblies unusable. This post shows how to migrate CLR logic with no native T-SQL equivalent to an AWS Lambda function, invoked from SQL Server 2025 through sp_invoke_external_rest_endpoint behind Amazon API Gateway.
