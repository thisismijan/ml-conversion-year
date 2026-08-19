# Week 20 — Phase 4: Modern LLM

**Topic:** RoPE

## Goals
- Rotary position embeddings — theory and implementation

## Resources
- **[Paper]** RoFormer: Enhanced Transformer with Rotary Position Embedding — Su et al. — https://arxiv.org/abs/2104.09864 — the RoPE paper itself
- **[Repo]** RoFormer reference implementation — ZhuiyiTechnology — https://github.com/ZhuiyiTechnology/roformer — original authors' code to check your implementation against

**Stretch:** Plot attention score decay vs relative token distance before/after adding RoPE.

## Milestone / exercise
Swap learned pos-embeddings for RoPE in your GPT.

## Daily plan (10h)
- **Mon** (2h): Read the RoFormer paper (Su et al.), focus on the rotation derivation
- **Tue** (2h): Study the ZhuiyiTechnology reference implementation
- **Wed** (2h): Project build — implement RoPE and swap it in for your GPT's learned positional embeddings
- **Thu** (2h): Debug shapes/rotation angles; retrain briefly to confirm it still learns
- **Fri** (1.5h + 0.5h): Plot attention-score decay vs relative token distance before/after RoPE -> video: why rotating Q/K encodes position

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
