# Week 35 — Phase 5: Post-training & RL

**Topic:** Run DPO, compare

## Goals
- Run DPO end to end

## Resources
- **[Paper]** Direct Preference Optimization — Rafailov et al. — https://arxiv.org/abs/2305.18290
- **[Docs]** TRL DPOTrainer — Hugging Face — https://huggingface.co/docs/trl/en/index — validate your from-scratch DPO loss against a known-correct implementation

**Stretch:** Report win-rate of DPO vs SFT vs base using your own GPT as an LLM-judge, foreshadowing Phase 6's eval-design work.

## Milestone / exercise
Milestone: mini-post-training-lab — compare base vs SFT vs DPO on an eval set.

## Daily plan (10h)
- **Mon** (2h): Re-read the DPO paper's loss derivation alongside TRL's DPOTrainer implementation
- **Tue** (2h): Validate your Week 31 DPO loss implementation against TRL's as a known-correct reference
- **Wed** (2h): Project build — run DPO training on your SFT model using your Week 33 preference data
- **Thu** (2h): Set up an eval comparing base vs SFT vs DPO (use your GPT as an LLM-judge for win-rate)
- **Fri** (1.5h + 0.5h): Finalize the mini-post-training-lab comparison + win-rate results -> video: base vs SFT vs DPO

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
