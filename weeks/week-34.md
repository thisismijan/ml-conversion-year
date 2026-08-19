# Week 34 — Phase 5: Post-training & RL

**Topic:** Train a reward/preference model

## Goals
- Reward model architecture and training

## Resources
- **[Docs]** TRL RewardTrainer — Hugging Face — https://huggingface.co/docs/trl/en/index — scalar reward head over a base model, Bradley-Terry pairwise loss
- **[Paper]** InstructGPT — Ouyang et al. — https://arxiv.org/abs/2203.02155 — section 3.2 covers reward model training and loss specifically


## Milestone / exercise
Train a preference model on your dataset.

## Daily plan (10h)
- **Mon** (2h): TRL RewardTrainer docs — Bradley-Terry pairwise loss, reward head architecture
- **Tue** (2h): Re-read InstructGPT section 3.2 (reward model training/loss)
- **Wed** (2h): Project build — add a scalar reward head to your model
- **Thu** (2h): Train the reward model on your Week 33 preference dataset; monitor accuracy on held-out pairs
- **Fri** (1.5h + 0.5h): Sanity-check the reward model ranks obviously-better responses higher -> video: teaching a model to score, not generate

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
