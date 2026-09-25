# Adaptive Tiling for Least-Squares Phase Unwrapping: Runtime and Accuracy

- **URL:** https://arxiv.org/abs/2609.28541
- **Author:** Antoine Moevus, Max Mignotte
- **Published Date:** 2026-09-25 04:00 UTC
- **Tags:** `distributed-systems`, `research`
- **Source:** arXiv cs.DC (Distributed Computing)

---

## Summary
arXiv:2609.28541v1 Announce Type: cross Abstract: Phase unwrapping estimates the missing multiples of in measured phase images. For large images, tiling limits the size of local reconstruction problems and enables parallel processing. Adaptive tiling could further reduce the number of local problems and boundaries by retaining large tiles where little refinement is needed. We investigate whether this reduction makes reconstruction faster. We compare complete reconstruction time and accuracy for a regular grid, quadtree, and kd-tree partitions. We also evaluate nine criteria for deciding where quadtree tiles should be subdivided, including residue count, fringe density, and measures of phase variation, at different tile sizes and budgets. In single-threaded experiments on a heterogeneous image dataset, optimized adaptive partitions use fewer tiles but remain slower than the optimized grid, and some reconstructions lose substantial accuracy. Stage measurements explain why: constructing the partition and solving larger retained tiles outweigh the savings at tile boundaries. The criterion comparison also shows that more refinement does not consistently improve accuracy. These results motivate evaluating adaptive partitions by the complete time needed to reach a chosen reconstruction accuracy, including whether limited refinement can provide a faster approximate result.
