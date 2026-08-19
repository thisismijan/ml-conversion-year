# Week 11 — Phase 3: Transformers

**Topic:** Language models 101

## Goals
- Tokenization, vocabulary, embeddings, context windows, autoregressive prediction

## Resources
- **[Video+Repo]** The spelled-out intro to language modeling: building makemore — Andrej Karpathy — https://www.youtube.com/watch?v=PaCmpygFfXo (repo: https://github.com/karpathy/makemore) — builds exactly a bigram character-level LM from counting through to a tiny neural net, the direct template for this week's milestone
- **[Series]** Neural Networks: Zero to Hero — Andrej Karpathy — https://karpathy.ai/zero-to-hero.html — index of the whole series, see how this week fits weeks 12-17
- **[Blog]** The Illustrated GPT-2 (Visualizing Transformer Language Models) — Jay Alammar — https://jalammar.github.io/illustrated-gpt2/ — conceptual grounding for tokens/embeddings/context windows before touching attention

**Stretch:** After the bigram model, try a simple trigram extension by hand to feel why it doesn't scale — motivates attention next week.

## Milestone / exercise
Build a bigram language model; generate (bad) text.

## Daily plan (10h)
- **Mon** (2h): Karpathy's makemore video, part 1 (bigram counting model)
- **Tue** (2h): The Illustrated GPT-2 blog — tokens/embeddings/context windows, conceptual grounding
- **Wed** (2h): Project build — implement the bigram counting model, sample from it
- **Thu** (2h): Reimplement as a tiny neural net (embedding + linear layer); compare to the counting version
- **Fri** (1.5h + 0.5h): Try a trigram extension by hand -> video: why bigrams break down, motivating attention

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
