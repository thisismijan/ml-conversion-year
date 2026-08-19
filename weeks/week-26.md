# Week 26 — Phase 4: Modern LLM

**Topic:** Integrate everything

## Goals
- GPT v1 -> RoPE -> RMSNorm -> GQA -> LoRA -> fine-tuned model

## Resources
- No new external resources — pure integration of weeks 19-25 (BPE, RoPE, RMSNorm/SwiGLU, GQA, LoRA) inside your own modern-gpt repo.

**Stretch:** Write a short design-doc/README section mapping each modification to its source paper — good scaffolding for the Friday video.

## Milestone / exercise
modern-gpt repo assembling the full stack.

## Daily plan (10h)
- **Mon** (2h): Write the design-doc/README section mapping each modification (BPE/RoPE/RMSNorm/SwiGLU/GQA/LoRA) to its source paper
- **Tue** (2h): Plan the integration order and interfaces for modern-gpt
- **Wed** (2h): Project build — assemble GPT v1 -> RoPE -> RMSNorm/SwiGLU -> GQA into one modern-gpt model
- **Thu** (2h): Wire in your from-scratch LoRA layer; get a full forward/backward pass working end to end
- **Fri** (1.5h + 0.5h): Smoke-test training for a few steps, confirm loss decreases -> video: what 'modern' means, stack by stack

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
