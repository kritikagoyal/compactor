# GLASS: Architecture-Tuned, Composable, Device-Side Linear Algebra for Edge Robotics and Beyond

- **URL:** https://arxiv.org/abs/2609.28179
- **Author:** Brian Plancher
- **Published Date:** 2026-09-24 04:00 UTC
- **Tags:** `distributed-systems`, `research`
- **Source:** arXiv cs.DC (Distributed Computing)

---

## Summary
arXiv:2609.28179v1 Announce Type: cross Abstract: GPU robotics lacks the reusable numerical infrastructure of mature CPU stacks, instead relying on compiler frameworks that introduce overhead or repeatedly reimplementing numerical libraries. To address this, we introduce GLASS (GPU Linear Algebra Simple Subroutines), a header-only CUDA C++ library that provides thread-, warp-, block-, and NVIDIA-backed implementations of robotics-scale linear algebra and geometric computations under one composable device API. GLASS treats implementation choice, execution scope, and launch packing as architecture-specific placement decisions determined by offline measurement and resolved statically at compile time. This is critical as the best and worst placements differ by a median of 4.9x (max 81x), with 145 of 396 recommended placements changing between a Jetson AGX Orin and an RTX 5090, and 162 of 396 versus an AGX Xavier. These stakes are highest at the edge as GLASS's advantage over the best of PyTorch and JAX is as much as 73x on the Orin versus 12x on the RTX 5090. GLASS is released open source with independent numerical oracles and source-bound local-GPU test attestation. Finally, integrating GLASS with published robotics systems both exposed a pre-existing numerical bug and improved embedded runtimes by up to 1.5x.
