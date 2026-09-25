# Ingest-Time Fact Compilation for Cost-Efficient and Reliable Question Answering over Revised Corpora

- **URL:** https://arxiv.org/abs/2609.29661
- **Author:** Kyle Wild, Yusuke Takahashi, Asako Uraki
- **Published Date:** 2026-09-25 04:00 UTC
- **Tags:** `databases`, `research`
- **Source:** arXiv cs.DB (Databases)

---

## Summary
arXiv:2609.29661v1 Announce Type: cross Abstract: Most agentic question answering (QA) systems do an important part of their semantic work at the worst possible time: every time someone asks a question. When a corpus contains revisions, drafts, revocations, deletions, and sources with different levels of authority, the model must reconstruct the governed current state on every read - then throw that work away and repeat it on the next query. This is a bit like a database that rebuilds a materialized view every time someone reads from it. We present ingest-time fact compilation, an architecture that performs this work when corpus data is ingested or changed. Raw passages are rephrased into self-contained facts; rules governing revisions, deletions, effective dates, and source trust are resolved once; and the resulting state is stored as typed records carrying source and revision provenance. At query time, an inexpensive model reads the compiled record instead of reconstructing it from noisy candidates. In a controlled synthetic experiment across five seeds, the same low-cost model produced the correct value, source, and revision in only one of 30 trials under query-time reconstruction, but in all 30 trials from the compiled substrate, at 12.89 times lower mean read cost per question. On simpler revision questions both architectures were exact, but the compiled path used 21.6 times fewer tokens. A separate test found that fact rephrasing roughly halved verbose Federal Reserve dialogue while preserving high source entailment, but left concise Wikipedia prose essentially unchanged. These results support a narrow but practical claim: resolving a corpus state once can make subsequent QA cheaper and more reliable for inexpensive models. We release the open source, MIT-licensed implementation and experimental artifacts.
