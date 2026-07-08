# Generative Omnimatte: Learning to Decompose Video into Layers

Tags: AI Video
Description: Generative Omnimatte
URL: https://gen-omnimatte.github.io/
Date Added: January 11, 2025 1:13 PM
Type: Article
Archive: No
Spark: No

![](Generative%20Omnimatte%20Learning%20to%20Decompose%20Video%20i/stn-gxBzQgvv9VJ4Lt4eK49P0afNiYQleQaFTPIxSo7w.jpeg)

# Generative Omnimatte
Learning to Decompose Video into Layers

[Erika Lu](https://erikalu.com/)1   [Sarah Rumbley](https://scholar.google.com/citations?user=gPkCTQ0AAAAJ&hl=en)1   [Michal Geyer](https://michalgeyer.my.canva.site/)1,3   [Jia-Bin Huang](https://jbhuang0604.github.io/)2   [Tali Dekel](https://www.weizmann.ac.il/math/dekel/home)1,3   [Forrester Cole](https://people.csail.mit.edu/fcole/)1

1Google DeepMind 2University of Maryland College Park 3Weizmann Institute of Science

[arXiv](https://arxiv.org/abs/2411.16683) [Video](https://www.youtube.com/watch?v=SD-VCNvTBg4) [BibTex](https://gen-omnimatte.github.io/#BibTeX)

Input video

Omnimatte layers

 
 
 
 
 

![](https://gen-omnimatte.github.io/assets/thumbnails/lego.png)

![](https://gen-omnimatte.github.io/assets/thumbnails/boys-beach.png)

![](https://gen-omnimatte.github.io/assets/thumbnails/six-penguins.png)

![](https://gen-omnimatte.github.io/assets/thumbnails/sand-draw.png)

![](https://gen-omnimatte.github.io/assets/thumbnails/cartoon.png)

![](https://gen-omnimatte.github.io/assets/thumbnails/pickup-desert.png)

![](https://gen-omnimatte.github.io/assets/thumbnails/two-skaters.png)

![](https://gen-omnimatte.github.io/assets/thumbnails/ice-skating.png)

## Our method decomposes a video into a set of RGBA omnimatte layers,
where each layer consists of a fully-visible object and its associated effects like shadows and reflections.

## Our omnimattes enable a wide range of video editing for users. (Scroll to view more videos)

## Our omnimattes enable a wide range of video editing for users.
(Scroll to view more videos)

[https://www.youtube.com/embed/SD-VCNvTBg4](https://www.youtube.com/embed/SD-VCNvTBg4)

## Comparisons on Omnimattes

 
 
 
 
 

![](https://gen-omnimatte.github.io/assets/thumbnails/boys-beach.png)

![](https://gen-omnimatte.github.io/assets/thumbnails/boat.png)

![](https://gen-omnimatte.github.io/assets/thumbnails/two-horses.png)

![](https://gen-omnimatte.github.io/assets/thumbnails/kite-walk.png)

![](https://gen-omnimatte.github.io/assets/thumbnails/goat.png)

![](https://gen-omnimatte.github.io/assets/thumbnails/factormatte-sandcar.png)

![](https://gen-omnimatte.github.io/assets/thumbnails/factormatte-puddle.png)

![](https://gen-omnimatte.github.io/assets/thumbnails/omnimatte-rf-walk.png)

 

![](https://gen-omnimatte.github.io/assets/thumbnails/eval-dog.png)

![](https://gen-omnimatte.github.io/assets/thumbnails/eval-cars.png)

Background Foreground #1 Foreground #2

Input

Omnimatte

Omnimatte3D

OmnimatteRF

Ours

We compare our method with existing omnimatte methods ([Omnimatte](https://omnimatte.github.io/), [Omnimatte3D](https://openaccess.thecvf.com/content/CVPR2023/papers/Suhail_Omnimatte3D_Associating_Objects_and_Their_Effects_in_Unconstrained_Monocular_Video_CVPR_2023_paper.pdf), [OmnimatteRF](https://omnimatte-rf.github.io/), and [FactorMatte](https://factormatte.github.io/)). Existing methods rely on restrictive motion assumptions, such as stationary background, resulting in dynamic background elements becoming entangled with foreground object layers. Omnimatte3D and OmnimatteRF may also produce blurry background layers (e.g., horses) because their 3D-aware background representations are sensitive to camera pose estimation quality. Furthermore, these methods lack a generative and semantic prior for completing occluded pixels and accurately associating effects with their corresponding objects.

## Comparisons on Object and Effect Removal

 
 
 
 

![](https://gen-omnimatte.github.io/assets/thumbnails/cartoon.png)

![](https://gen-omnimatte.github.io/assets/thumbnails/car-puddle.png)

![](https://gen-omnimatte.github.io/assets/thumbnails/boat.png)

![](https://gen-omnimatte.github.io/assets/thumbnails/eleven-penguins.png)

![](https://gen-omnimatte.github.io/assets/thumbnails/lego.png)

![](https://gen-omnimatte.github.io/assets/thumbnails/boys-beach.png)

![](https://gen-omnimatte.github.io/assets/thumbnails/parkour.png)

 

![](https://gen-omnimatte.github.io/assets/thumbnails/eval-dodge.png)

![](https://gen-omnimatte.github.io/assets/thumbnails/eval-chair.png)

Input & object to remove

ProPainter

Lumiere-Inpainting

ObjectDrop

Ours

We compare our object-effect-removal model, Casper, with existing methods for object removal. Video inpainting models ([ProPainter](https://shangchenzhou.com/projects/ProPainter/) and [Lumiere-Inpainting](https://lumiere-video.github.io/)) fail to remove soft shadows and reflections outside the input masks. [ObjectDrop](https://objectdrop.github.io/) is an image-based model, and thus, it processes each video frame independently and inpaints regions without global context and temporal consistency. We use the same ratio of mask dilation for all the methods.

## Method

Given an input video and binary object masks, we first apply our object-effect-removal model, Casper, to generate a clean-plate background and a set of single-object (solo) videos applying different trimask conditions. The trimasks specify regions to preserve (white), remove (black), and regions that potentially contain uncertain object effects (gray). In Stage 2, a test-time optimization reconstructs the omnimatte layers Oi from pairs of solo video and background video.

![](https://gen-omnimatte.github.io/assets/images/pipeline.svg)

## Object and Effect Removal with Trimask Condition

We use different trimask conditions for an input video to obtain a set of single-object (solo) videos and a clean-plate background video (bottom row). Note that we do not cherry pick the random seeds for the Casper model. We use the same random seed (=0) for all different input videos.

Input

Trimask

Output removal

## Training data

Omnimatte Tripod Kubric Object-Paste

We collect omnimatte results from existing omnimatte methods (Omnimatte, Omnimatte3D, and OmnimatteRF) to provide examples of cause-and-effect relationships in real videos.

## Ablation Study on Training data of Casper

![](https://gen-omnimatte.github.io/assets/thumbnails/puppy-walk.png)

![](https://gen-omnimatte.github.io/assets/thumbnails/boat.png)

 

![](https://gen-omnimatte.github.io/assets/thumbnails/judo.png)

![](https://gen-omnimatte.github.io/assets/thumbnails/goat.png)

Input

Trimask

Omnimatte-only

+ Tripod

+ Kubric

+ Object-Paste (full)

We assess the individual contributions of each dataset category to our model's performance by incrementally adding each category to the training set. While the Omnimatte data provides basic examples of shadows in real-world videos, it primarily features static backgrounds and single objects. The Tripod data provides additional real-world scenarios to handle better water effects, such as reflections and boat wakes. Our Kubric synthetic data strengthens the models' ability to handle multi-object scenes. Finally, the Object-Paste data reduces undesired background changes and improves inpainting quality.

## Ablation Study on Input Condition of Casper

![](https://gen-omnimatte.github.io/assets/thumbnails/factormatte-puddle.png)

![](https://gen-omnimatte.github.io/assets/thumbnails/delivery.png)

![](https://gen-omnimatte.github.io/assets/thumbnails/red-umbrella.png)

Input

Masked RGB + binary mask

Unmasked RGB + binary mask

Unmasked RGB + Trimask (ours)

Our proposed trimask explicitly defines the regions to be removed or preserved, thereby enabling more accurate handling of multi-object scenarios. In contrast, the model trained on binary masks is susceptible to ambiguity, potentially leading to undesired removal of objects meant to be preserved.

## Our Limitations

 
 

![](https://gen-omnimatte.github.io/assets/thumbnails/trampoline.png)

![](https://gen-omnimatte.github.io/assets/thumbnails/dog-agility.png)

![](https://gen-omnimatte.github.io/assets/thumbnails/five-beagles.png)

![](https://gen-omnimatte.github.io/assets/thumbnails/bowling.png)

![](https://gen-omnimatte.github.io/assets/thumbnails/dog-crosswalk.png)

Input

Trimask

Output removal

The removal model may not always produce the desired outcome, particularly in challenging multi-object cases.

## User-specified trimask

We observe some cases where Casper will associate unrelated dynamic background effects with a foreground layer, such as the waves in the below example. To mitigate this, our system allows the user to modify the trimask by specifying a coarse preservation region to preserve the background waves better.

Click to zoom in

## Visualization of Effect Association in the Self-Attention of Video Generator

 

![](https://gen-omnimatte.github.io/assets/thumbnails/car-puddle.png)

![](https://gen-omnimatte.github.io/assets/thumbnails/parkour.png)

![](https://gen-omnimatte.github.io/assets/thumbnails/boys-beach.png)

![](https://gen-omnimatte.github.io/assets/thumbnails/five-beagles.png)

Foreground #1

Spatial Attention Block #1 Spatial Attention Block #9 Spatial Attention Block #16

Input & target object
for visualization metric

Lumiere T2V
output & attention

Lumiere Inpainting
output & attention

Our Casper
output & attention

To investigate the inherent understanding of object-effect associations in the text-to-video (T2V) Lumiere generation model, we analyze its self-attention patterns during the denoising process using SDEdit. We hypothesize that the T2V model possesses an intrinsic understanding of effect associations, allowing us to train an effective object-effect-removal model with a relatively small dataset.

We further compare the attention behaviors of the original T2V model, the Lumiere-Inpainting model, and our Casper model, which is sequentially fine-tuned from the T2V model. To ensure accurate attention measurement, we do not dilate the input mask conditions for both Inpainting and Casper models.

The visualized value of each pixel indicates the strength of association between its query token and the key tokens in the target object mask region. We visualize the first, middle, and final attention blocks of the U-Net architecture at the sampling step t=0.125. For a detailed description of the attention visualization metric, please refer to Section 3.3 of our main paper.

We observe that the T2V model's object query tokens exhibit a strong focus on the object itself, as its primary task is to **generate the object and its effects**. This tendency may also be present in the Inpainting model when it attempts to fill the mask region with another object to justify shadows. In contrast, Casper's object query tokens show less self-attention and more attention to the background region, suggesting a focus on **background completion** rather than object and effect generation.

In multi-object scenarios (

boys-beach

,

five-beagles

), the T2V and Inpainting models may associate different, similar objects with the target object. Our Casper model, however, demonstrates a lower attention response (darker) to similar objects, indicating a **stronger ability to isolate individual objects**.

We also analyzed the attention patterns of the failure case,

five-beagles

, where our Casper model did not remove the corresponding shadow completely. We hypothesize that the effect association is already weak in the T2V model, and our Casper model, inheriting knowledge from the pretrained models, struggles to handle such challenging cases.

## BibTeX

```
@article{generative-omnimatte,
  author    = {Lee, Yao-Chih and Lu, Erika and Rumbley, Sarah and Geyer, Michal and Huang, Jia-Bin and Dekel, Tali and Cole, Forrester},
  title     = {Generative Omnimatte: Learning to Decompose Video into Layers},
  journal   = {arXiv preprint arXiv:2411.16683},
  year      = {2024},
}
```