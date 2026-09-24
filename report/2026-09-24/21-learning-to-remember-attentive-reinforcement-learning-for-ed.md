# Learning to Remember: Attentive Reinforcement Learning for Edge Serverless Autoscaling

- **URL:** https://arxiv.org/abs/2603.28790
- **Author:** Faraz Shaikh, Gianluca Reali, Mauro Femminella
- **Published Date:** 2026-09-24 04:00 UTC
- **Tags:** `distributed-systems`, `kubernetes`, `research`
- **Source:** arXiv cs.DC (Distributed Computing)

---

## Summary
arXiv:2603.28790v2 Announce Type: replace Abstract: In edge computing, the stochastic and bursty nature of serverless workloads challenges autonomous resource orchestration. Traditional reactive controllers, such as the Kubernetes Horizontal Pod Autoscaler (HPA), suffer from reaction latency, leading to Service Level Objective (SLO) violations during traffic spikes and resource flapping during ramp-downs. While Deep Reinforcement Learning (DRL) offers a pathway toward proactive management, standard agents suffer from temporal blindness, an inability to exploit the recent temporal context in non-Markovian edge environments. To bridge this gap, we propose a stability-aware autoscaling framework unifying short-horizon temporal context and control via an Attention-Enhanced Double-Stacked LSTM architecture integrated within a Proximal Policy Optimization (PPO) agent. Unlike shallow recurrent models, our approach employs a learned attention mechanism that weights recent historical states non-uniformly, suppressing high-frequency jitter while preserving the trend that precedes demand shifts. We validate the framework on two independent Kubernetes clusters using real-world Azure Functions traces. Against the single-layer LSTM ablation and the static HPA baseline, our approach reduces P90 latency by 67\%, and holds average latency within the 50ms hard SLO for 98.8\% of the run against 49.6\% and 43.5\% respectively. Against Kubernetes Event-Driven Autoscaling (KEDA), it matches latency performance at 75\% fewer replica-steps and 59\% less churn, with P90 hard-SLO violation bursts of at most 5 consecutive intervals against up to 24 for KEDA. These results indicate that mitigating temporal blindness through deep attentive memory improves the reliability and stability of Kubernetes autoscaling under bursty edge workloads.
