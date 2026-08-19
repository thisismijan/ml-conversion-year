# Week 25 — Phase 4: Modern LLM

**Topic:** Implement LoRA yourself

## Goals
- Low-rank adapter math and implementation

## Resources
- **[Paper]** LoRA: Low-Rank Adaptation of Large Language Models — Hu et al. — https://arxiv.org/abs/2106.09685 — re-read sections 4 & 7 closely for the delta-W = BA math you're implementing
- **[Repo]** loralib — Microsoft — https://github.com/microsoft/LoRA — minimal reference implementation to check your from-scratch version against

**Stretch:** Sweep rank r and plot trainable-param-count vs eval loss on your own GPT.

## Milestone / exercise
LoRA implemented from scratch, applied to your GPT.

## Daily plan (10h)
- **Mon** (2h): Re-read LoRA paper sections 4 & 7 closely (the delta-W = BA math)
- **Tue** (2h): Study Microsoft's loralib reference implementation
- **Wed** (2h): Project build — implement a LoRA adapter layer from scratch (low-rank A/B, merge/unmerge)
- **Thu** (2h): Apply it to your GPT's attention/MLP projections; sweep rank r
- **Fri** (1.5h + 0.5h): Plot trainable-param-count vs eval loss across ranks -> video: LoRA from first principles

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
