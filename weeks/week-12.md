# Week 12 — Phase 3: Transformers

**Topic:** Attention, conceptually

## Goals
- Read 'Attention Is All You Need' (don't rush the whole paper)
- Q=XWq, K=XWk, V=XWv, softmax(QK^T/sqrt(d))V — understand each operation

## Resources
- **[Paper]** Attention Is All You Need — Vaswani et al. (2017) — https://arxiv.org/abs/1706.03762 — the primary source; read section 3.2 (Attention) closely, skim the rest
- **[Blog]** The Illustrated Transformer — Jay Alammar — https://jalammar.github.io/illustrated-transformer/ — the canonical plain-English + diagram walkthrough of Q/K/V and softmax(QK^T/sqrt(d))V
- **[Video]** Let's build GPT: from scratch, in code, spelled out (first ~40 min, self-attention derivation) — Andrej Karpathy — https://www.youtube.com/watch?v=kCc8FmEb1nY — watch only through the self-attention section this week; save the rest for weeks 13-17

**Stretch:** Draw the Q/K/V matrix shapes for a toy 4-token, 8-dim example by hand before writing any code.

## Milestone / exercise
Write a plain-English + math walkthrough of self-attention (this is your video script).

## Daily plan (10h)
- **Mon** (2h): Read Attention Is All You Need section 3.2 closely, skim the rest
- **Tue** (2h): The Illustrated Transformer blog — the Q/K/V walkthrough
- **Wed** (2h): Project build (no video) — draw Q/K/V shapes for a toy 4-token example by hand; work softmax(QK^T/sqrt(d))V numerically on paper
- **Thu** (2h): Watch Karpathy's self-attention derivation segment; map it onto the paper's notation
- **Fri** (1.5h + 0.5h): Write the plain-English + math self-attention walkthrough — this IS the video script — and record it

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
