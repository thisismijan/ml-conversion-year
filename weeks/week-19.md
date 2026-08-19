# Week 19 — Phase 4: Modern LLM

**Topic:** BPE tokenisation

## Goals
- BPE / SentencePiece-style approaches

## Resources
- **[Video+Repo]** Let's build the GPT Tokenizer — Andrej Karpathy — https://www.youtube.com/watch?v=zduSFxRajkE (repo: https://github.com/karpathy/minbpe) — builds a BPE tokenizer from scratch, the exact milestone for this week; minbpe's exercise.md has 4 progressive steps to a GPT-4-equivalent tokenizer
- **[Docs]** SentencePiece — Google (GitHub) — https://github.com/google/sentencepiece — compare against a production BPE/unigram library after building your own

**Stretch:** Diff your tokenizer's vocab/merges against tiktoken's cl100k_base on a shared text sample.

## Milestone / exercise
Implement a BPE tokenizer yourself.

## Daily plan (10h)
- **Mon** (2h): Karpathy's Let's build the GPT Tokenizer video, part 1
- **Tue** (2h): Continue the tokenizer video; read minbpe's exercise.md for the 4-step progression
- **Wed** (2h): Project build — implement BPE training (merge counting) from scratch
- **Thu** (2h): Implement encode/decode; compare vocab/merges against SentencePiece and tiktoken's cl100k_base
- **Fri** (1.5h + 0.5h): Diff your tokenizer's output against tiktoken on a shared text sample -> video: BPE merges, visualized

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
