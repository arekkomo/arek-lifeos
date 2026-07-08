# LongCat‑Flash‑Chat

Tags: AI Automation, Content Creation, VFX
Description: High‑throughput MoE LLM (560B params) with dynamic activation (~27B) and 128k token context, optimized for agentic tasks.
URL: https://github.com/meituan-longcat/LongCat-Flash-Chat
Date Added: November 15, 2025 5:19 PM
Type: Github
Archive: No
Spark: No

## Summary

LongCat‑Flash‑Chat from Meituan LongCat Team uses a Mixture‑of‑Experts architecture to activate only a subset of its 560B parameters per token using a zero‑computation experts design and shortcut‑connected MoE blocks. It supports extremely long context (128k tokens) and shows strong reasoning/coding performance while maintaining inference efficiency.

## Features

- Dynamic MoE activation (18.6B‑31.3B params per token)
- Shortcut‑connected MoE (ScMoE) architecture for improved training/inference efficiency
- Long context (128k tokens) support
- Strong benchmark performance on reasoning/coding tasks

## Use Cases

Developing advanced conversational agents, large‑context interactive tools, coding helpers, content creation systems with extended context or multi‑step reasoning.

## Installation

Clone the repo and check install instructions in README; model weights and usage via Hugging Face (meituan‑longcat/LongCat‑Flash‑Chat) and deployment guides for SGLang/vLLM. ([digitalocean.com](https://www.digitalocean.com/community/tutorials/longcat-flash-chat-2025?utm_source=chatgpt.com))

## Other Info

Released by Meituan LongCat team 2025; open‑source MIT; strong architecture focus on efficiency and agentic capability. ([arxiv.org](https://arxiv.org/abs/2509.01322?utm_source=chatgpt.com))