---
title: Google AI Proposes TransformerFAM: A Novel Transformer Architecture that Leverages a Feedback Loop to Enable the Neural Network to Attend to Its Latent Representations
category: note
summary: Preserved substantive Notion export for Google AI Proposes TransformerFAM: A Novel Transformer Architecture that Leverages a Feedback Loop to Enable the Neural Network to Attend to Its Latent Representations.
tags: [notion-import, source-preservation]
sources: 1
updated: 2026-07-16
source_path: raw/notion-dump-ingest-archive/2026-07-16/Batch-02/Google AI Proposes TransformerFAM A Novel Transfor b14715677da640cfa1e6e75f95d5d8ca.md
ingested: 2026-07-16
---

# Google AI Proposes TransformerFAM: A Novel Transformer Architecture that Leverages a Feedback Loop to Enable the Neural Network to Attend to Its Latent Representations

**Ingest batch:** [[Notion-Dump-Ingest-Batch-02]]  
**Original export:** `raw/notion-dump-ingest-archive/2026-07-16/Batch-02/Google AI Proposes TransformerFAM A Novel Transfor b14715677da640cfa1e6e75f95d5d8ca.md`

---

# Google AI Proposes TransformerFAM: A Novel Transformer Architecture that Leverages a Feedback Loop to Enable the Neural Network to Attend to Its Latent Representations

Tags: AI Automation
Description: Transformers have revolutionized deep learning, yet their quadratic attention complexity limits their ability to process infinitely long inputs. Despite their effectiveness, they suffer from drawbacks such as forgetting information beyond the attention window and needing help with long-context processing. Attempts to address this include sliding window attention and sparse or linear approximations, but they often must catch up at large scales. Drawing inspiration from neuroscience, particularly the link between attention and working memory, there's a proposed solution: incorporating attention to its latent representations via a feedback loop within the Transformer blocks, potentially leading to the emergence of working memory in
URL: https://www.marktechpost.com/2024/04/17/google-ai-proposes-transformerfam-a-novel-transformer-architecture-that-leverages-a-feedback-loop-to-enable-the-neural-network-to-attend-to-its-latent-representations/?amp
Date Added: January 11, 2025 11:51 AM
Type: Article
Archive: No
Spark: No

![](Google%20AI%20Proposes%20TransformerFAM%20A%20Novel%20Transfor/stn-GINjv4LRc0Qc24xTiAo4tkMvivg1rSep4mmQkV2V.jpeg)

![](https://www.marktechpost.com/wp-content/uploads/2024/04/Screenshot-2024-04-17-at-4.06.47-PM.png)

![](https://www.marktechpost.com/wp-content/uploads/2024/04/Screenshot-2024-04-17-at-4.06.47-PM.png)

https://arxiv.org/abs/2404.09173

Transformers have revolutionized deep learning, yet their quadratic attention complexity limits their ability to process infinitely long inputs. Despite their effectiveness, they suffer from drawbacks such as forgetting information beyond the attention window and needing help with long-context processing. Attempts to address this include sliding window attention and sparse or linear approximations, but they often must catch up at large scales. Drawing inspiration from neuroscience, particularly the link between attention and working memory, there’s a proposed solution: incorporating attention to its latent representations via a feedback loop within the Transformer blocks, potentially leading to the emergence of working memory in Transformers.

Google LLC researchers have developed TransformerFAM, a unique Transformer architecture employing a feedback loop to enable self-attention to the network’s latent representations, facilitating the emergence of working memory. This innovation improves Transformer performance on long-context tasks across various model sizes (1B, 8B, and 24B) without adding weights, seamlessly integrating with pre-trained models. TransformerFAM maintains past information indefinitely, promisingly handling infinitely long input sequences for LLMs. Without introducing new weights, TransformerFAM allows the reuse of pre-trained checkpoints. Fine-tuning TransformerFAM with LoRA for 50k steps significantly enhances performance across 1B, 8B, and 24B Flan-PaLM LLMs.

[](https://lh7-us.googleusercontent.com/PfA305g5FJL3DinEO3usws3Zu9yl0DO8nJyINQWEHnYyjpT-z1FFJOmiLEmlq_4wuicQM454jSM0EgxremRe6BeBDO7FEBFvoD68LyG8VPt-D03TEl1j-0gsBFyvAG9Ft9C1EkNPUACxAd3DMG3Uoec)

[](https://lh7-us.googleusercontent.com/PfA305g5FJL3DinEO3usws3Zu9yl0DO8nJyINQWEHnYyjpT-z1FFJOmiLEmlq_4wuicQM454jSM0EgxremRe6BeBDO7FEBFvoD68LyG8VPt-D03TEl1j-0gsBFyvAG9Ft9C1EkNPUACxAd3DMG3Uoec)

Prior attempts to incorporate feedback mechanisms in Transformers mainly focused on passing output activations from top layers to lower or intermediate ones, neglecting potential representational gaps. While some research compressed information blockwise, none ensured infinite propagation—recurrent cross-attention between blocks and feedback from upper layers integrated past information to subsequent blocks. To overcome quadratic complexity in Transformer context length approaches like sparse attention and linear approximations were explored. Alternatives to attention-based Transformers include MLP-mixer and State Space Models. TransformerFAM draws inspiration from Global Workspace Theory, aiming for a unified attention mechanism for processing various data types.

Two primary approaches are commonly employed in handling long-context inputs: increasing computational resources or implementing Sliding Window Attention (SWA). SWA, introduced by Big Bird, partitions the input into blocks, caching information block by block, a strategy termed Block Sliding Window Attention (BSWA). Unlike standard SWA, BSWA attends to all information within the ring buffer without masking out past keys and values. It employs two hyperparameters, block size, and memory segment, to control the size and scope of attended information. While BSWA offers linear complexity compared to the quadratic complexity of standard Transformers, it possesses a limited receptive field. This limitation necessitates further innovation to address long-context dependencies effectively.

FAM is developed in response to this challenge, building upon BSWA’s blockwise structure. FAM integrates feedback activations into each block, dubbed virtual activations, enabling the dynamic propagation of global contextual information across blocks. This architecture fulfills key requirements such as integrated attention, block-wise updates, information compression, and global contextual storage. Incorporating FAM enriches representations and facilitates the propagation of comprehensive contextual information, surpassing the limitations of BSWA. Despite the initial concern of potential inefficiency due to the feedback mechanism, the vectorized map-based self-attention in blocks ensures efficient training and minimal impact on memory consumption and training speed, maintaining parity with TransformerBSWA.

In the movie “Memento,” the protagonist’s struggle with anterograde amnesia parallels the current limitations of LLMs. While LLMs possess vast long-term memory capabilities, their short-term memory is restricted by attention windows. TransformerFAM offers a solution to addressing anterograde amnesia in LLMs, leveraging attention-based working memory inspired by neuroscience. The study hints at a path toward resolving the memory challenge in deep learning, a crucial precursor to tackling broader issues like reasoning. 

Check out the [**Paper.**](https://arxiv.org/abs/2404.09173) All credit for this research goes to the researchers of this project. Also, don’t forget to follow us on [**Twitter**](https://twitter.com/Marktechpost). Join our [**Telegram Channel**](https://pxl.to/at72b5j), [**Discord Channel**](https://pxl.to/8mbuwy), and [**LinkedIn Group**](https://www.linkedin.com/groups/13668564/).

**If you like our work, you will love our** [**newsletter..**](https://marktechpost-newsletter.beehiiv.com/subscribe)

Don’t Forget to join our [**40k+ ML SubReddit**](https://www.reddit.com/r/machinelearningnews/)

Want to get in front of 1.5 Million AI Audience? [**Work with us here**](https://docs.google.com/forms/d/e/1FAIpQLSejG1xG7RnIV6AJmVCfzmH3y0_pliALNo9ZIgjVeJdPAFTcwQ/viewform)

![](https://www.marktechpost.com/wp-content/uploads/2023/10/author-profile-Sana-Hassan-150x150.jpg)

![](https://www.marktechpost.com/wp-content/uploads/2023/10/author-profile-Sana-Hassan-150x150.jpg)

### [Sana Hassan](https://www.marktechpost.com/author/sana-hassan/?amp)

+ posts

Sana Hassan, a consulting intern at Marktechpost and dual-degree student at IIT Madras, is passionate about applying technology and AI to address real-world challenges. With a keen interest in solving practical problems, he brings a fresh perspective to the intersection of AI and real-life solutions.

[✅ [Recommended Read] Nebius AI Studio expands with vision models, new language models, embeddings and LoRA (Promoted)](https://nebius.com/blog/posts/studio-embeddings-vision-and-language-models?utm_medium=newsletter&utm_source=marktechpost&utm_campaign=embedding-post-ai-studio)
