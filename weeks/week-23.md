# Week 23 — Phase 4: Modern LLM

**Topic:** Scaling

## Goals
- Parameter count, FLOPs, training tokens, compute-optimal training, scaling laws

## Resources
- **[Paper]** Scaling Laws for Neural Language Models — Kaplan et al. — https://arxiv.org/abs/2001.08361 — original scaling-law formulation (params/data/compute power laws)
- **[Paper]** Training Compute-Optimal Large Language Models (Chinchilla) — Hoffmann et al. — https://arxiv.org/abs/2203.15556 — the paper to compare your own model's token budget against

**Stretch:** Compute where your GPT would sit on the Chinchilla compute-optimal frontier if scaled to 1B/10B params.

## Milestone / exercise
Estimate compute-optimal token count for your model size; compare to Chinchilla.

## Daily plan (10h)
- **Mon** (2h): Read the Kaplan et al. scaling laws paper
- **Tue** (2h): Read the Chinchilla paper (Hoffmann et al.), focus on the compute-optimal formula
- **Wed** (2h): Project build (no video) — compute your model's exact parameter count and FLOPs
- **Thu** (2h): Estimate compute-optimal token count for your model size; compare to what you actually trained on
- **Fri** (1.5h + 0.5h): Plot where your model sits on the Chinchilla frontier scaled to 1B/10B -> video: is my GPT over- or under-trained?

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
