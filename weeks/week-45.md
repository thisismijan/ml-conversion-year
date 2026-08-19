# Week 45 — Phase 7: ML systems

**Topic:** Scheduler + dynamic batching

## Goals
- requests -> scheduler -> dynamic batching -> model -> KV cache -> streaming output
- Trading-latency framing: scheduler ~ matching engine, TTFT ~ tick-to-trade

## Resources
- **[Paper]** Orca: A Distributed Serving System for Transformer-Based Generative Models — Yu et al. — https://www.usenix.org/conference/osdi22/presentation/yu — iteration-level scheduling is the core idea here
- **[Docs]** vLLM scheduling/continuous-batching docs — https://docs.vllm.ai/en/stable/configuration/optimization/
- **[Blog]** Inside vLLM: Anatomy of a High-Throughput LLM Inference System — https://vllm.ai/blog/2025-09-05-anatomy-of-vllm — shows the schedule -> execute -> postprocess loop, a direct model for your own scheduler

**Stretch:** Write the 'scheduler ~ matching engine, TTFT ~ tick-to-trade' mapping as a one-page design note before writing code — forces the trading-domain transfer to be explicit, not just a metaphor.

## Milestone / exercise
Add a request scheduler with dynamic batching to your server.

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
