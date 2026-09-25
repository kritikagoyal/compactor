# AgileLog: A Forkable Shared Log for Agents on Data Streams

- **URL:** https://arxiv.org/abs/2604.14590
- **Author:** Shreesha G. Bhat, Tony Hong, Michael Noguera, Aishwarya Ganesan, Ramnatthan Alagappan
- **Published Date:** 2026-09-25 04:00 UTC
- **Tags:** `distributed-systems`, `research`
- **Source:** arXiv cs.DC (Distributed Computing)

---

## Summary
arXiv:2604.14590v3 Announce Type: replace Abstract: In modern data-streaming systems, alongside traditional programs, a new type of entity has emerged that can interact with streaming data: AI agents. Unlike traditional programs, AI agents use LLM reasoning to accomplish high-level tasks specified in natural language over streaming data. Unfortunately, current streaming systems cannot fully support agents: they lack the fundamental mechanisms to avoid the performance interference caused by agentic tasks and to safely handle agentic writes. We argue that the shared log, the core abstraction underlying streaming data, must support creating forks of itself, and that such a forkable shared log serves as a great substrate for agents acting on streaming data. We propose AgileLog, a new shared log abstraction that provides novel forking primitives for agentic use cases. We design Bolt, a system that implements the AgileLog abstraction. Bolt uses many novel techniques to make forks cheap and to provide logical and performance isolation.
