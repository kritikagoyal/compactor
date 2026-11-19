# Validating a High-Performance Cloud Object Store with Lightweight Formal Methods

- **URL:** https://dl.acm.org/doi/10.1145/3830418.3843899
- **Author:** dl.acm.org via typesanitizer
- **Published Date:** 2026-11-19 08:53 UTC
- **Tags:** `distributed-systems`, `kubernetes`
- **Source:** Lobste.rs (Distributed Systems)

---

## Summary
Abstract: We report on our experience validating S3 Express One Zone, a high-performance Amazon S3 storage class launched in November 2023. We focused on its distributed metadata index, which implements a hierarchical namespace using distributed transactions. We check strong consistency and durability under crashes, network delays, and timeouts. Building on our prior work on lightweight formal methods, we combined executable reference models with property-based testing and stateless model checking. Applying these techniques to a production distributed system required three new techniques: a white-box approach to checking serializability; compositional validation of the data and control planes; and long-running canaries that use reference models to check correctness across deployments. We extended Shuttle, our open-source stateless checker, to support a production async Rust runtime and failure injection, including cancelled operations and timeouts. Our main finding is that this approach is sustainable at engineering scale. After launch, the engineering team took ownership of models and test infrastructure, increasing its share of validation commits from 41% to 84% and independently extending the models for conditional writes, object append, and atomic rename, with little involvement from the formal methods team. Comments
