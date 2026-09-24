# Aspen: Making Leaderless BFT Fast Paths Practical with Synchronized Clocks

- **URL:** https://arxiv.org/abs/2601.03390
- **Author:** Daniel Qian, Xiyu Hao, Jinkun Geng, Yuncheng Yao, Aurojit Panda, Jinyang Li, Anirudh Sivaraman
- **Published Date:** 2026-09-24 04:00 UTC
- **Tags:** `distributed-systems`, `research`
- **Source:** arXiv cs.DC (Distributed Computing)

---

## Summary
arXiv:2601.03390v3 Announce Type: replace Abstract: No Byzantine Fault Tolerant (BFT) protocol can commit a request in less than the single round trip it takes for clients to reach the replicas and hear back. Some protocols approach this bound with a leaderless, speculative fast path, where clients broadcast requests directly to replicas and commit in two message delays (). However, such a fast path is extremely fragile: when clients submit requests concurrently, replicas receive them in different orders and end up in different states, forcing the protocol into costly recovery. This paper presents Aspen, a leaderless speculative BFT protocol that can maintain its fast path even while clients submit requests concurrently, at a near-optimal latency of . The term is a short waiting delay that Aspen adds to give requests a best-effort, tentative initial order using loosely synchronized clocks and network delay estimates. Since real networks are not perfectly predictable, Aspen also tolerates replicas diverging: it adds extra replicas () so that the fast path survives up to diverged replicas, a lightweight alignment subprotocol that returns those replicas to the fast path in the background, and a repair subprotocol that restores agreement when too many diverge. In experiments with geo-distributed replicas, Aspen reduces the latency of requests by -- compared to state-of-the-art BFT protocols, while maintaining throughput matching or exceeding throughput-optimized designs.
