# URAvatar: Universal Relightable Gaussian Codec Avatars

Tags: AI Avatar
Description: URAvatar: Universal Relightable Gaussian Codec Avatars
URL: https://junxuan-li.github.io/urgca-website/
Date Added: January 11, 2025 1:17 PM
Type: Article
Archive: No
Spark: No

![](URAvatar%20Universal%20Relightable%20Gaussian%20Codec%20Avat/stn-umQNXEkpWWsKjb1LMLUkRLU0KryUbsHq4qi2CJ0M.jpeg)

[Chen Cao](https://sites.google.com/site/zjucaochen/home/), [Gabriel Schwartz](https://scholar.google.com/citations?user=x47jgTcAAAAJ&hl=en), [Rawal Khirodkar](https://rawalkhirodkar.github.io/),
[Christian Richardt](https://richardt.name/), [Tomas Simon](https://scholar.google.com/citations?user=7aabHgsAAAAJ), [Yaser Sheikh](https://scholar.google.com/citations?user=Yd4KvooAAAAJ&hl=en), [Shunsuke Saito](https://shunsukesaito.github.io/)

Codec Avatars Lab, Meta

SIGGRAPH Asia 2024

[Paper](https://arxiv.org/abs/2410.24223) [arXiv](https://arxiv.org/abs/2410.24223)

## Our model is a high-fidelity **U**niversal prior for **R**elightable **Avatars**.

## You can create URAvatar (**Your Avatar**) from a phone scan.

## Here is a video showing driving different relightable avatars with the target subject (left) expression.

## Abstract

In this work, we present URAvatar, a new approach to creating photorealistic and relightable head avatars using a phone scan with unknown illumination. The reconstructed avatars can be animated and relit in real time with the global illumination of diverse environments.

Unlike existing approaches that estimate parametric reflectance parameters via inverse rendering, our approach directly models learnable radiance transfer that incorporates global light transport in an efficient manner for real-time rendering. However, learning such a complex light transport that can generalize across identities is non-trivial. A phone scan in a single environment lacks sufficient information to infer how the head would appear in general environments. To address this, we build a universal relightable avatar model represented by 3D Gaussians. We train on hundreds of high-quality multi-view human scans with controllable point lights. High-resolution geometric guidance further enhances the reconstruction accuracy and generalization.

Once trained, we finetune the pretrained model on a phone scan using inverse rendering to obtain a personalized relightable avatar. Our experiments establish the efficacy of our design, outperforming existing approaches while retaining real-time rendering capability.

![](https://junxuan-li.github.io/urgca-website/static/images/overview.png)

## URAvatar . Our approach enables the creation of drivable and relightable photorealistic head avatars from a single phone scan (left). The reconstructed avatars can be driven consistently across identities under different illuminations in real time (right).

## Method Overview

We first employ a large relightable corpus of multi-view facial performances to train a cross-identity decoder that can generate volumetric avatar representations. Then given a single phone scan of an unseen identity, we reconstruct the head pose, geometry, and albedo texture, and fine-tune our pretrained relightable prior model. Our final model provides disentangled control over relighting, gaze and neck control.

![](https://junxuan-li.github.io/urgca-website/static/images/method_overview.png)

## URAvatar from Phone Scan

### You can create URAvatar using a phone scan in any natural environment, and then relight it in various lighting conditions.

### More from Phone Scan

### Driving URAvatar with Target Expression

## BibTeX

```
        @inproceedings{li2024uravatar,
          author = {Junxuan Li and Chen Cao and Gabriel Schwartz and Rawal Khirodkar and Christian Richardt and Tomas Simon and Yaser Sheikh and Shunsuke Saito},
          title = {URAvatar: Universal Relightable Gaussian Codec Avatars}, 
          booktitle = {ACM SIGGRAPH 2024 Conference Papers},
          year = {2024},
        }
```