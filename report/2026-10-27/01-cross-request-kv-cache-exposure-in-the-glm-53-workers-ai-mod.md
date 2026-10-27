# Cross-request KV cache exposure in the GLM-5.3 Workers AI model, and our remediation with SGLang

- **URL:** https://blog.cloudflare.com/kv-cache-exposure-remediation/
- **Author:** Michelle Chen
- **Published Date:** 2026-10-26 22:01 UTC
- **Tags:** `distributed-systems`, `infrastructure`
- **Source:** Cloudflare Technical Blog

---

## Summary
A configuration mismatch in GLM 5.3 on Workers AI triggered an SGLang bug that exposed KV cache pages across requests. Here is how we addressed the issue.
