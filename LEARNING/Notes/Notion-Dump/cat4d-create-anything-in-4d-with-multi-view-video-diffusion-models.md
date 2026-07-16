---
title: CAT4D: Create Anything in 4D with Multi-View Video Diffusion Models
category: note
summary: Preserved substantive Notion export for CAT4D: Create Anything in 4D with Multi-View Video Diffusion Models.
tags: [notion-import, source-preservation]
sources: 1
updated: 2026-07-16
source_path: raw/notion-dump-ingest-archive/2026-07-16/Batch-01/CAT4D Create Anything in 4D with Multi-View Video  5391bd660c164aa88e3fabd951a677e5.md
ingested: 2026-07-16
---

# CAT4D: Create Anything in 4D with Multi-View Video Diffusion Models

**Ingest batch:** [[Notion-Dump-Ingest-Batch-01]]  
**Original export:** `raw/notion-dump-ingest-archive/2026-07-16/Batch-01/CAT4D Create Anything in 4D with Multi-View Video  5391bd660c164aa88e3fabd951a677e5.md`

---

# CAT4D: Create Anything in 4D with Multi-View Video Diffusion Models

Tags: AI Video
Description: We present CAT4D, a method for creating 4D (dynamic 3D) scenes from monocular video. CAT4D leverages a multi-view video diffusion model trained on a diverse combination of datasets to enable novel view synthesis at any specified camera poses and timestamps. Combined with a novel sampling approach, this model can transform a single monocular video into a multi-view video, enabling robust 4D reconstruction via optimization of a deformable 3D Gaussian representation.  We demonstrate competitive performance on novel view synthesis and dynamic scene reconstruction benchmarks, and highlight the creative capabilities for 4D scene generation from real or generated videos.
URL: https://cat-4d.github.io/
Date Added: January 11, 2025 1:13 PM
Type: Article
Archive: No
Spark: No

![](CAT4D%20Create%20Anything%20in%204D%20with%20Multi-View%20Video%20/stn-DXd1lEq4BOQss5mVe0zOoQQP7oEhEOz8sTeX6Gu4.jpeg)

- [Rundi Wu¹𝄒²](https://www.cs.columbia.edu/~rundi/)
- [Ruiqi Gao¹](https://ruiqigao.github.io/)
- [Ben Poole¹](https://poolio.github.io/)
- [Alex Trevithick¹𝄒³](https://alextrevithick.github.io/)
- [Changxi Zheng²](https://www.cs.columbia.edu/~cxz/index.htm/)
- [Jonathan T. Barron¹](https://jonbarron.info/)
- [Aleksander Holynski¹](https://holynski.org/)

¹Google DeepMind      ²Columbia University      ³UC San Diego

[arXiv](https://arxiv.org/abs/2411.18613)

### **TL;DR**: CAT4D creates 4D scenes from real or generated videos.

### How it works

Given an input monocular video, we generate multi-view videos at novel viewpoints using our multi-view video diffusion model. These generated videos are then used to reconstruct the dynamic 3D scene as deforming 3D Gaussians.

An animated diagram briefly describing the method. On the left, an input image is shown. Next are samples from the diffusion model (5 secs), with a spinning camera path. Finally, it shows the optimized 3D Model obtained by optimizing a NeRF (55 seconds).

### Interactive Viewer

Click on the images below to render 4D scenes in real-time in your browser, powered by [Brush](https://github.com/ArthurBrussee/brush)!
Note that this is experimental and quality may be reduced.

![](https://cat-4d.github.io/videos/viewer_thumbnails/genmo-coffee-machine.png)

![](https://cat-4d.github.io/videos/viewer_thumbnails/genmo-dog-holding-teddybear.png)

![](https://cat-4d.github.io/videos/viewer_thumbnails/genmo-mice-on-pizza.png)

![](https://cat-4d.github.io/videos/viewer_thumbnails/genmo-two-babies-dancing.png)

![](https://cat-4d.github.io/videos/viewer_thumbnails/hailuo-bee.png)

![](https://cat-4d.github.io/videos/viewer_thumbnails/hailuo-rabbit-snow.png)

![](https://cat-4d.github.io/videos/viewer_thumbnails/kling-0689-girl.png)

![](https://cat-4d.github.io/videos/viewer_thumbnails/kling-6210-cat.png)

![](https://cat-4d.github.io/videos/viewer_thumbnails/kling-baby-dragon-in-bowl.png)

![](https://cat-4d.github.io/videos/viewer_thumbnails/kling-baby-panda-in-hand.png)

![](https://cat-4d.github.io/videos/viewer_thumbnails/kling-bee-on-rice-flower.png)

![](https://cat-4d.github.io/videos/viewer_thumbnails/kling-bird-in-snow-cartoon.png)

![](https://cat-4d.github.io/videos/viewer_thumbnails/kling-bulldog-swing.png)

![](https://cat-4d.github.io/videos/viewer_thumbnails/kling-cat-kneading2.png)

![](https://cat-4d.github.io/videos/viewer_thumbnails/kling-cat-potato-in-water.png)

![](https://cat-4d.github.io/videos/viewer_thumbnails/kling-cat-swing-in-snow.png)

![](https://cat-4d.github.io/videos/viewer_thumbnails/kling-chemical-lab-fire.png)

![](https://cat-4d.github.io/videos/viewer_thumbnails/kling-coffee.png)

![](https://cat-4d.github.io/videos/viewer_thumbnails/kling-ecEDleSS-pig.png)

![](https://cat-4d.github.io/videos/viewer_thumbnails/kling-forest-elf-fire.png)

![](https://cat-4d.github.io/videos/viewer_thumbnails/kling-kungfu-cat.png)

![](https://cat-4d.github.io/videos/viewer_thumbnails/kling-mood-fast-play.png)

![](https://cat-4d.github.io/videos/viewer_thumbnails/kling-panda-playing-guitar.png)

![](https://cat-4d.github.io/videos/viewer_thumbnails/kling-turtle-violin.png)

![](https://cat-4d.github.io/videos/viewer_thumbnails/pexels-dog5.png)

![](https://cat-4d.github.io/videos/viewer_thumbnails/pexels-lucky-cat.png)

![](https://cat-4d.github.io/videos/viewer_thumbnails/pexels-penguin.png)

![](https://cat-4d.github.io/videos/viewer_thumbnails/pika-deflate-sumo.png)

![](https://cat-4d.github.io/videos/viewer_thumbnails/sora-mammoths.png)

### Separate camera and time control

At the core of CAT4D is a multi-view video diffusion model that disentangles the controls of camera and scene motions. We demonstrate this by generating three types of output sequences given 3 input images (with camera poses): 1) fixed viewpoint and varying time, 2) varying viewpoint and fixed time, and 3) varying viewpoint and varying time.

Input

Fixed View
Varying Time

Varying View
Fixed Time

Varying View
Varying Time

![](https://cat-4d.github.io/videos/cameartime_ours/wt0000.png)

![](https://cat-4d.github.io/videos/cameartime_ours/wt0409.png)

![](https://cat-4d.github.io/videos/cameartime_ours/wt0177.png)

![](https://cat-4d.github.io/videos/cameartime_ours/backpack.png)

![](https://cat-4d.github.io/videos/cameartime_ours/block.png)

![](https://cat-4d.github.io/videos/cameartime_ours/haru-sit.png)

![](https://cat-4d.github.io/videos/cameartime_ours/wt0013.png)

![](https://cat-4d.github.io/videos/cameartime_ours/pillow.png)

![](https://cat-4d.github.io/videos/cameartime_ours/space-out.png)

![](https://cat-4d.github.io/videos/cameartime_ours/wt0120.png)

![](https://cat-4d.github.io/videos/cameartime_ours/umbrella.png)

### Comparisons

Compare our method to baselines on different tasks. Try selecting different tasks and scenes!

Comparison of dynamic scene reconstruction from monocular videos on the DyCheck dataset.

4D-GS

Shape-of-Motion

MoSca

Ours

Ground Truth

Input

![](https://cat-4d.github.io/videos/dycheck/apple.png)

![](https://cat-4d.github.io/videos/dycheck/block.png)

![](https://cat-4d.github.io/videos/dycheck/paper-windmill.png)

![](https://cat-4d.github.io/videos/dycheck/spin.png)

![](https://cat-4d.github.io/videos/dycheck/teddy.png)

### Acknowledgements

We would like to thank Arthur Brussee, Philipp Henzler, Daniel Watson, Jiahui Lei, Hang Gao, Qianqian Wang, Songyou Peng, Stan Szymanowicz, Jiapeng Tang, Hadi Alzayer, Dana Roth, and Angjoo Kanazawa for their valuable contributions. We also extend our gratitude to Shlomi Fruchter, Kevin Murphy, Mohammad Babaeizadeh, Han Zhang, and Amir Hertz for training the base text-to-image latent diffusion model.

### BibTeX

AخA

@article{wu2024cat4d,

title={{CAT4D: Create Anything in 4D with Multi-View Video Diffusion Models}},

author={Wu, Rundi and Gao, Ruiqi and Poole, Ben and Trevithick, Alex and Zheng, Changxi and Barron, Jonathan T. and Holynski, Aleksander}

journal={arXiv:2411.18613},

year={2024}

}

An animated illustrated cat paws at an image. It turns into a 3D cat head!
