# Week 31 — Phase 5: Post-training & RL

**Topic:** DPO / RLAIF

## Goals
- DPO derivation, RLAIF

## Resources
- **[Paper]** Direct Preference Optimization: Your Language Model is Secretly a Reward Model — Rafailov et al. (2023) — https://arxiv.org/abs/2305.18290 — section 4 has the derivation you're asked to implement from
- **[Paper]** Constitutional AI: Harmlessness from AI Feedback — Bai et al., Anthropic (2022) — https://arxiv.org/abs/2212.08073 — the RLAIF reference; SL-CAI + RL-CAI two-stage pipeline


## Milestone / exercise
Implement DPO loss from the paper's derivation.

## Daily plan (10h)
- **Mon** (2h): Read the DPO paper (Rafailov et al.) section 4 closely
- **Tue** (2h): Read the Constitutional AI paper (Bai et al.) for the RLAIF comparison
- **Wed** (2h): Project build — derive the DPO loss on paper from the Bradley-Terry + reward reparameterization steps
- **Thu** (2h): Implement the DPO loss function in code from your derivation
- **Fri** (1.5h + 0.5h): Unit-test the loss against known input/output pairs -> video: DPO's trick — skipping the reward model

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
