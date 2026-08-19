# Week 10 — Phase 2: PyTorch fundamentals

**Topic:** Minimal-abstraction reimplementation

## Goals
- Rewrite your NN with minimal nn.* usage — most forward/training logic by hand

## Resources
- **[Repo]** tinygrad/tinygrad — tiny corp / George Hotz — https://github.com/tinygrad/tinygrad — read (don't copy) as a real-world minimal, from-scratch autodiff + NN framework, positioned between micrograd and PyTorch
- **[Repo]** karpathy/micrograd — Andrej Karpathy — https://github.com/karpathy/micrograd — revisit your Week 6 engine and extend it toward this week's tensor-level milestone

**Stretch:** Write a short README section comparing your design decisions against tinygrad's (e.g. lazy eval, ops as a small closed set).

## Milestone / exercise
Milestone: tinygrad repo — your own autodiff + NN library, README with design notes.

## Daily plan (10h)
- **Mon** (2h): Skim the tinygrad repo — README, core ops, design choices
- **Tue** (2h): Revisit your Week 6 engine; plan what needs extending to tensor-level ops
- **Wed** (2h): Project build — rewrite your Week 7 MLP with most forward/training logic hand-rolled, minimal nn.*
- **Thu** (2h): Finish the reimplementation; write tests comparing outputs/gradients to the nn.*-based version
- **Fri** (1.5h + 0.5h): Write the tinygrad repo README with design notes vs tinygrad's choices -> video: what minimal abstraction buys you

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
