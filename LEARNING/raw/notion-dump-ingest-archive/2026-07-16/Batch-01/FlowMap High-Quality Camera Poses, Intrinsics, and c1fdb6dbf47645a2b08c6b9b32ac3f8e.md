# FlowMap: High-Quality Camera Poses, Intrinsics, and Depth via Gradient Descent

Tags: AI 3D Model
Description: FlowMap uses flow- and tracking-based losses to produce high-quality camera poses, intrinsics, and depth via gradient descent.
URL: https://cameronosmith.github.io/flowmap/
Date Added: January 11, 2025 11:25 AM
Type: Github
Archive: No
Spark: No

![](FlowMap%20High-Quality%20Camera%20Poses,%20Intrinsics,%20and/stn-t1kGcs7TkXrJ7XRhBji6cLPykNGRxjmtLAxyODTS.jpeg)

[Cameron Smith*](https://cameronosmith.github.io/), [David Charatan*](http://davidcharatan.com/), [Ayush Tewari](https://ayushtewari.com/), and [Vincent Sitzmann](https://www.vincentsitzmann.com/)

Massachusetts Institute of Technology

* denotes joint first authorship.

[Paper](https://arxiv.org/abs/2404.15259) [Code](https://github.com/dcharatan/flowmap) [Datasets and Initialization](https://drive.google.com/drive/folders/1PqByQSfzyLjfdZZDwn6RXIECso7WB9IY?usp=drive_link)

TL;DR: FlowMap is the first self-supervised, end-to-end differentiable SfM method that provides COLMAP-level accuracy for 360° scenes.

## Abstract

This paper introduces FlowMap, an end-to-end differentiable method that solves for precise camera poses, camera intrinsics, and per-frame dense depth of a video sequence. Our method performs per-video gradient-descent minimization of a simple least-squares objective that compares the optical flow induced by depth, intrinsics, and poses against correspondences obtained via off-the-shelf optical flow and point tracking. Alongside the use of point tracks to encourage long-term geometric consistency, we introduce a differentiable re-parameterization of depth, intrinsics, and pose that is amenable to first-order optimization. We empirically show that camera parameters and dense depth recovered by our method enable photo-realistic novel view synthesis on 360° trajectories using Gaussian Splatting. Our method not only far outperforms prior gradient-descent based bundle adjustment methods, but surprisingly performs on par with COLMAP, the state-of-the-art SfM method, on the downstream task of 360° novel view synthesis - even though our method is purely gradient-descent based, fully differentiable, and presents a complete departure from conventional SfM. Our result opens the door to the self-supervised training of neural networks that perform camera parameter estimation, 3D reconstruction, and novel view synthesis.

## Overview

![](https://cameronosmith.github.io/static/images/highlevel_yoda.png)

## Point Clouds from FlowMap

The high-quality camera poses, camera intrinsics, and depths FlowMap predicts can be combined to create well-aligned, dense point clouds.

![](https://cameronosmith.github.io/static/images/point_clouds_more.png)

## Optimization Timelapse

FlowMap is trained end-to-end using gradient descent.

## Downstream 3D Gaussian Splatting

FlowMap's outputs can be used to train high-quality 3D Gaussian Splatting scenes. Reconstruction quality significantly beats NoPE-NeRF and DROID-SLAM and matches COLMAP.

Methods marked with an asterisk (*) require ground-truth intrinsics.

 

![](https://cameronosmith.github.io/static/images/nope_bonsai_marked.png)

![](https://cameronosmith.github.io/static/images/our_bonsai_marked.png)

 

![](https://cameronosmith.github.io/static/images/droid_bench_marked.png)

![](https://cameronosmith.github.io/static/images/our_bench_marked.png)

 

![](https://cameronosmith.github.io/static/images/colmap_kitchen_marked.png)

![](https://cameronosmith.github.io/static/images/our_kitchen_marked_41.png)

 

![](https://cameronosmith.github.io/static/images/gt_flower_marked.png)

![](https://cameronosmith.github.io/static/images/our_flower_marked.png)

Note that because we fit a smooth trajectory to each method's estimated poses, the alignment in the videos below is imperfect.

## Pose Plots

Raw poses and depths from FlowMap are shown below.

## More Downstream Splatting Results

FlowMap's outputs allow Gaussian Splatting to produce crisp features and depths.