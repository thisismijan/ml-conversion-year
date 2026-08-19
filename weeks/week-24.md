# Week 24 — Phase 4: Modern LLM

**Topic:** Fine-tuning landscape

## Goals
- SFT, LoRA, QLoRA, PEFT, quantisation — survey

## Resources
- **[Docs]** PEFT Quicktour — Hugging Face — https://huggingface.co/docs/peft/quicktour — practical LoRA fine-tune of an open model, this week's milestone
- **[Paper]** LoRA: Low-Rank Adaptation of Large Language Models — Hu et al. — https://arxiv.org/abs/2106.09685 — read before using the library
- **[Paper]** QLoRA: Efficient Finetuning of Quantized LLMs — Dettmers et al. — https://arxiv.org/abs/2305.14314 — 4-bit NF4 + LoRA
- **[Docs]** Quantization overview (bitsandbytes/GPTQ/AWQ) — Hugging Face Transformers docs — https://huggingface.co/docs/transformers/main_classes/quantization

**Stretch:** Fine-tune the same base model with both full LoRA (16-bit) and QLoRA (4-bit) and compare memory/quality.

## Milestone / exercise
Fine-tune an open small model using an existing LoRA library.

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
