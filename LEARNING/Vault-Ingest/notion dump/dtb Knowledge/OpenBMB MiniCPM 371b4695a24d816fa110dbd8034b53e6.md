# OpenBMB/MiniCPM

Tags: AI Automation, Github, LLM
Description: MiniCPM5-1B — 1B-class on-device LLM SOTA with hybrid reasoning, tool calling, 128K context, trained via RL+OPD. Works with vLLM, SGLang, llama.cpp, Ollama, MLX.
URL: https://github.com/OpenBMB/MiniCPM
Date Added: May 31, 2026 11:06 AM
Type: Github
Archive: No
Spark: No

## About

MiniCPM5-1B is the strongest open-source 1B LLM — 42.57 avg score vs next-best 35.61. Hybrid think/no-think reasoning, native tool calling, 128K context, standard LlamaForCausalLM architecture.

**GitHub:** [https://github.com/OpenBMB/MiniCPM](https://github.com/OpenBMB/MiniCPM)

**Model:** [https://huggingface.co/openbmb/MiniCPM5-1B](https://huggingface.co/openbmb/MiniCPM5-1B)

**Paper:** [https://arxiv.org/pdf/2506.07900](https://arxiv.org/pdf/2506.07900)

## Capabilities

- 1B-class SOTA: reasoning, code, tool use, instruction following
- Hybrid reasoning: enable_thinking=True/False on same checkpoint
- Tool calling via SGLang (OpenAI-compatible)
- 128K context; standard LlamaForCausalLM — no custom kernels
- Works: vLLM, SGLang, transformers, llama.cpp, Ollama, LM Studio, MLX

## VFX / Filmmaking Use Cases

- Local on-device agentic LLM for n8n automations without cloud API cost
- Script analysis, shot list generation, creative brief processing on-device
- Fine-tune on production-specific data for a VFX pipeline agent

## How to Run

```bash
pip install "vllm>=0.21"
vllm serve openbmb/MiniCPM5-1B --port 8000
```