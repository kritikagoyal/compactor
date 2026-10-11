# JSON Tiles: Fast Analytics on Semi-Structured Data (2021)

- **URL:** https://db.cit.tum.de/~durner/papers/json-tiles-sigmod21.pdf
- **Author:** db.cit.tum.de via typesanitizer
- **Published Date:** 2026-10-11 06:21 UTC
- **Tags:** `databases`, `research`
- **Source:** Lobste.rs (Databases)

---

## Summary
Abstract: Developers often prefer flexibility over upfront schema design, making semi-structured data formats such as JSON increasingly popular. Large amounts of JSON data are therefore stored and analyzed by relational database systems. In existing systems, however, JSON’s lack of a fixed schema results in slow analytics. In this paper, we present JSON tiles, which, without losing the flexibility of JSON, enables relational systems to perform analytics on JSON data at native speed. JSON tiles automatically detects the most important keys and extracts them transparently – often achieving scan performance similar to columnar storage. At the same time, JSON tiles is capable of handling heterogeneous and changing data. Furthermore, we automatically collect statistics that enable the query optimizer to find good execution plans. Our experimental evaluation compares against state-of-the-art systems and research proposals and shows that our approach is both robust and efficient. Comments
