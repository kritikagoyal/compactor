# Perseus: A Fail-Slow Detection Framework for Cloud Storage Systems (2023)

- **URL:** https://www.usenix.org/system/files/fast23-lu.pdf
- **Author:** usenix.org via typesanitizer
- **Published Date:** 2026-10-06 18:11 UTC
- **Tags:** `distributed-systems`, `research`
- **Source:** Lobste.rs (Distributed Systems)

---

## Summary
Abstract: The newly-emerging “fail-slow” failures plague both software and hardware where the victim components are still functioning yet with degraded performance. To address this problem, this paper presents PERSEUS, a practical fail-slow detection framework for storage devices. PERSEUS leverages a light regression-based model to fast pinpoint and analyze fail-slow failures at the granularity of drives. Within a 10-month close monitoring on 248K drives, PERSEUS managed to find 304 fail-slow cases. Isolating them can reduce the (node-level) 99.99th tail latency by 48%. We assemble a large-scale fail-slow dataset (including 41K normal drives and 315 verified fail-slow drives) from our production traces, based on which we provide root cause analysis on fail-slow drives covering a variety of ill-implemented scheduling, hardware defects, and environmental factors. We have released the dataset to the public for fail-slow study. Comments
