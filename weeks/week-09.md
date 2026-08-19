# Week 09 — Phase 2: PyTorch fundamentals

**Topic:** Deep learning behaviour

## Goals
- Initialization, exploding/vanishing gradients, normalization, dropout, LR schedules

## Resources
- **[Notes]** CS231n: Neural Networks Part 2 (Setting up the data and the loss) — Stanford CS231n — https://cs231n.github.io/neural-networks-2/ — the standard reference on weight-init pitfalls and regularization/dropout
- **[Notes]** CS231n: Neural Networks Part 3 (Learning and Evaluation) — Stanford CS231n — https://cs231n.github.io/neural-networks-3/ — babysitting the learning process via loss curves, exactly the diagnostic skill this week's milestone requires

**Stretch:** Deliberately reproduce vanishing gradients with a deep sigmoid MLP and fix it with better init/normalization, per CS231n's guidance.

## Milestone / exercise
Deliberately break a model 3 ways (bad init, no norm, huge LR) and diagnose each from the loss curve.

## Daily plan (10h)
- **Mon** (2h): CS231n Neural Networks Part 2 (weight init pitfalls, regularization/dropout)
- **Tue** (2h): CS231n Neural Networks Part 3 (babysitting the learning process via loss curves)
- **Wed** (2h): Project build — break #1: bad init on a deep MLP, observe and record the loss curve
- **Thu** (2h): Break #2 (no normalization) and #3 (huge LR); diagnose each from its loss curve, then fix each
- **Fri** (1.5h + 0.5h): Write up the three failure signatures side by side -> video: reading a loss curve like an X-ray

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
