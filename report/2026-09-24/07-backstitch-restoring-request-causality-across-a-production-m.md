# Backstitch: Restoring Request Causality Across a Production Microservice Fleet

- **URL:** https://arxiv.org/abs/2609.27538
- **Author:** Ziyue Dang, Qiuyu Wu, Haoyun Xu, Tongjue Wang, Yongqing Ling, Weihao Chen, Guangming Luo
- **Published Date:** 2026-09-24 04:00 UTC
- **Tags:** `distributed-systems`, `research`
- **Source:** arXiv cs.DC (Distributed Computing)

---

## Summary
arXiv:2609.27538v1 Announce Type: new Abstract: A major video platform runs on thousands of microservices, each request propagating a context so downstream work can be traced and governed. At handoffs outside instrumented paths, e.g., custom queues and callbacks, the payload continues but the context does not, and the request still succeeds under existing tests. Such breaks are silent and widespread: 673 of 1,133 services carried at least one. Backstitch, a specialized agentic system, repairs them using the surviving execution as its reference: replay determines whether a suspicious call is request-correlated, source analysis reaches the responsible handoff, a bounded change restores its contract, and the same replay validates the fix. Repairs restore the causal chain without disturbing the work it describes: breaks at 240 of the repaired calls fell from 90.46% to 4.69%, and over 112 days the fleet's break rate more than halved.
