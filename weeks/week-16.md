# Week 16 — Phase 3: Transformers

**Topic:** Stack it: build GPT

## Goals
- Stack blocks into a full model

## Resources
- **[Repo]** nanoGPT — Andrej Karpathy — https://github.com/karpathy/nanoGPT — 'the simplest, fastest repository for training/finetuning medium-sized GPTs,' the direct target architecture for stacking blocks into a full model
- **[Video]** Let's build GPT (full model assembly + generation loop) — Andrej Karpathy — https://www.youtube.com/watch?v=kCc8FmEb1nY
- **[Repo]** minGPT — Andrej Karpathy — https://github.com/karpathy/minGPT — even smaller (~300 line) reference if nanoGPT feels too dense

**Stretch:** Print total parameter count and compare it against a back-of-envelope calc (embedding + per-layer attention/MLP params x n_layer).

## Milestone / exercise
A tiny, architecturally-correct GPT.

## Daily plan (10h)
- **Mon** (2h): Read nanoGPT's model.py end to end — the full GPT class, not just the Block
- **Tue** (2h): Skim minGPT as a second, smaller reference; note the differences from nanoGPT
- **Wed** (2h): Project build — stack your Blocks into a full GPT class (embedding, N blocks, final norm, output head)
- **Thu** (2h): Wire up the forward pass end to end on dummy input; sanity-check parameter count against a back-of-envelope calc
- **Fri** (1.5h + 0.5h): Confirm architecture correctness -> video: from block to full model

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
