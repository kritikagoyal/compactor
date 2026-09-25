# Weave: Fine-Grained Dynamic SM Scheduling in an MoE Megakernel for Compute-Communication Overlap

- **URL:** https://arxiv.org/abs/2609.21483
- **Author:** Ziyu Huang, Yangjie Zhou, Chenhao Zhu, Yu Peng, Zihan Liu, Jinyu Liu, Shulai Zhang, Xingxun Tang, Hongzhe Yan, Xinhao Luo, Minyi Guo, Xiu Lin, Yinghao Yu, Guodong Yang, Liping Zhang, Shixuan Sun, Jingwen Leng
- **Published Date:** 2026-09-25 04:00 UTC
- **Tags:** `distributed-systems`, `research`
- **Source:** arXiv cs.DC (Distributed Computing)

---

## Summary
arXiv:2609.21483v2 Announce Type: replace Abstract: Mixture-of-Experts (MoE) inference under expert parallelism (EP) turns each MoE layer into a distributed computation with costly dispatch and combine communication. State-of-the-art systems reduce this cost through communication-computation overlap, splitting the GPU's SMs for communication and computation respectively. However, this approach still leaves GPU resources wasted along two dimensions. Spatially, the best SM split is determined by each layer's routing result and varies across layers and GPUs, so fixed policies mismatch the workload and waste either NVLink bandwidth or compute throughput. Temporally, complex MoE data dependencies introduce bubbles that leave SMs idle. We present Weave, to our knowledge the first MoE overlap system that performs fine-grained dynamic SM scheduling - deciding per layer and per GPU by routing results at runtime. Once routing completes, each layer's communication and computation volumes become known; Weave exploits this predictability through a lightweight cost model running inside the persistent megakernel: a spatial scheduler partitions SMs into communication workers and computation workers to match the communication/computation throughput ratio, and a temporal scheduler coordinates the two worker groups to minimize SM idleness. On 4x H100 SXM GPUs across six mainstream MoE models, Weave achieves a 2.89x geometric-mean MoE-layer speedup and a 1.33x geometric-mean end-to-end speedup over five state-of-the-art baselines.
