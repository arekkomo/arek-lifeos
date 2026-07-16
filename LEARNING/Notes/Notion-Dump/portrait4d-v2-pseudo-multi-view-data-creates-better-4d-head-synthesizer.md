---
title: Portrait4D-v2: Pseudo Multi-View Data Creates Better 4D Head Synthesizer
category: note
summary: Preserved substantive Notion export for Portrait4D-v2: Pseudo Multi-View Data Creates Better 4D Head Synthesizer.
tags: [notion-import, source-preservation]
sources: 1
updated: 2026-07-16
source_path: raw/notion-dump-ingest-archive/2026-07-16/Batch-03/Portrait4D-v2 Pseudo Multi-View Data Creates Bette 20b12cccadb64270a926b4c9f090ddbf.md
ingested: 2026-07-16
---

# Portrait4D-v2: Pseudo Multi-View Data Creates Better 4D Head Synthesizer

**Ingest batch:** [[Notion-Dump-Ingest-Batch-03]]  
**Original export:** `raw/notion-dump-ingest-archive/2026-07-16/Batch-03/Portrait4D-v2 Pseudo Multi-View Data Creates Bette 20b12cccadb64270a926b4c9f090ddbf.md`

---

# Portrait4D-v2: Pseudo Multi-View Data Creates Better 4D Head Synthesizer

Tags: AI Video
Description: Portrait4D-v2: Pseudo Multi-View Data Creates Better 4D Head Synthesizer
URL: https://yudeng.github.io/Portrait4D-v2/
Date Added: January 11, 2025 12:23 PM
Type: Article
Archive: No
Spark: No

![](Portrait4D-v2%20Pseudo%20Multi-View%20Data%20Creates%20Bette/stn-Aef56LOhpSBafopg46KyHGscKQH4jDzjlXXgCWXz.jpeg)

# Portrait4D-v2: Pseudo Multi-View Data Creates Better 4D Head Synthesizer
ECCV 2024

Xiaobing.AI

[Paper](https://arxiv.org/abs/2403.13570)

[Video](https://www.youtube.com/watch?v=5YJY6-wcOJo)

[Code](https://github.com/YuDeng/Portrait-4D)

## Portrait4D-v2 takes a source image (left) as input and synthesizes its lifelike 4D head avatar (middle) given another driving video (right) for reenactment.

## Abstract

In this paper, we propose a novel learning approach for feed-forward one-shot 4D head avatar synthesis. Different from existing methods that often learn from reconstructing monocular videos guided by 3DMM, we employ pseudo multi-view videos to learn a 4D head synthesizer in a data-driven manner, avoiding reliance on inaccurate 3DMM reconstruction that could be detrimental to the synthesis performance. The key idea is to first learn a 3D head synthesizer using synthetic multi-view images to convert monocular real videos into multi-view ones, and then utilize the pseudo multi-view videos to learn a 4D head synthesizer via cross-view self-reenactment. By leveraging a simple vision transformer backbone with motion-aware cross-attentions, our method exhibits superior performance compared to previous methods in terms of reconstruction fidelity, geometry consistency, and motion control accuracy. We hope our method offers novel insights into integrating 3D priors with 2D supervisions for improved 4D head avatar creation.

## Video

[https://www.youtube.com/embed/5YJY6-wcOJo?rel=0&showinfo=0](https://www.youtube.com/embed/5YJY6-wcOJo?rel=0&showinfo=0)

## Framework

![](https://yudeng.github.io/Portrait4D-v2/static/images/framework.png)

Overview of our approach. Given a monocular video sampled from the training set, we first leverage a pre-trained 3D synthesizer Ψ3d to turn each driving frame within the video into multi-view one, and then use the pseudo multi-view driving frames and a source frame sampled from the original video to perform cross-view self-reenactment for learning a feed-forward 4D head synthesizer Ψ. After training, Ψ can synthesize an animatable 3D head given two arbitrary images to provide the source appearance and driving motion, respectively.

## Results

## Talking Head Synthesis

Our method can synthesize vivid 4D talking heads via video-based reenactment. It faithfully reconstructs the source appearance meanwhile mimics the nuanced expressions in different driving videos.

## Free View Rendering

Our method supports free-view rendering of the head avatars thanks to the underlying 3D representation. Use the slider below to linearly change the camera viewpoint.

![](https://yudeng.github.io/Portrait4D-v2/static/images/interpolation/stacked-00/id0002_drive0033_source.jpg)

Soure Image

![](https://yudeng.github.io/Portrait4D-v2/static/images/interpolation/stacked-00/id0002_drive0033_frame0000.jpg)

![](https://yudeng.github.io/Portrait4D-v2/static/images/interpolation/stacked-00/id0002_drive0033_target.jpg)

Driving Image

![](https://yudeng.github.io/Portrait4D-v2/static/images/interpolation/stacked-01/id0026_drive0126_source.jpg)

Soure Image

![](https://yudeng.github.io/Portrait4D-v2/static/images/interpolation/stacked-01/id0026_drive0126_frame0000.jpg)

![](https://yudeng.github.io/Portrait4D-v2/static/images/interpolation/stacked-01/id0026_drive0126_target.jpg)

Driving Image

![](https://yudeng.github.io/Portrait4D-v2/static/images/interpolation/stacked-02/id0005_drive0235_source.jpg)

Soure Image

![](https://yudeng.github.io/Portrait4D-v2/static/images/interpolation/stacked-02/id0005_drive0235_frame0000.jpg)

![](https://yudeng.github.io/Portrait4D-v2/static/images/interpolation/stacked-02/id0005_drive0235_target.jpg)

Driving Image

![](https://yudeng.github.io/Portrait4D-v2/static/images/interpolation/stacked-03/id0012_drive0191_source.jpg)

Soure Image

![](https://yudeng.github.io/Portrait4D-v2/static/images/interpolation/stacked-03/id0012_drive0191_frame0000.jpg)

![](https://yudeng.github.io/Portrait4D-v2/static/images/interpolation/stacked-03/id0012_drive0191_target.jpg)

Driving Image

![](https://yudeng.github.io/Portrait4D-v2/static/images/interpolation/stacked-04/id0010_drive0130_source.jpg)

Soure Image

![](https://yudeng.github.io/Portrait4D-v2/static/images/interpolation/stacked-04/id0010_drive0130_frame0000.jpg)

![](https://yudeng.github.io/Portrait4D-v2/static/images/interpolation/stacked-04/id0010_drive0130_target.jpg)

Driving Image

![](https://yudeng.github.io/Portrait4D-v2/static/images/interpolation/stacked-05/id0003_drive0467_source.jpg)

Soure Image

![](https://yudeng.github.io/Portrait4D-v2/static/images/interpolation/stacked-05/id0003_drive0467_frame0000.jpg)

![](https://yudeng.github.io/Portrait4D-v2/static/images/interpolation/stacked-05/id0003_drive0467_target.jpg)

Driving Image

## BibTeX

```
@article{deng2024portrait4dv2,
  title     = {Portrait4D-v2: Pseudo Multi-View Data Creates Better 4D Head Synthesizer},
  author    = {Deng, Yu and Wang, Duomin and Wang, baoyuan},
  journal   = {arXiv},
  year      = {2024},
}
```
