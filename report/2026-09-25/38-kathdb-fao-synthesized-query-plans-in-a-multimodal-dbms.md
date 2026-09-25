# KathDB-FAO: Synthesized Query Plans in a Multimodal DBMS

- **URL:** https://arxiv.org/abs/2609.28761
- **Author:** Guorui Xiao, Douglas Brown, Artur Borycki, Magdalena Balazinska
- **Published Date:** 2026-09-25 04:00 UTC
- **Tags:** `databases`, `research`
- **Source:** arXiv cs.DB (Databases)

---

## Summary
arXiv:2609.28761v1 Announce Type: new Abstract: We design, implement, and evaluate KathDB-FAO, a new query evaluation subsystem for our KathDB multimodal DBMS. KathDB-FAO takes as input a query in natural language (NL) and converts it into a query execution plan where each operator is a function whose body is synthesized during query evaluation, which allows powerful query-specific optimizations. To generate accurate and efficient plans from NL, KathDB-FAO first extracts fine-grained atomic actions for correctness, then establishes contracts on the inputs and outputs of those actions and groups them for efficiency, and finally synthesizes the function for each group on the fly. On SemBench, KathDB-FAO cuts execution cost by 58.8% on average across scenarios compared with the next best system, at comparable or better quality.
