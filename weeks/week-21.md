# Week 21 — Phase 4: Modern LLM

**Topic:** RMSNorm + SwiGLU

## Goals
- RMSNorm vs LayerNorm, SwiGLU activation

## Resources
- **[Paper]** Root Mean Square Layer Normalization — Zhang & Sennrich — https://arxiv.org/abs/1910.07467 — the RMSNorm paper
- **[Paper]** GLU Variants Improve Transformer — Noam Shazeer — https://arxiv.org/abs/2002.05202 — introduces SwiGLU, now standard in LLaMA/PaLM/DeepSeek

**Stretch:** Ablate LayerNorm-vs-RMSNorm and ReLU-vs-SwiGLU independently; log both loss curves on the same plot.

## Milestone / exercise
Swap in RMSNorm + SwiGLU, compare training curves.

## Daily plan (10h)
- **Mon** (2h): Read the RMSNorm paper (Zhang & Sennrich)
- **Tue** (2h): Read the GLU Variants paper (Shazeer) for SwiGLU
- **Wed** (2h): Project build — swap LayerNorm for RMSNorm in your GPT
- **Thu** (2h): Swap the MLP activation for SwiGLU; run LayerNorm-vs-RMSNorm and ReLU-vs-SwiGLU ablations
- **Fri** (1.5h + 0.5h): Plot both loss curves on the same chart -> video: two small swaps, one modern GPT

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
