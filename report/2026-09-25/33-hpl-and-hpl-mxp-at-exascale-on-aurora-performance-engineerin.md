# HPL and HPL-MxP at Exascale on Aurora: Performance Engineering and Characterization

- **URL:** https://arxiv.org/abs/2604.09517
- **Author:** Kazushige Goto, Huda Ibeid, Kalyan Kumaran, Servesh Muralidharan, Anthony-Trung Nguyen, Aditya Nishtala
- **Published Date:** 2026-09-25 04:00 UTC
- **Tags:** `distributed-systems`, `research`
- **Source:** arXiv cs.DC (Distributed Computing)

---

## Summary
arXiv:2604.09517v2 Announce Type: replace Abstract: Running HPL and HPL-MxP at exascale requires more than optimized numerical kernels; it requires coordinated performance engineering across communication, resource mapping, runtime configuration, CPU--GPU interaction, and mixed-precision execution. This paper reports experience from large-scale benchmarking campaigns on Aurora, the Intel-based exascale supercomputer at the Argonne Leadership Computing Facility. Aurora progressed from 0.585~EF/s on 5,439 nodes to 1.012EF/s on 9,234 nodes in FP64 HPL, while HPL-MxP reached 11.64EF/s on 9,500 nodes. We describe the system-level choices behind these results and grade the evidence for each (measured, operational, or reasoned), including locality-aware rank, GPU, memory, and NIC placement; explicit CPU--GPU pipelining; host-buffer MPI and transport configuration; phase-specific NIC assignment; AMX-accelerated mixed precision; and a hybrid point-to-point/collective path introduced after synchronization stalls at scale. This experience-based study concludes with practitioner guidance separating Aurora-specific findings from broader principles for tightly coupled heterogeneous systems.
