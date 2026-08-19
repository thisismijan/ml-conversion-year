# Week 42 — Phase 7: ML systems

**Topic:** Batching

## Goals
- Static vs continuous batching, quantisation, FlashAttention

## Resources
- **[Paper]** Orca: A Distributed Serving System for Transformer-Based Generative Models — Yu et al., OSDI 2022 — https://www.usenix.org/conference/osdi22/presentation/yu — the iteration-level/continuous batching paper
- **[Paper]** Efficient Memory Management for Large Language Model Serving with PagedAttention (vLLM) — Kwon et al. — https://arxiv.org/abs/2309.06180
- **[Paper+repo]** FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness — Dao et al. — https://arxiv.org/abs/2205.14135 (repo: https://github.com/dao-ailab/flash-attention)
- **[Docs]** vLLM Optimization and Tuning — https://docs.vllm.ai/en/stable/configuration/optimization/ — concrete knobs (max-num-seqs, max-num-batched-tokens) that map straight to the batching concepts

**Stretch:** Read 'Inside vLLM: Anatomy of a High-Throughput LLM Inference System' to see how a production system combines all of the above: https://vllm.ai/blog/2025-09-05-anatomy-of-vllm

## Milestone / exercise
Add basic batching to your inference loop.

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
