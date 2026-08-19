# Week 17 — Phase 3: Transformers

**Topic:** Train it

## Goals
- Tokenisation, batches, sequence length, LR, validation loss, sampling temperature, top-k

## Resources
- **[Video]** Let's build GPT (training loop, loss curves, sampling) — Andrej Karpathy — https://www.youtube.com/watch?v=kCc8FmEb1nY
- **[Docs]** How to generate text: using different decoding methods — Hugging Face — https://huggingface.co/docs/transformers/main_classes/text_generation — official reference for temperature/top-k/top-p sampling semantics and application order

**Stretch:** Plot validation loss for 2-3 different learning rates on the same chart to build intuition before Phase 4's scaling-laws work.

## Milestone / exercise
Train on a small corpus; sample text at a few temperatures.

## Daily plan (10h)
- **Mon** (2h): Watch Karpathy's training-loop/sampling segment
- **Tue** (2h): HF docs on decoding methods (temperature/top-k/top-p) and the order they're applied
- **Wed** (2h): Project build — set up tokenisation, batching, sequence length, train/val split on a small corpus
- **Thu** (2h): Train the model tracking validation loss; implement temperature + top-k sampling
- **Fri** (1.5h + 0.5h): Sample text at a few temperatures, plot val loss for 2-3 LRs -> video: watching your GPT learn to babble

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
