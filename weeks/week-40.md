# Week 40 — Phase 7: ML systems

**Topic:** GPU fundamentals

## Goals
- CPU vs GPU, CUDA, kernels, warps, memory hierarchy, HBM, compute vs memory bound

## Resources
- **[Reference]** GPU Glossary (memory hierarchy, CUDA programming model, thread hierarchy) — Modal — https://modal.com/gpu-glossary — best free from-scratch primer on SM/warp/HBM/shared-memory concepts for ML engineers
- **[Worklog]** How to Optimize a CUDA Matmul Kernel for cuBLAS-like Performance — Simon Boehm — https://siboehm.com/articles/22/CUDA-MMM — iteratively optimizes naive matmul to ~95% of cuBLAS, makes compute-vs-memory-bound concrete
- **[Tutorial]** PyTorch Profiler recipe — PyTorch — https://docs.pytorch.org/tutorials/recipes/recipes/profiler_recipe.html — the tool needed to profile your matmul
- **[Article]** Understanding Application Performance with Roofline Modeling — Towards Data Science — https://towardsdatascience.com/understanding-application-performance-with-roofline-modeling/ — arithmetic-intensity framework to classify compute- vs memory-bound

**Stretch:** Try Boehm's kernel progression yourself in a minimal CUDA or Triton snippet, not just read it.

## Milestone / exercise
Profile a matmul; identify if it's compute- or memory-bound.

## Daily plan (10h)
- **Mon** (2h): Theory / implement concepts
- **Tue** (2h): Theory / implementation
- **Wed** (2h): Project build (no videos)
- **Thu** (2h): Reading / experiments & debugging
- **Fri** (1.5h + 0.5h): Read a paper / reproduce a result -> curate into weekly video

## Checklist
- [ ] Core reading/lecture done
- [ ] Exercise/milestone implemented
- [ ] Code pushed to relevant repo
- [ ] Friday video recorded & published
- [ ] Notes on what was hard / what to revisit

## Video outline (draft while working, don't leave to Friday)
1. What I set out to learn this week
2. The one concept that took longest to click, explained simply
3. Demo of the code/result
4. What's next
