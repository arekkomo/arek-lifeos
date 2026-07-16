# Free-Moving Object Reconstruction and Pose Estimation with Virtual Camera

Tags: AI 3D Model
Description: Deformable Neural Radiance Fields creates free-viewpoint portraits (nerfies) from casually captured videos.
URL: https://haixinshi.github.io/fmov/
Date Added: January 11, 2025 11:16 AM
Type: Github
Archive: No
Spark: No

![](Free-Moving%20Object%20Reconstruction%20and%20Pose%20Estimat/stn-SMBwDAgJGx1sYiyYCx9GOFOsejm9SPBzhPojAuq7.jpeg)

[Yinlin Hu](https://scholar.google.com/citations?user=dhmdaoQAAAAJ&hl=en)2, [Daniel Koguciuk](https://scholar.google.pl/citations?user=7EEaNWQAAAAJ&hl=en)2, [Juan-Ting Lin](https://scholar.google.com/citations?user=2SmmWtQAAAAJ&hl=en)2, [Mathieu Salzmann](https://scholar.google.com/citations?user=n-B0jr4AAAAJ&hl=en)1, [David Ferstl](https://scholar.google.com/citations?user=kW1QrJYAAAAJ&hl=en)2

1EPFL, 2MagicLeap

[Paper](https://arxiv.org/pdf/2405.05858) [arXiv](https://arxiv.org/abs/2405.05858)

[Code](https://github.com/HaixinShi/fmov_pose)

* Work done as part of Haixin's Master thesis.

## Abstract

We propose an approach for reconstructing free-moving object from a monocular RGB video. Most existing methods either assume scene prior, hand pose prior, object category pose prior, or rely on local optimization with multiple sequence segments. We propose a method that allows free interaction with the object in front of a moving camera without relying on any prior, and optimizes the sequence globally without any segments. We progressively optimize the object shape and pose simultaneously based on an implicit neural representation. A key aspect of our method is a virtual camera system that reduces the search space of the optimization significantly. We evaluate our method on the standard HO3D dataset and a collection of egocentric RGB sequences captured with a head-mounted device. We demonstrate that our approach outperforms most methods significantly, and is on par with recent techniques that assume prior information.

## Results on HO3D

Our method optimizes object shape, color, and pose progressively without any segments, which produces globally-consistent results and outperforms state of the art.

**Pose results** (GT)

**Pose trajectories**

[**Hampali's](https://rgbinhandscanning.github.io/) meshes**

**Our meshes**

## Results on Egocentric Sequences

Most objects in HO3D are captured with a fixed camera and manipulated by one hand with a fixed grasping style. To verify the generalization capabilities of our methd, we collect sequences in a more general setting involving free-moving objects with a head-mounted device ([Magic Leap 2](https://www.magicleap.com/magic-leap-2)), where the objects are manipulated by both hands with a free manipulation style. While the standard joint optimization method [BARF](https://chenhsuanlin.bitbucket.io/bundle-adjusting-NeRF/) typically fails, our method produces accurate results for most objects.

**Pose results**

**Pose trajectories**

[**BARF](https://chenhsuanlin.bitbucket.io/bundle-adjusting-NeRF/)'s meshes**

**Our meshes**

## Citation

If you find this work useful in your research, please consider citing:

```
@article{shi2024fmov,
  author    = {Shi, Haixin and Hu, Yinlin and Koguciuk, Daniel and Lin, Juan-Ting and Salzmann, Mathieu and Ferstl, David},
  title     = {Free-Moving Object Reconstruction and Pose Estimation with Virtual Camera},
  journal   = {arXiv},
  year      = {2024},
}
```