# Week 22 — Phase 4: Modern LLM

**Topic:** GQA/MQA + FlashAttention + MoE (survey)

## Goals
- Grouped/multi-query attention, FlashAttention, mixture of experts (conceptual)

## Resources
- **[Paper]** GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints — Ainslie et al. — https://arxiv.org/abs/2305.13245 — the GQA paper, this week's implementation target
- **[Paper]** FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness — Dao et al. — https://arxiv.org/abs/2205.14135 — read for understanding, no need to implement the CUDA kernel
- **[Blog]** Mixture of Experts Explained — Hugging Face — https://huggingface.co/blog/moe — survey-level MoE explainer matching this week's 'conceptual' scope

**Stretch:** If you want a from-scratch MoE reference without committing to implementing it: https://huggingface.co/blog/AviSoori1x/makemoe-from-scratch

## Milestone / exercise
Implement GQA in your GPT (MoE/FlashAttention: understand, don't necessarily implement).

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
