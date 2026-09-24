# Silent Failures Beyond the 32-Bit Index Range: A Differential Characterization of Large-Tensor Matrix Multiplication in PyTorch's MPS Backend

- **URL:** https://arxiv.org/abs/2609.22991
- **Author:** Junichiro Niimi
- **Published Date:** 2026-09-24 04:00 UTC
- **Tags:** `distributed-systems`, `research`
- **Source:** arXiv cs.DC (Distributed Computing)

---

## Summary
arXiv:2609.22991v2 Announce Type: replace Abstract: Apple Silicon machines with large unified memory make it possible to hold large tensors on a desktop GPU. However, we found that PyTorch's Metal Performance Shaders (MPS) backend silently returns wrong results for batched matrix multiplication with more than elements. torch bmm, including its wrappers matmul and eager attention, returns relative errors above 1 without an exception or a warning in every PyTorch release tested (2.4.1 to 2.14.0). We sweep bmm over dtypes, memory layouts, shapes and batch sizes around and elements, and judge every result against a float64 computation on the CPU. Three rules account for every outcome on 2.14.0. When the output exceeds elements and an operand is a transposed view, the entire output is wrong and equals a computation that ignores that operand's strides. Otherwise, a view with at least elements raises an exception, and a contiguous input above elements makes exactly the batches beyond that point wrong, equal to a computation whose index wraps at . A slightly larger problem can thus turn an explicit error into a silent failure. The rules extend to the backward pass, where a correct forward pass can return silently wrong gradients. A second machine with another chip, under two macOS versions, reproduces all 6156 results, including the wrong values, and the same sweeps on an NVIDIA A100 are correct in all 2530 runs. In a public sentiment classifier, one oversized batch corrupts a third of the outputs, which collapse onto one class. All findings come from observable behavior, without access to the backend's closed-source kernels; we release the harness, raw results and a guard that stops any MPS operation touching or more elements at jniimi/mps-silent-failures (https://github.com/jniimi/mps-silent-failures).
