# Week 05 — Phase 2: PyTorch fundamentals

**Topic:** Tensors + GPU execution

## Goals
- x.shape, x.dtype, x.device, x.requires_grad
- CPU <-> GPU movement
- PyTorch 'Learn the Basics' tutorial

## Resources
- **[Tutorial]** Learn the Basics (Quickstart -> Tensors -> Autograd -> Optimization) — PyTorch official docs — https://docs.pytorch.org/tutorials/beginner/basics/intro.html — the canonical, official walkthrough of exactly this week's tensor/device/autograd basics
- **[Article]** PyTorch in One Hour: From Tensors to Training Neural Networks on Multiple GPUs — Sebastian Raschka — https://sebastianraschka.com/teaching/pytorch-1h/ — dense single-sitting refresher on tensors/devices/autograd
- **[Docs]** torch.Tensor attributes (shape, dtype, device, requires_grad) — PyTorch docs — https://docs.pytorch.org/docs/stable/tensors.html — primary reference for this week's exact goals


## Milestone / exercise
Port your NumPy linear regression to PyTorch tensors.

## Daily plan (10h)
- **Mon** (2h): PyTorch 'Learn the Basics' Quickstart + Tensors sections
- **Tue** (2h): Raschka's PyTorch in One Hour (tensors/devices/autograd); torch.Tensor docs for shape/dtype/device/requires_grad
- **Wed** (2h): Project build — port Week 1's NumPy linear regression to PyTorch tensors (CPU)
- **Thu** (2h): Add CPU<->GPU (or MPS) movement; benchmark CPU vs GPU/MPS timing on the same run
- **Fri** (1.5h + 0.5h): Compare the ported loss curve to Week 1's NumPy version -> video: what changes when you move to tensors

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
