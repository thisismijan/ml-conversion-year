# Week 14 — Phase 3: Transformers

**Topic:** Multi-head + positional + norm

## Goals
- Causal masking, multi-head attention, positional encoding, layer norm, residual connections

## Resources
- **[Video]** Let's build GPT (multi-head attention, positional encoding, LayerNorm, residuals segment) — Andrej Karpathy — https://www.youtube.com/watch?v=kCc8FmEb1nY
- **[Blog]** Transformer Architecture: The Positional Encoding — Amirhossein Kazemnejad — https://kazemnejad.com/blog/transformer_architecture_positional_encoding/ — deep-dive on why sinusoidal positional encodings work and their relative-position property
- **[Blog]** The Illustrated Transformer — Jay Alammar — https://jalammar.github.io/illustrated-transformer/ — clear diagrams for multi-head split/concat and the residual+LayerNorm sublayers

**Stretch:** Compare causal (decoder) masking vs no masking by visualizing the attention matrix as a heatmap for both.

## Milestone / exercise
Add all four to your attention module.

## Daily plan (10h)
- **Mon** (2h): Kazemnejad's positional encoding blog
- **Tue** (2h): Illustrated Transformer diagrams for multi-head split/concat and residual/LayerNorm sublayers
- **Wed** (2h): Project build — add multi-head attention (split/concat) and causal masking to your attention module
- **Thu** (2h): Add sinusoidal positional encoding + LayerNorm + residual connections; visualize masked vs unmasked attention heatmaps
- **Fri** (1.5h + 0.5h): Compare the heatmaps side by side -> video: causal masking, made visible

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
