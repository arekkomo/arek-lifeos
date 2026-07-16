# A Hierarchical 3D Gaussian Representation for Real-Time Rendering of
    Very Large Datasets

Tags: AI Video
Description: A Hierarchical 3D Gaussian Representation for Real-Time Rendering of
        Very Large Datasets
URL: https://repo-sam.inria.fr/fungraph/hierarchical-3d-gaussians/
Date Added: January 11, 2025 10:21 AM
Type: Article
Archive: No
Spark: No

![](A%20Hierarchical%203D%20Gaussian%20Representation%20for%20Real/stn-Uazd63nXiHizCAxkISmGlSdFBEG119IiwvRgcrYw.jpeg)

SIGGRAPH 2024
(ACM Transactions on Graphics)

=================================================

[Andreas Meuleman](https://ameuleman.github.io/)* 1,2 [Georgios Kopanas](https://grgkopanas.github.io/) 1,2      [Michael Wimmer](https://scholar.google.at/citations?user=DIwQC78AAAAJ&hl=en) 3 [Alexandre Lanvin](https://scholar.google.com/citations?hl=fr&user=e1s7mGsAAAAJ)1,2 [George Drettakis](http://www-sop.inria.fr/members/George.Drettakis/) 1,2

* Both authors contributed equally to the paper.

1Inria      2Université Côte d'Azur      3TU Wien

1   2   3 

![](https://repo-sam.inria.fr/fungraph/hierarchical-3d-gaussians/content/images/inria_logo.png)

![](https://repo-sam.inria.fr/fungraph/hierarchical-3d-gaussians/content/images/uca_logo.png)

![](https://repo-sam.inria.fr/fungraph/hierarchical-3d-gaussians/content/images/tuwien_logo.jpg)

[Paper - 74MB](https://repo-sam.inria.fr/fungraph/hierarchical-3d-gaussians/hierarchical-3d-gaussians_high.pdf) [Paper - 10MB](https://repo-sam.inria.fr/fungraph/hierarchical-3d-gaussians/hierarchical-3d-gaussians_low.pdf) [Code](https://github.com/graphdeco-inria/hierarchical-3d-gaussians) [Datasets](https://repo-sam.inria.fr/fungraph/hierarchical-3d-gaussians/datasets/) [Group Publ. Page](https://www-sop.inria.fr/reves/Basilic/2024/KMKWLD24/)

![](https://repo-sam.inria.fr/fungraph/hierarchical-3d-gaussians/content/images/graphdeco_logo.png)

## Abstract

Novel view synthesis has seen major advances in recent years, with 3D Gaussian splatting offering an excellent level of visual quality, fast training and real-time rendering. However, the resources needed for training and rendering inevitably limit the size of the captured scenes that can be represented with good visual quality.

We introduce a **hierarchy** of 3D Gaussians that preserves visual quality for very large scenes, while offering an **efficient Level-of-Detail (LOD)** solution for efficient rendering of distant content with effective level selection and smooth transitions between levels. We introduce a divide-and-conquer approach that allows us to **train very large scenes** in independent chunks. We consolidate the chunks into a hierarchy that can be optimized to further improve visual quality of Gaussians merged into intermediate nodes.

Very large captures typically have sparse coverage of the scene, presenting many challenges to the original 3D Gaussian splatting training method; we adapt and regularize training to account for these is- sues. We present a complete solution, that enables **real-time rendering of very large scenes** and can adapt to available resources thanks to our LOD method. We show results for captured scenes with up to tens of thousands of images with a simple and affordable rig, covering trajectories of up to several kilometers and lasting up to one hour

## Video

[https://www.youtube.com/embed/p-mb2TzVJZk](https://www.youtube.com/embed/p-mb2TzVJZk)

## BibTeX

```
@Article{hierarchicalgaussians24,
      author       = {Kerbl, Bernhard and Meuleman, Andreas and Kopanas, Georgios and Wimmer, Michael and Lanvin, Alexandre and Drettakis, George},
      title        = {A Hierarchical 3D Gaussian Representation for Real-Time Rendering of Very Large Datasets},
      journal      = {ACM Transactions on Graphics},
      number       = {4},
      volume       = {43},
      month        = {July},
      year         = {2024},
      url          = {https://repo-sam.inria.fr/fungraph/hierarchical-3d-gaussians/}
}
```

## Acknowledgments and Funding

![](https://repo-sam.inria.fr/fungraph/hierarchical-3d-gaussians/content/images/erc.jpg)

This research was funded by the ERC Advanced grant [FUNGRAPH](http://fungraph.inria.fr/) No 788065; B.K. and M.W. acknowledge funding from WWTF (project ICT22-055: Instant Visualization and Interaction for Large Point Clouds). The authors are grateful to Adobe for generous donations, the OPAL infrastructure from Université Côte d’Azur and for the HPC resources from GENCI–IDRIS (Grant 2022-AD011014505). The authors thank the anonymous reviewers for their valuable feedback, Frédo Durand and Adrien Bousseau for proof reading and insightful comments, Sebastian Viscay for capturing SmallCity and Nikhil Mohan and colleagues at Wayve for the dataset and overall help.

## Mention information RGPD

La mention information RGPD est disponible [ici](https://repo-sam.inria.fr/fungraph/hierarchical-3d-gaussians/Mentions_information_RGPD_GRAPHDECO.pdf).

## References

[Müller 2022] Müller, T., Evans, A., Schied, C. and Keller, A., 2022. Instant neural graphics primitives with a multiresolution hash encoding

[Hedman 2018] Hedman, P., Philip, J., Price, T., Frahm, J.M., Drettakis, G. and Brostow, G., 2018. Deep blending for free-viewpoint image-based rendering. ACM Transactions on Graphics (TOG), 37(6), pp.1-15.

[Barron 2022] Barron, Jonathan T., et al. "Mip-nerf 360: Unbounded anti-aliased neural radiance fields." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2022.

[Wang et al. 2023] Wang, P., Liu, Y., Chen, Z., Liu, L., Liu, Z., Komura, T., Theobalt, C. & Wang, W. (2023). F2-nerf: Fast neural radiance field training with free camera trajectories. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition.

[Turki et al. 2022] Turki, H., Ramanan, D., & Satyanarayanan, M. (2022). Mega-nerf: Scalable construction of large-scale nerfs for virtual fly-throughs. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition.

[Kerbl and Kopanas et al. 2023] Kerbl, B., Kopanas, G., Leimkühler, T., & Drettakis, G. (2023). 3d gaussian splatting for real-time radiance field rendering. ACM Transactions on Graphics, 42(4), 1-14.