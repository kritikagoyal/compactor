# Dependency- and Layer-Aware Microservice Workflow Offloading and Service Image Caching for Edge Environments

- **URL:** https://arxiv.org/abs/2609.28943
- **Author:** Zhongxiao Wang, Yueshen Xu, Qingshan Li, Xinkui Zhao, Wei Shao, Shuiguang Deng, Rui Li
- **Published Date:** 2026-09-25 04:00 UTC
- **Tags:** `distributed-systems`, `research`
- **Source:** arXiv cs.DC (Distributed Computing)

---

## Summary
arXiv:2609.28943v1 Announce Type: new Abstract: The microservice architecture has been applied broadly in many mainstream computing environments. As one of the most prevalent environments, edge computing also widely employs microservices to handle diverse requests and tasks. In practical scenarios, microservices usually constitute workflows that are built based on service dependencies to execute tasks. This offers an opportunity to explore the offloading technology to better harness resources and accelerate task execution. Unfortunately, this problem has not been paid attention to by existing research, and thus some valuable resources (e.g., microservice image cache) remain obscure. To fill this gap, we innovatively study the problem of joint optimization for microservice workflow offloading and service image caching in edge. This problem is challenging due to several issues such as the complexity of its solution space, intricate relationships among shared image layers, long-range dependencies between workflow tasks, and the absence of a real-world collection of service images. To address these issues, this paper proposes an innovative dependency- and layer-aware workflow offloading and image caching framework for microservices. We collected a real-world collection of microservice image layer data and published both this collection and experimental codes on GitHub. Extensive results demonstrate that our framework achieves superior performances, for example, a 22. 38\% reduction in average task completion time compared to baselines and significantly-increased image hit rates.
