# Omni-Flow: A Unified Workflow Orchestration and Distributed KV Cache Sharing Framework for Multimodal Inference

- **URL:** https://arxiv.org/abs/2606.31093
- **Author:** Bin Xiao, Jingfu Dong, Changran Wang, Yitian Chen, Xiaoyu Zhao, Yuqi Peng, Jianping Lin, Yuchen Xie
- **Published Date:** 2026-09-25 04:00 UTC
- **Tags:** `distributed-systems`, `research`
- **Source:** arXiv cs.DC (Distributed Computing)

---

## Summary
arXiv:2606.31093v2 Announce Type: replace Abstract: Multimodal models increasingly integrate heterogeneous components, from encoders and LLMs to diffusion models and media decoders. Serving these models efficiently requires flexible workflow orchestration, independent component scheduling, and cross-component state sharing. However, existing multimodal frameworks primarily organize execution as stage-level pipelines, while state ownership remains largely stage-local. We present Omni-Flow, a distributed serving framework built around three cooperating abstractions. Control Flow defines workflows through a Python DSL, organizing heterogeneous components and their dependencies into a unified dataflow graph. The runtime uses these dependencies to determine when each component can execute. Data Flow manages the placement, transfer, and lifetime of shared tensors and paged KV caches across roles, together with same-device weight sharing. Compute Flow matches multimodal conversation histories to reuse KV across turns and integrates framework-managed KV and model-specific sampling with SGLang's execution interfaces. Omni-Flow also enables cross-role prefix-KV reuse between compatible LLM and diffusion components. Together, these abstractions separate model-specific computation from workflow coordination and state management, allowing independently executing roles to share compatible resources through a common programming model. Experiments with Qwen3-Omni show that, across four benchmarks and multiple concurrency levels, Omni-Flow's aggregate job completion time (JCT) is 1.2\% and 4.9\% higher than vLLM-Omni's and SGLang-Omni's, respectively. In a 50-turn multimodal session, Omni-Flow avoids resubmitting accumulated inputs through server-side session state, reducing mean JCT by 7.5\% and 19.3\% relative to vLLM-Omni and SGLang-Omni, respectively.
