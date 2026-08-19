# Week 46 — Phase 7: ML systems

**Topic:** Streaming + measurement

## Goals
- TTFT, TPOT, throughput (tokens/sec), GPU memory utilisation, P50/P99/P999 latency (bring trading rigor here)

## Resources
- **[Handbook]** Key metrics for LLM inference — BentoML LLM Inference Handbook — https://bentoml.com/llm/llm-inference-basics/llm-inference-metrics — defines TTFT/TPOT/throughput precisely
- **[Blog]** LLM Inference SLO Engineering: TTFT, ITL, and P99 Latency Budgets for Production AI — Spheron — https://www.spheron.network/blog/llm-inference-slo-ttft-itl-latency-budget-guide-2026/ — directly frames P50/P95/P99/P99.9 tradeoffs
- **[Blog]** LLM Benchmarking: Latency, Throughput, TTFT, TPS — Neel Mishra — https://neelmishra.github.io/blog/mlops/llm-inference/inference-benchmarking.html

**Stretch:** Compare your P50/P99 methodology against vLLM's own benchmark_serving.py (in the vLLM repo) as a reference implementation, without depending on vLLM itself.

## Milestone / exercise
Add streaming output; build a benchmark harness reporting P50/P99/P999, not just averages.

## Daily plan (10h)
- **Mon** (2h): BentoML's Key metrics for LLM inference handbook (TTFT/TPOT/throughput)
- **Tue** (2h): Spheron's SLO Engineering blog + Neel Mishra's benchmarking post
- **Wed** (2h): Project build — add streaming (SSE) output to your server
- **Thu** (2h): Build a benchmark harness reporting P50/P99/P999, not just averages; compare against vLLM's benchmark_serving.py
- **Fri** (1.5h + 0.5h): Run the harness under load, inspect the tail -> video: P50 lies, P99 doesn't

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
