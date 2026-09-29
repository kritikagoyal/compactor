# Resolving query plan regressions after a MySQL engine upgrade

- **URL:** https://aws.amazon.com/blogs/database/resolving-query-plan-regressions-after-a-mysql-engine-upgrade/
- **Author:** CHANDANA DA
- **Published Date:** 2026-09-28 17:22 UTC
- **Tags:** `databases`, `kv-store`, `sql`
- **Source:** AWS Database Blog

---

## Summary
After a major or minor version upgrade on Amazon Aurora MySQL or Amazon RDS for MySQL, some queries regress because the optimizer's cost models, defaults, and execution strategies change. This post walks through a diagnostic workflow that traces each regression to the specific version change behind it and applies the right fix.
