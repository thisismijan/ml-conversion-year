# Week 15 — Phase 3: Transformers

**Topic:** Transformer block

## Goals
- Assemble attention + MLP + norm + residuals into one block

## Resources
- **[Video]** Let's build GPT (assembling the Transformer Block: attention + MLP + norm + residual) — Andrej Karpathy — https://www.youtube.com/watch?v=kCc8FmEb1nY
- **[Code]** nanoGPT model.py — Andrej Karpathy — https://github.com/karpathy/nanoGPT/blob/master/model.py — canonical minimal, readable reference for a correctly-assembled GPT block to unit-test your own against
- **[Code]** The Annotated Transformer, EncoderLayer/DecoderLayer — Harvard NLP — https://nlp.seas.harvard.edu/annotated-transformer/ — second independent reference implementation for cross-checking block structure

**Stretch:** Write a unit test that feeds a fixed-seed input through your block and asserts output shape and that gradients flow to every parameter.

## Milestone / exercise
A single working Transformer block, unit-tested.

## Daily plan (10h)
- **Mon** (2h): Theory / implement concepts
- **Tue** (2h): Theory / implementation
- **Wed** (2h): Project build (no videos)
- **Thu** (2h): Reading / experiments & debugging
- **Fri** (1.5h + 0.5h): Read a paper / reproduce a result -> curate into weekly video

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
