# IBLTs Measure Before They Decode: Self-Sizing Set Reconciliation for Database Consistency Verification

- **URL:** https://arxiv.org/abs/2608.26537
- **Author:** Min Wu, Ji Qi, Zhengsheng Ye, Chengdui Luo, Shudong Lu, Zhengyang Wei
- **Published Date:** 2026-09-24 04:00 UTC
- **Tags:** `databases`, `distributed-systems`, `research`, `sql`
- **Source:** arXiv cs.DC (Distributed Computing)

---

## Summary
arXiv:2608.26537v3 Announce Type: replace-cross Abstract: Cross-system data replication pipelines cannot confirm end-to-end consistency from the local guarantees of each hop, so the two endpoints must be compared directly on a periodic basis. Once the rows of a fixed snapshot are normalized into fingerprints, the task reduces to finding the symmetric difference of the two sets. An Invertible Bloom Lookup Table (IBLT) reconciles the sets with communication that grows only with the difference cardinality , independent of table size, but its capacity must be fixed while is still unknown. Across 41,603 production reconciliations over 90 days, nonzero spans about seven orders of magnitude, and no reliable empirical constant exists. We show that the count array of an IBLT has already measured before decoding. The measurement is in-band: it is carried by the recovery sketch itself and adds no bytes dedicated to estimation. A mapping-aware theorem extends the construction to Irregular, Rateless, and MET IBLTs. The protocol reads the estimate only after a decoding failure; we prove that the failure-conditioned lower quantile bounds the risk of underestimation, which gives the second-round capacity a configurable success-probability guarantee. The resulting self-sizing protocol attempts recovery with a small first-round sketch and stops on success; on failure it reads , sizes the second round, and completes reconciliation in at most two rounds. Against a controlled oracle, communication is 1.29-1.47 times that of a scheme given in advance. Production workload characterization, relational-database replay, and a cross-city KV deployment confirm the end-to-end mechanism. In production on an Oracle-MySQL link, all completed runs succeeded within two rounds, 90.7% on the 1-RTT fast path with a single 16 KB sketch.
