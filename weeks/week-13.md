# Week 13 — Phase 3: Transformers

**Topic:** Implement self-attention

## Goals
- No nn.MultiheadAttention — build it from matmuls

## Resources
- **[Video]** Let's build GPT (self-attention head implementation segment) — Andrej Karpathy — https://www.youtube.com/watch?v=kCc8FmEb1nY — builds a Head module from raw matmuls, no nn.MultiheadAttention
- **[Code]** The Annotated Transformer — Sasha Rush / Harvard NLP — https://nlp.seas.harvard.edu/annotated-transformer/ (repo: https://github.com/harvardnlp/annotated-transformer) — line-by-line PyTorch implementation to check your from-scratch attention against
- **[Reference]** CS231n Gradient checks notes — Stanford — https://cs231n.github.io/neural-networks-3/ — relative-error thresholds and float64 precision guidance for this week's numerical gradient check

**Stretch:** Also gradient-check against PyTorch autograd directly (torch.autograd.gradcheck) as a second, independent verification.

## Milestone / exercise
Self-attention module passing a numerical gradient check.

## Daily plan (10h)
- **Mon** (2h): Re-watch the Head-module implementation segment of Let's Build GPT
- **Tue** (2h): Study the Annotated Transformer's attention implementation line by line
- **Wed** (2h): Project build — implement a single self-attention head from raw matmuls, no nn.MultiheadAttention
- **Thu** (2h): Write a numerical gradient check (CS231n method) + cross-check with torch.autograd.gradcheck; fix bugs
- **Fri** (1.5h + 0.5h): Get the gradient check passing cleanly -> video: what a gradient check actually verifies

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
