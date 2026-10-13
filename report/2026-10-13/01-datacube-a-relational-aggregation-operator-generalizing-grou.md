# DataCube: A Relational Aggregation Operator Generalizing Group-By, Cross-Tab, and Sub-Totals (1997)

- **URL:** https://arxiv.org/pdf/cs/0701155
- **Author:** arxiv.org via typesanitizer
- **Published Date:** 2026-10-13 04:57 UTC
- **Tags:** `databases`, `sql`
- **Source:** Lobste.rs (Databases)

---

## Summary
Abstract: Data analysis applications typically aggregate data across many dimensions looking for anomalies or unusual patterns. The SQL aggregate functions and the GROUP BY operator produce zero-dimensional or one-dimensional aggregates. Applications need the N-dimensional generalization of these operators. This paper defines that operator, called the data cube or simply cube. The cube operator generalizes the histogram, cross-tabulation, roll-up, drill-down, and sub-total constructs found in most report writers. The novelty is that cubes are relations. Consequently, the cube operator can be imbedded in more complex non-procedural data analysis programs. The cube operator treats each of the N aggregation attributes as a dimension of N-space. The aggregate of a particular set of attribute values is a point in this space. The set of points forms an N-dimensional cube. Super-aggregates are computed by aggregating the N-cube to lower dimensional spaces. This paper (1) explains the cube and roll-up operators, (2) shows how they fit in SQL, (3) explains how users can define new aggregate functions for cubes, and (4) discusses efficient techniques to compute the cube. Many of these features are being added to the SQL Standard. Comments
