# GBR: Generative Bundle Refinement for High-fidelity Gaussian Splatting and Meshing

Tags: AI 3D Model
Description: soon
URL: https://gbrnvs.github.io/
Date Added: January 11, 2025 1:06 PM
Type: Article
Archive: No
Spark: No

![](GBR%20Generative%20Bundle%20Refinement%20for%20High-fidelity/stn-5XlRYVWjwAzOJpvYaRj7FhDDMszgCJVygAy2SfHg.jpeg)

   [Yuchao Zheng](chrome-extension://ldmmifpegigmeammaeckplhnjbbpccmm/popup/index.html)3 [Ziwei Li](chrome-extension://ldmmifpegigmeammaeckplhnjbbpccmm/popup/index.html)1 [Qionghai Dai](chrome-extension://ldmmifpegigmeammaeckplhnjbbpccmm/popup/index.html)3 [Xiaoyun Yuan](chrome-extension://ldmmifpegigmeammaeckplhnjbbpccmm/popup/index.html)2

1Fudan University   2Shanghai Jiao Tong University 3Tsinghua University

[Paper](https://gbrnvs.github.io/paper/GBR.pdf) [arXiv](https://arxiv.org/abs/2412.05908)

Coming soon

## Videos

## Abstract

Gaussian splatting has gained attention for its efficient representation and rendering of 3D scenes using continuous Gaussian primitives. However, it struggles with sparse-view inputs due to limited geometric and photometric information, causing ambiguities in depth, shape, and texture, as well as challenges in ensuring spatial consistency and geometry accuracy. To address these limitations, we propose GBR: Generative Bundle Refinement, a method for high-fidelity Gaussian splatting and meshing using only 4–6 input views. GBR integrates a neural bundle adjustment module for enhanced geometry accuracy and a generative depth refinement module to improve geometry fidelity. More specifically, the neural bundle adjustment module integrates a foundation network to produce initial 3D point maps and point matches from unposed images, followed by bundle optimization to improve cross-view consistency and accuracy. The generative depth refinement module employs a diffusion-based strategy to enhance geometric details and fidelity while preserving the depth scale. Finally, for Gaussian primitives learning, we propose a multimodal loss function incorporating depth and normal consistency, geometric regularization, and pseudo-view generation, providing robust guidance under sparse-view conditions. Experiments on widely-used datasets show that GBR significantly outperforms existing methods under sparse-view inputs. Additionally, GBR demonstrates the ability to reconstruct and render large-scale real scenes, such as the Great Wall, with remarkable detail using only 6 views.

## Method

![](https://gbrnvs.github.io/static/images/system.png)

Overview of our algorithm: Given sparse, pose-free camera inputs, we first employ neural Bundle Adjustment (neural-BA), combining neural-based MVS with traditional optimization techniques to obtain a dense, accurate point cloud along with precise intrinsic and extrinsic camera matrices, providing a robust initialization for 3DGS. Next, the dense point cloud is projected to obtain depth maps with accurate scale, and a diffusion process is applied to enhance the depth map resolution, resulting in scale-consistent, detail-rich depth and normal maps. These geometric constraints subsequently aid in the training of 3DGS, ultimately achieving a geometrically accurate 3DGS.

## Comparisons

## DTU meshes generated from 4 unposed images

scan_24 scan_40 scan_105

![](https://gbrnvs.github.io/static/images/cmp/ours/24_ours.png)

![](https://gbrnvs.github.io/static/images/cmp/2dgs/24_2dgs.png)

## More Results

![](https://gbrnvs.github.io/static/images/all_dtu.png)

## Mip360 & TnT normal maps generated from 6 unposed images

Ignatius Courthouse Garden Room

![](https://gbrnvs.github.io/static/images/cmp/ours/ig_ours.png)

![](https://gbrnvs.github.io/static/images/cmp/2dgs/ig_2dgs.png)

## More Results

![](https://gbrnvs.github.io/static/images/more_results.png)

## Mip360 view synthesis with 6 unposed images

Garden Room Kitchen

![](https://gbrnvs.github.io/static/images/cmp/ours/garden_ours_img.png)

![](https://gbrnvs.github.io/static/images/cmp/2dgs/garden_2dgs_img.png)

## BibTeX

```
      @misc{zhang2024gbrgenerativebundlerefinement,
        title={GBR: Generative Bundle Refinement for High-fidelity Gaussian Splatting and Meshing}, 
        author={Jianing Zhang and Yuchao Zheng and Ziwei Li and Qionghai Dai and Xiaoyun Yuan},
        year={2024},
        eprint={2412.05908},
        archivePrefix={arXiv},
        primaryClass={cs.CV},
        url={https://arxiv.org/abs/2412.05908}, 
  }
      ```
```