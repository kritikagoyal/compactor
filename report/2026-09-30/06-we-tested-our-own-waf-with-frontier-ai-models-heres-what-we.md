# We tested our own WAF with frontier AI models. Here’s what we found

- **URL:** https://blog.cloudflare.com/adaptive-ai-waf-testing/
- **Author:** Kuber Nandwani
- **Published Date:** 2026-09-29 13:00 UTC
- **Tags:** `distributed-systems`, `infrastructure`
- **Source:** Cloudflare Technical Blog

---

## Summary
We built a WAF tester that adapted each request based on what the WAF blocked or passed. This helped us explore variations that a fixed test might miss. We ran it across six attack categories on an authorized staging environment and discovered detection gaps worth fixing. Here’s how the loop worked, what got through, and what we did about it.
