# Resource-Aware Model Selection for Scalable Indoor Localization on HPC Platforms

- **URL:** https://arxiv.org/abs/2609.29402
- **Author:** Fukuharu Tanaka, Hamada Rizk, Moustafa Youssef, Hirozumi Yamaguchi
- **Published Date:** 2026-09-25 04:00 UTC
- **Tags:** `distributed-systems`, `research`
- **Source:** arXiv cs.DC (Distributed Computing)

---

## Summary
arXiv:2609.29402v1 Announce Type: new Abstract: Large-scale indoor localization is increasingly needed in campuses, smart buildings, factories, and digital-twin infrastructures, where wireless conditions, access-point deployments, and spatial layouts evolve over time. Such systems must be accurate, extendable, and maintainable, allowing new buildings, floors, rooms, and service areas to be added without retraining a monolithic model. Modular learning-based localization supports this goal by assigning independent models to buildings, floors, and fine-grained spatial regions. However, this extendability introduces a high-performance inference challenge: each query may require selecting and executing among hundreds or thousands of local models, making exhaustive inference costly in computation, accelerator memory residency, model loading, and scheduling. This paper presents a resource-aware modular inference framework for WiFi fingerprint-based indoor localization on high-performance and distributed computing platforms. The framework organizes local autoencoder models into a building-floor-spot hierarchy and formulates localization as model selection over a large pretrained model ensemble. To reduce inference cost under resource constraints, we introduce two lightweight execution-pruning strategies: Hierarchical Candidate Pruning, which performs coarse-to-fine model selection, and Trajectory-Aware Pruning, which uses temporal locality in user movement to restrict inference to spatially plausible neighboring models. Experiments on a real-world dataset demonstrate that the proposed framework delivers scalable inference without sacrificing localization quality. Compared with exhaustive evaluation over 735 spot models, Hierarchical Candidate Pruning requires only 67 model evaluations, while Trajectory-Aware Pruning reduces this number to just 10, cutting model executions by 98.6%.
