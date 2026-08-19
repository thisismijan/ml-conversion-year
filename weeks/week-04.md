# Week 04 — Phase 1: Math refresh

**Topic:** Info theory + optimisation

## Goals
- Entropy, cross-entropy, KL divergence, perplexity, softmax, log-probs (stat-mech parallel: Boltzmann distribution)
- Implement softmax and cross-entropy yourself
- SGD, momentum, Adam, learning rate, weight decay, regularisation, train/val/test

## Resources
- **[Blog]** Visual Information Theory — Chris Olah — https://colah.github.io/posts/2015-09-Visual-Information/ — best available entropy/cross-entropy/KL-divergence explainer, builds intuition before implementing softmax+cross-entropy from scratch
- **[Notes]** Linear Classification: Softmax classifier & cross-entropy — CS231n / Karpathy — https://cs231n.github.io/linear-classify/#softmax — worked derivation matching the 'implement it yourself' milestone directly
- **[Paper/Survey]** An Overview of Gradient Descent Optimization Algorithms — Sebastian Ruder — https://arxiv.org/abs/1609.04747 — SGD -> momentum -> AdaGrad/RMSprop -> Adam derivations in one place, exactly what you need to implement SGD and Adam in NumPy
- **[Notes]** Neural Networks Part 3: Learning and Evaluation — CS231n — https://cs231n.github.io/neural-networks-3/ — practical companion on LR schedules, weight decay, train/val/test methodology

**Stretch:** After implementing Adam, reproduce Ruder's toy loss-landscape comparison plot (different optimizers converging at different rates) on a simple 2D function.

## Milestone / exercise
Implement SGD and Adam with NumPy. Milestone: explain 'how does a neural net learn' end-to-end, in code.

## Daily plan (10h)
- **Mon** (2h): Chris Olah's Visual Information Theory; CS231n softmax/cross-entropy notes
- **Tue** (2h): Implement softmax + cross-entropy from scratch in NumPy; test against a known worked example
- **Wed** (2h): Project build — implement plain SGD with NumPy on a toy loss surface
- **Thu** (2h): Ruder's optimization overview -> add momentum + Adam; CS231n Part 3 for LR schedules/weight decay/train-val-test
- **Fri** (1.5h + 0.5h): Reproduce Ruder's optimizer-comparison plot on your own 2D loss function -> video: how a neural net learns, end to end

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
