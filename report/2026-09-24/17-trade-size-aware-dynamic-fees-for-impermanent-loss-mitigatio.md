# Trade-Size-Aware Dynamic Fees for Impermanent Loss Mitigation in AMMs

- **URL:** https://arxiv.org/abs/2609.27937
- **Author:** Anton Ledrov, Ignat Melnikov, Irina Lebedeva, Dmitrii Umnov, George Ovchinnikov, Yury Yanovich
- **Published Date:** 2026-09-24 04:00 UTC
- **Tags:** `distributed-systems`, `research`
- **Source:** arXiv cs.DC (Distributed Computing)

---

## Summary
arXiv:2609.27937v1 Announce Type: cross Abstract: Automated Market Makers enable decentralized trading but systematically expose liquidity providers to impermanent loss through arbitrage-driven rebalancing. While dynamic fee mechanisms offer a promising mitigation strategy, existing approaches remain largely reactive, adjusting costs based on historical signals rather than explicitly linking them to the structural risk imposed by individual trades. To address this limitation, we propose a novel fee formation framework built on three core innovations. First, we introduce a coupled market maker architecture in which fee dynamics are governed by a secondary invariant, allowing liquidity state and transaction costs to evolve jointly. Second, we develop an impermanent-loss trimming fee model that adaptively increases transaction costs for trades exceeding the liquidity providers' profitable region, effectively offsetting losses from large arbitrage executions while preserving baseline fees for smaller transactions. Third, we establish a unified evaluation methodology using performance profiles to systematically compare fee algorithms across diverse market conditions. By extending a heterogeneous trader model to derive optimal arbitrage strategies under state-dependent fees, we conduct extensive simulations on historical data spanning four distinct market regimes and three token pair categories. Our results demonstrate that the proposed fee enhancements improve liquidity provider yields by 6--24% in volatile markets and up to 119% in calm regimes, while maintaining uninformed user participation and reducing informed arbitrage profitability by 3--10%. Performance profile analysis confirms that ILT-enhanced algorithms dominate baseline counterparts across 60--75% of test scenarios.
