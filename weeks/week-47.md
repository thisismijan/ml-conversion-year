# Week 47 — Phase 7: ML systems

**Topic:** Benchmark + writeup

## Goals
- Consolidate benchmarks, compare batching strategies

## Resources
- **[Paper]** Efficiently Scaling Transformer Inference — Pope et al. (Google), MLSys 2023 Outstanding Paper — https://arxiv.org/abs/2211.05102 — gold-standard example of a rigorous latency/throughput/MFU writeup; model your llm-engine writeup's structure on this paper's Pareto-frontier framing

**Stretch:** Reuse week 46's metrics resources for the benchmark-harness section of the writeup.

## Milestone / exercise
Milestone: llm-engine repo with benchmarks and a latency writeup.

## Daily plan (10h)
- **Mon** (2h): Read Pope et al. 'Efficiently Scaling Transformer Inference' — the Pareto-frontier framing
- **Tue** (2h): Consolidate all benchmark runs (static vs dynamic batching) into comparable tables/plots
- **Wed** (2h): Project build (no video) — draft the llm-engine latency writeup's methodology + results sections
- **Thu** (2h): Draft the analysis/discussion, modeled on Pope et al.'s structure; polish the repo
- **Fri** (1.5h + 0.5h): Finalize llm-engine repo + writeup -> video: batching strategies, benchmarked

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
