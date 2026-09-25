# A Neural Hierarchical-Matrix Preconditioner for Real-Time GPU Solves

- **URL:** https://arxiv.org/abs/2605.13343
- **Author:** Carl Osborne, Minghao Guo, Crystal Owens, Wojciech Matusik
- **Published Date:** 2026-09-25 04:00 UTC
- **Tags:** `distributed-systems`, `research`
- **Source:** arXiv cs.DC (Distributed Computing)

---

## Summary
arXiv:2605.13343v3 Announce Type: replace-cross Abstract: Interactive simulation solves Ax=b for a sparse SPD A that changes every frame, inside an 8-16 ms budget. At a few thousand unknowns, the setup of algebraic multigrid alone exceeds that budget, while Jacobi and other local preconditioners have no setup but cannot move error across the domain. We learn a preconditioner for this gap: a graph-and-attention network predicts an SPD approximate inverse in H^2-matrix format. On a spatially ordered 3D mesh, blocks of the true inverse lose rank as the clusters they couple move apart; the nested bases of the format follow that decay, so inference and apply are dominated by leaf-block work linear in N, where a dense inverse costs N^2. Our main finding concerns training. Probe losses reach M only through a product with A, so their gradient vanishes on the near-null modes that set the conjugate-gradient iteration count. A truncated Kaporin condition number has no such factor; changing only the objective cuts iterations on a held-out frame from 116 to 33. On a ladder of stiff tetrahedral diffusion problems ours alone fits an 8.3 ms (120 fps) frame from N=572 to 3,647.
