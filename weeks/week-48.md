# Week 48 — Phase 8: Research project

**Topic:** Pick the question + read literature

## Goals
- Candidate: batching/scheduling policy vs P99 latency under bursty load, feed-handler parallels

## Resources
- **[Paper]** Efficient Memory Management for Large Language Model Serving with PagedAttention (vLLM) — Kwon et al., SOSP 2023 — https://arxiv.org/abs/2309.06180 — reference architecture for KV-cache memory management
- **[Paper]** Orca: A Distributed Serving System for Transformer-Based Generative Models — Yu et al., OSDI 2022 — https://www.usenix.org/conference/osdi22/presentation/yu — introduces continuous/iteration-level batching, the direct analogue of matching-engine order-by-order processing vs batch auctions
- **[Paper]** SARATHI: Efficient LLM Inference by Piggybacking Decodes with Chunked Prefills — Agrawal et al. — https://arxiv.org/abs/2308.16369 — chunked-prefill scheduling, useful for interleaving big and small jobs fairly
- **[Paper]** Efficiently Scaling Transformer Inference — Pope et al. — https://arxiv.org/abs/2211.05102 — classic latency/FLOPs-utilization tradeoff analysis for large-model serving
- **[Paper]** SLO-Aware Scheduling for Large Language Model Inferences — Huang et al. (2025) — https://arxiv.org/abs/2504.14966 — recent SLO/tail-latency-aware scheduler design, closest match to 'hit a P99 target under bursty load'
- **[Paper]** A Predictive and Synergistic Two-Layer Scheduling Framework for LLM Serving — (2025) — https://arxiv.org/abs/2509.23384 — two-layer (engine + cluster) SLO-aware batching/routing, a comparison point for your own scheduler design
- **[Talk]** How NOT to Measure Latency — Gil Tene, QCon/Azul — https://www.youtube.com/watch?v=lJ8ydIuPFeU — the 'Coordinated Omission' problem; watch before designing any P99/P999 measurement, directly reusable from your trading background

**Stretch:** No single canonical paper yet bridges LLM-serving scheduling and market-microstructure queueing theory — that gap is itself the novelty angle for this research question. Skim the vLLM v0.6.0 performance blog (https://blog.vllm.ai/2024/09/05/perf-update.html) for a benchmarking-methodology template.

## Milestone / exercise
Finalise research question; annotated bibliography of 5-10 relevant papers.

## Daily plan (10h)
- **Mon** (2h): Read the PagedAttention/vLLM and Orca papers closely, this time with a research lens rather than an implementation one
- **Tue** (2h): Read the SARATHI and Efficiently Scaling Transformer Inference papers
- **Wed** (2h): Project build (no video) — read the SLO-aware and two-layer scheduling papers; watch Gil Tene's 'How NOT to Measure Latency'
- **Thu** (2h): Draft the annotated bibliography (5-10 papers, one paragraph each on relevance to your question)
- **Fri** (1.5h + 0.5h): Finalize your research question (batching/scheduling policy vs P99 latency under bursty load, feed-handler parallels) -> video: framing my research question

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
