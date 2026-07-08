# ReVideo: Remake a Video with Motion and Content Control

Tags: AI Video
Description: Mutual Self-Attention Control
URL: https://mc-e.github.io/project/ReVideo/
Date Added: January 11, 2025 10:41 AM
Type: Github
Archive: No
Spark: No

![](ReVideo%20Remake%20a%20Video%20with%20Motion%20and%20Content%20Con/stn-G107DtlKTFYMYPxrvUjPNmA7Swf3Z4vLATN2EZrR.jpeg)

[Mingdeng Cao](https://scholar.google.com/citations?user=EcS0L5sAAAAJ&hl=en)3,4, [Xintao Wang](https://xinntao.github.io/)3✉, [Zhaoyang Zhang](https://zzyfd.github.io/)3, [Ying Shan](https://scholar.google.com/citations?user=4oXBp9UAAAAJ)3, [Jian Zhang](https://scholar.google.com/citations?user=7brFI_4AAAAJ&hl=zh-CN)1,2✉,

1School of Electronic and Computer Engineering, Shenzhen Graduate School, Peking University, 2Peking University Shenzhen Graduate School-Rabbitpre AIGC Joint Research Laboratory, 3ARC Lab, Tencent PCG, 4University of Tokyo

[arXiv](https://arxiv.org/abs/2405.13865) [Github](https://github.com/MC-E/ReVideo)

![](https://mc-e.github.io/project/ReVideo/static/assets/teaser.jpg)

## Abstract

Despite significant advancements in video generation and editing using diffusion models, achieving accurate and localized video editing remains a substantial challenge. Additionally, most existing video editing methods primarily focus on altering visual content, with limited research dedicated to motion editing. In this paper, we present a novel attempt to Remake a Video (ReVideo) which stands out from existing methods by allowing precise video editing in specific areas through the specification of both content and motion. Content editing is facilitated by modifying the first frame, while the trajectory-based motion control offers an intuitive user interaction experience. ReVideo addresses a new task involving the coupling and training imbalance between content and motion control. To tackle this, we develop a three-stage training strategy that progressively decouples these two aspects from coarse to fine. Furthermore, we propose a spatiotemporal adaptive fusion module to integrate content and motion control across various sampling steps and spatial locations. Extensive experiments demonstrate that our ReVideo has promising performance on several accurate video editing applications, i.e., (1) locally changing video content while keeping the motion constant, (2) keeping content unchanged and customizing new motion trajectories, (3) modifying both content and motion trajectories. Our method can also seamlessly extend these applications to multi-area editing without specific training, demonstrating its flexibility and robustness.

## Methods

![](https://mc-e.github.io/project/ReVideo/static/assets/method.PNG)

## Some Editing Results

Original video (Left) & Editing results (Right)

Original video (Left) & Editing results (Right)

Original video (Left) & Editing results (Right)

Original video (Left) & Editing results (Right)

Original video (Left) & Editing results (Right)

Original video (Left) & Editing results (Right)

Original video (Left) & Editing results (Right)

Original video (Left) & Editing results (Right)

Original video (Left) & Editing results (Right)

Original video (Left) & Editing results (Right)

Original video (Left) & Editing results (Right)

Original video (Left) & Editing results (Right)

Original video (Left) & Editing results (Right)

Original video (Left) & Editing results (Right)

Original video (Left) & Editing results (Right)

Original video (Left) & Editing results (Right)

Original video (Left) & Editing results (Right)

Original video (Left) & Editing results (Right)

Original video (Left) & Editing results (Right)

Original video (Left) & Editing results (Right)

Original video (Left) & Editing results (Right)

## Related Links

[1] [https://pika.art/](https://pika.art/)

[2] [DragNUWA: Fine-grained Control in Video Generation by Integrating Text, Image, and Trajectory](https://arxiv.org/abs/2308.08089)

[3] [DragAnything: Motion Control for Anything using Entity Representation](https://arxiv.org/abs/2403.07420)

[4] [AnyV2V: A Plug-and-Play Framework For Any Video-to-Video Editing Tasks](https://arxiv.org/abs/2403.14468/)