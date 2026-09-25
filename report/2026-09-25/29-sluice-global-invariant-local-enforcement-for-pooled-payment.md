# Sluice: Global Invariant, Local Enforcement for Pooled Payment-Channel Liquidity

- **URL:** https://arxiv.org/abs/2609.29975
- **Author:** Yueqi Wu, Huiping Sun, Peilu Guo, Yiming Zhu, Zhong Chen
- **Published Date:** 2026-09-25 04:00 UTC
- **Tags:** `distributed-systems`, `research`
- **Source:** arXiv cs.DC (Distributed Computing)

---

## Summary
arXiv:2609.29975v1 Announce Type: cross Abstract: A routing node on the Lightning Network holds its liquidity in separate channels, so a payment can fail at a channel whose outbound balance is exhausted while the node's other channels still hold balance. Pooling the channels into one reserve fixes this only if the node's draws across all channels stay within the reserve: a global invariant that each counterparty must enforce from its own channel, with no shared counter that off-chain draws can update. A node must therefore split the reserve into per-channel quotas in advance or coordinate every draw with every counterparty. On three Lightning snapshots the advance split forfeits to of the pooling gain over unpooled channels, and the loss grows with channel count. Sluice recovers to of that loss with a nested reservation: each channel keeps an exclusive base that its counterparty checks alone, and the rest is a shared overflow drawn on with certificates from a capacity-weighted quorum of the node's counterparties. Two conflicting certificates share an honest signer, so over-drawing is prevented without a slashable stake, under a stated bound on the capacity the node controls in the signing set. Sluice loses at most points of payment success to coordination where deployed coin movers lose up to , and improves them in eleven of twelve cells when stacked on them. Re-creating every base output each epoch costs to times Lightning's on-chain bytes; re-creating only those that overflowed costs to times and keeps part of the gain.
