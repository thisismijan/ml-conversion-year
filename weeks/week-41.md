# Week 41 — Phase 7: ML systems

**Topic:** Inference pipeline

## Goals
- prompt -> prefill -> KV cache -> decode -> sampling

## Resources
- **[Docs]** Caching (KV cache) — Hugging Face Transformers — https://huggingface.co/docs/transformers/en/cache_explanation — official explanation of use_cache/past_key_values
- **[Blog]** LLM Inference Series: 3. KV caching explained — Pierre Lienhart — https://medium.com/@plienhar/llm-inference-series-3-kv-caching-unveiled-048152e461c8 — why KV cache turns per-token cost from quadratic to linear
- **[Blog/code]** Inference Server From Scratch — Part 2: Real Model — Pavel Belevich — https://medium.com/@pbelevich/inference-server-from-scratch-part-2-real-model-c69b803d59ee — a real greedy_generate() loop to study/adapt

**Stretch:** Log wall-clock time for the prefill step vs each decode step separately to see the asymmetry firsthand.

## Milestone / exercise
Diagram + implement a minimal prefill/decode loop with KV cache.

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
