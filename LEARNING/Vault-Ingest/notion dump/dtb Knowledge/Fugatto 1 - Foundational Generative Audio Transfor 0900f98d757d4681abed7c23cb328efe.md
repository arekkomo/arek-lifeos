# Fugatto 1 - Foundational Generative Audio Transformer Opus 1 | Research

Tags: AI Music
Description: Fugatto is a versatile audio synthesis and transformation model capable of followingfree-form text instructions with optional audio inputs. While large languagemodels (LLMs) trained with text on a simple next-token prediction objective canlearn to infer instructions directly from the data, models trained solely on audiodata lack this capacity. This is because audio data does not inherently contain theinstructions that were used to generate it. To overcome this challenge, we introduce
URL: https://research.nvidia.com/publication/2024-11_fugatto-1-foundational-generative-audio-transformer-opus-1
Date Added: January 10, 2025 12:05 AM
Type: Article
Archive: No
Spark: No

![](Fugatto%201%20-%20Foundational%20Generative%20Audio%20Transfor/stn-2M1hjuFh6clz2ZkOAmoKcKlv9JiOdXH5t0ErCUBu.jpeg)

1. [Publications](https://research.nvidia.com/publications)
2. Fugatto 1 - Foundational Generative Audio Transformer Opus 1

![](https://research.nvidia.com/sites/default/files/styles/wide/public/publications/Screenshot%202024-12-03%20at%204.29.01%20PM.png?itok=tA7Cym0a)

***Fugatto*** is a versatile audio synthesis and transformation model capable of following
free-form text instructions with optional audio inputs. While large language
models (LLMs) trained with text on a simple next-token prediction objective can
learn to infer instructions directly from the data, models trained solely on audio
data lack this capacity. This is because audio data does not inherently contain the
instructions that were used to generate it. To overcome this challenge, we introduce
a specialized dataset generation approach optimized for producing a wide range of
audio generation and transformation tasks, ensuring the data reveals meaningful
relationships between audio and language. Another challenge lies in achieving
compositional abilities – such as combining, interpolating between, or negating
instructions – using data alone. To address it, we propose ***ComposableAR*T**, an
inference-time technique that extends classifier-free guidance to compositional
guidance. It enables the seamless and flexible composition of instructions, leading
to highly customizable audio outputs outside the training distribution. Our evaluations
across a diverse set of tasks demonstrate that ***Fugatto*** performs competitively
with specialized models, while ***ComposableART*** enhances its sonic palette and
control over synthesis. Most notably, we highlight our framework’s ability to
synthesize emergent sounds – sonic phenomena that transcend conventional audio
generation – unlocking new creative possibilities. [Demo Website](https://fugatto.github.io/).

## Authors

Rafael Valle (NVIDIA)

Rohan Badlani (NVIDIA)

Zhifeng Kong (NVIDIA)

Sang-gil Lee (NVIDIA)

Arushi Goel (NVIDIA)

Sungwon Kim (NVIDIA)

Joao Felipe Santos (NVIDIA)

Shuqi Dai (NVIDIA)

[Siddharth Gururani](https://research.nvidia.com/person/siddharth-gururani)

Aya AIJa'fari (NVIDIA)

Alex Liu (NVIDIA)

Kevin Shih (NVIDIA)

Wei Ping (NVIDIA)

[Huck Yang](https://research.nvidia.com/person/huck-yang)

Bryan Catanzaro (NVIDIA)

## Publication Date

Monday, November 25, 2024

## Research Area

[Generative AI](https://research.nvidia.com/research-area/generative-ai)

## External Links

[Demo Website](https://fugatto.github.io/)

## Uploaded Files

[FUGATTO.pdf](https://d1qx31qr3h6wln.cloudfront.net/publications/FUGATTO.pdf)1.75 MB