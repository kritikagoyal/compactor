# Security Limits of Mining Before Validation in Nakamoto Consensus

- **URL:** https://arxiv.org/abs/2609.29222
- **Author:** Yifan Zhou, Jiang Xiao, Kaihua Qin
- **Published Date:** 2026-09-25 04:00 UTC
- **Tags:** `distributed-systems`, `research`
- **Source:** arXiv cs.DC (Distributed Computing)

---

## Summary
arXiv:2609.29222v1 Announce Type: cross Abstract: Mining before validation allows miners to extend a newly received block before completing its validity checks, giving them a head start in the race for the next block reward. This head start, however, comes with a security risk: rejecting one invalid block also discards the honest work built on it, an effect missed when validation is treated as instantaneous. We quantify this risk in a model of Nakamoto consensus with bounded network delay and a validation-time bound independent of processing load. We establish an explicit threshold on adversarial mining power below which honest miners' fully validated chains continue to grow and agree on a stable history with high probability over any fixed observation period. We also construct an attack that repeatedly draws honest mining onto invalid branches. When the adversary produces more than one block on average during the allowed validation time, the attack can eventually remove a target block at any fixed initial confirmation depth. Combined with ordinary private mining, this attack yields a matching asymptotic bound in the fully decentralized regime, where each honest miner has negligible mining power. The results show how validation latency limits the security of mining before validation, beyond the constraint imposed by network delay.
