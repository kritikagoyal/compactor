# Distributed Service Orchestration in Edge-Cloud Continuum for Digital Healthcare

- **URL:** https://arxiv.org/abs/2609.28855
- **Author:** Johirul Islam, Hafiz Faheem Shahid, Ijaz Ahmad, Tanesh Kumar, Ayan Mondal, Erkki Harjula
- **Published Date:** 2026-09-25 04:00 UTC
- **Tags:** `distributed-systems`, `docker`, `research`
- **Source:** arXiv cs.DC (Distributed Computing)

---

## Summary
arXiv:2609.28855v1 Announce Type: new Abstract: Today's digital healthcare services rely on various applications and functions that must be continuously accessible. Cloud computing enables global access to these services through public networks, which often also introduce increased latency, higher bandwidth consumption, and additional security risks compared to local operation. Edge computing mitigates these challenges by deploying cloud services closer to the end users and data sources, thereby improving resilience to network disruptions and reducing latency, bandwidth usage, and exposure to security threats. However, service deployment typically relies on the availability of centralized registry servers. Consequently, if the network connection or the registry server itself becomes unavailable, service deployment at the target edge node may fail. To address this, we propose a three-tier registry architecture to enhance deployment reliability and service availability, considering DockerHub as a remote public registry, an MEC-based off-premises registry as a remote private registry, and a LAN-based on-premises registry as a local private registry. The performance and efficiency are analyzed through measurements related to the estimated deployment time, inflicted network and computational load, and energy consumption, while the required nanoservices are deployed from different tiers. The experimental results indicate that alongside the improved tolerance to network disruptions, the local private and remote private registries also outperform the remote public registry in the deployment performance. The findings highlight the effectiveness of proximity-aware service distribution in improving the resilience, performance and efficiency of service deployment.
