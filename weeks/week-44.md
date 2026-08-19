# Week 44 — Phase 7: ML systems

**Topic:** Inference server v1

## Goals
- HTTP request -> model.generate() -> response

## Resources
- **[Blog/code]** Inference Server From Scratch — Part 1: OpenAI API — Pavel Belevich — https://pbelevich.github.io/2025/09/10/Inference_Server_From_Scratch_-_Part_1.html — builds a minimal FastAPI server speaking the OpenAI /v1/chat/completions wire format, streamed via SSE, a near-exact match for this week's milestone
- **[Docs]** FastAPI StreamingResponse — used throughout the above and in most LLM-serving tutorials for token-by-token output

**Stretch:** Match the OpenAI wire format so any OpenAI-client library can hit your server later.

## Milestone / exercise
A minimal working inference server.

## Daily plan (10h)
- **Mon** (2h): Read Belevich's 'Inference Server From Scratch — Part 1: OpenAI API'
- **Tue** (2h): FastAPI StreamingResponse docs; plan your server's request/response shape
- **Wed** (2h): Project build — build a minimal HTTP server: request -> model.generate() -> response
- **Thu** (2h): Match the OpenAI /v1/chat/completions wire format so OpenAI-client libraries work against it
- **Fri** (1.5h + 0.5h): Test the server end to end with a real client call -> video: your GPT, now behind an API

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
