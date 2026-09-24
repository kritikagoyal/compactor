# Scheduling Coflows in Multi-Core OCS Networks with Performance Guarantee

- **URL:** https://arxiv.org/abs/2604.08242
- **Author:** Xin Wang, Hong Shen, Hui Tian, Dong Wang
- **Published Date:** 2026-09-24 04:00 UTC
- **Tags:** `distributed-systems`, `research`
- **Source:** arXiv cs.DC (Distributed Computing)

---

## Summary
arXiv:2604.08242v5 Announce Type: replace Abstract: The coflow abstraction captures application-level communication patterns and enables coordinated scheduling of parallel flows to reduce job completion times in distributed systems. Modern data center networks (DCNs) are employing multiple independent optical circuit switching (OCS) cores operating concurrently to meet the massive bandwidth demands of application jobs. However, existing coflow scheduling research primarily focuses on the single-core setting, while studies of multi-core fabrics have largely considered electrical packet switching (EPS) networks. To address this gap, this paper studies the coflow scheduling problem in multi-core OCS networks under the not-all-stop reconfiguration model, in which the reconfiguration of one circuit does not interrupt other circuits. The challenges stem from two aspects: (i) cross-core coupling induced by traffic assignment across heterogeneous cores; and (ii) per-core OCS scheduling constraints, namely port exclusivity and reconfiguration delay. We propose an approximation algorithm that jointly integrates cross-core flow assignment and per-core circuit scheduling to minimize the total weighted coflow completion time (CCT) and establish a provable worst-case performance guarantee. Furthermore, our algorithm framework can be applied to the multi-core EPS scenario with a corresponding approximation guarantee for packet-switched fabrics. Trace-driven simulations using real Facebook workloads demonstrate that our algorithm can reduce the total weighted CCT and tail CCT.
