# Week 43 — Phase 7: ML systems

**Topic:** Distributed training concepts

## Goals
- Tensor/pipeline/data parallelism, FSDP, NCCL, checkpointing

## Resources
- **[Interactive book]** The Ultra-Scale Playbook: Training LLMs on GPU Clusters — Hugging Face (nanotron) — https://huggingface.co/spaces/nanotron/ultrascale-playbook — grounded in 4,000+ real scaling experiments; covers DP/TP/PP/context-parallel/ZeRO in one place
- **[Docs]** Parallelism methods — Hugging Face Transformers — https://huggingface.co/docs/transformers/en/perf_train_gpu_many
- **[Tutorial]** Getting Started with FSDP — PyTorch — https://docs.pytorch.org/tutorials/intermediate/FSDP1_tutorial.html (note: FSDP2 is now current)
- **[Docs]** NCCL documentation — NVIDIA — https://docs.nvidia.com/deeplearning/nccl/ — reference for what's actually moving data between GPUs under DDP/FSDP


## Milestone / exercise
Write up how you'd parallelise training your GPT across N GPUs (design doc, doesn't need real hardware).

## Daily plan (10h)
- **Mon** (2h): HF's Ultra-Scale Playbook — data/tensor/pipeline parallelism sections
- **Tue** (2h): HF Parallelism methods docs + PyTorch FSDP tutorial
- **Wed** (2h): Project build (no video) — sketch how you'd parallelise training your GPT across N GPUs
- **Thu** (2h): Read NCCL docs for what actually moves between GPUs; refine the design doc with a checkpointing strategy
- **Fri** (1.5h + 0.5h): Finalize the parallelisation design doc -> video: how I'd scale my GPT's training across N GPUs

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
