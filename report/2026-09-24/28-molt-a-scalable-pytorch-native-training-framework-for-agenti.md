# Molt: A Scalable PyTorch-Native Training Framework for Agentic Reinforcement Learning

- **URL:** https://arxiv.org/abs/2607.21653
- **Author:** Jian Hu, Huiying Li, Hao Zhang, Binfeng Xu, Yifan Zhang, Shaokun Zhang, Hemil Desai, Michael Demoret, Pavlo Molchanov, Jan Kautz, Yi Dong
- **Published Date:** 2026-09-24 04:00 UTC
- **Tags:** `databases`, `distributed-systems`, `research`
- **Source:** arXiv cs.DC (Distributed Computing)

---

## Summary
arXiv:2607.21653v3 Announce Type: replace-cross Abstract: Agentic reinforcement learning requires rapid experimentation with agents and learning algorithms, yet large policies and long, multimodal trajectories demand substantial distributed infrastructure. We present MOLT, a lightweight, PyTorch- and Hugging Face-native framework that brings these goals together through four contributions. MOLT combines direct loading of Hugging Face models with experimentally validated trillion-parameter scalability in approximately 9.2K lines of framework code. Unified OpenAI- and Anthropic-compatible interfaces integrate existing agents with automatic handling of context compaction. Fully asynchronous training overlaps agent rollouts and policy optimization, accommodating variable agent execution times. Distributed experience storage removes centralized rollout-memory bottlenecks for long, multimodal trajectories. We experimentally validate the complete RL training pipeline on a one-trillion-parameter policy and demonstrate sustained learning with a 30B mixture-of-experts agent, establishing MOLT as a lightweight foundation for large-scale agentic RL research.
