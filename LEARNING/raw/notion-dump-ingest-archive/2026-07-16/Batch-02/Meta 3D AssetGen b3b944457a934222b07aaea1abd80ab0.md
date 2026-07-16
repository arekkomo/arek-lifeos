# Meta 3D AssetGen

Tags: AI 3D Model
Description: Meta 3D AssetGen: Text-to-Mesh Generation with High-Quality Geometry, Texture, and PBR Materials
URL: https://assetgen.github.io/
Date Added: January 10, 2025 12:37 AM
Type: Github
Archive: No
Spark: No

![](Meta%203D%20AssetGen/stn-Hu9oXzq0hinAf2nq9HwI448ENQDMgZZknykowWmR.jpeg)

# Meta 3D AssetGen: Text-to-Mesh Generation with High-Quality Geometry, Texture, and PBR Materials

## NeurIPS 2024

[Tom Monnier](https://www.tmonnier.com/)*2, [Filippos Kokkinos](https://fkokkinos.github.io/)*2, [Mahendra Kariya](https://uk.linkedin.com/in/mahendrakariya)2, [Yanir Kleiman](https://www.yanirk.com/)2, [Emilien Garreau](https://fr.linkedin.com/in/emilien-garreau-b87606ab/en)2, [Oran Gafni](https://ai.meta.com/people/218463647991453/oran-gafni/)2, [Natalia Neverova](https://uk.linkedin.com/in/natalia-neverova-14066133)2, [Andrea Vedaldi](https://www.robots.ox.ac.uk/~vedaldi/)2, [Roman Shapovalov](https://www.shapovalov.ro/)*2, [David Novotny](https://d-novotny.github.io/)*2

1Technical University of Munich, 2GenAI, Meta, *Equal Core Contributors

[Paper](https://assetgen.github.io/static/AssetGen.pdf)

[Video](https://www.youtube.com/watch?v=xY_2jAEcBa0)

![](https://assetgen.github.io/static/teaser/teaser.jpg)

## We introduce Meta 3D AssetGen, a novel text- or image-conditioned generator of 3D assets with physically-based rendering materials (top). Meta 3D AssetGen roduces meshes with detailed geometry and high-fidelity textures, and decomposes materials into albedo, metalness, and roughness (bottom left), which allows to realistically relight objects in new environments (bottom right).

Loading...

"A red-eyed tree frog"

Loading...

"A wedge of cheese on a silver platter"

Loading...

"A train engine made out of clay"

Loading...

"A metallic pug"

Loading...

"A marble bust of a mouse"

Loading...

"A toilet made out of gold"

Loading...

"A colorful mushroom growing on a log"

Loading...

"A bichon frise in academic regalia"

Press **G** to toggle between geometry and textured meshes. Press **R** to reset the view.

## Abstract

We present Meta 3D AssetGen (AssetGen), a significant advancement in text-to-3D generation which produces faithful, high-quality meshes with texture and material control. Compared to works that bake shading in the 3D object’s appearance, AssetGen outputs physically-based rendering (PBR) materials, supporting realistic relighting. AssetGen generates first several views of the object with factored shaded and albedo appearance channels, and then reconstructs colours, metalness and roughness in 3D, using a deferred shading loss for efficient supervision. It also uses a sign-distance function to represent 3D shape more reliably and introduces a corresponding loss for direct shape supervision. This is implemented using fused kernels for high memory efficiency. After mesh extraction, a texture refinement transformer operating in UV space significantly improves sharpness and details. AssetGen achieves 17% improvement in Chamfer Distance and 40% in LPIPS over the best concurrent work for few-view reconstruction, and a human preference of 72% over the best industry competitors of comparable speed, including those that support PBR.

## Video

[https://www.youtube.com/embed/xY_2jAEcBa0](https://www.youtube.com/embed/xY_2jAEcBa0)

## Relightability of Assets

Meta 3D AssetGen is able to generate assets with varying material properties, which allows faithful modelling of the interaction between the object surface as the environment lighting changes. Here, we show assets generated with the prompt "A cat made of MATERIAL".

Environment 1 Environment 2 Environment 3

Loading...

Shiny Plastic

Loading...

Rock

Loading...

Shiny Silver

Loading...

Rusted Iron

[ Press **G** to toggle between geometry and textured meshes. Press **R** to reset the view. ]

## Method Overview

![](https://assetgen.github.io/static/teaser/overview.jpg)

Given a text prompt, AssetGen generates a 3D mesh with PBR materials in two stages. The first text-to-image stage (blue) predicts a 6-channel image depicting 4 views of the object with shaded and albedo colors. The second image-to-3D stage includes two steps. First, a 3D reconstructor (dubbed MetaILRM) outputs a triplane-supported SDF field converted into a mesh with textured PBR materials (orange). Then, PBR materials are enhanced with our texture refiner which recovers missing details from the input views (green).

## Related Links

For more work on similar tasks, please check out

[Gaussian Reconstruction Model](https://arxiv.org/abs/2403.14621) presents a fast, transformer-based model for efficient 3D reconstruction and generation using pixel-aligned Gaussians.

[InstantMesh](https://arxiv.org/abs/2404.07191) introduces a fast, efficient framework for generating high-quality 3D meshes from a single image using a multi-view diffusion model and sparse-view large reconstruction.

[MeshLRM](https://arxiv.org/abs/2404.12385) introduces a fast, efficient model for generating high-quality 3D meshes from just four input images using differentiable mesh extraction.

[Instant3D](https://arxiv.org/abs/2311.06214), the original pioneering feed-forward method for generating high-quality and diverse 3D assets from text prompts using a two-stage approach: generating four-view images with a fine-tuned diffusion model and reconstructing a NeRF with a transformer-based sparse-view reconstructor.

[LightplaneLRM](https://lightplane.github.io/) add highly scalable splatting and rendering kernels to Instant3D's large reconstruction model, improving performance.

[LumaAI Genie](https://lumalabs.ai/genie?view=create) and [Meshy 3](https://www.meshy.ai/) are commercial softwares for creating relightable assets from text prompts.

## BibTeX

```
@article{siddiqui2024assetgen,
    author = {Yawar Siddiqui and Tom Monnier and Filippos Kokkinos and Mahendra Kariya and Yanir Kleiman and Emilien Garreau and Oran Gafni and Natalia Neverova and Andrea Vedaldi and Roman Shapovalov and David Novotny},
    title = {Meta 3D AssetGen: Text-to-Mesh Generation with High-Quality Geometry, Texture, and PBR Materials},
    journal = {arXiv},
    year = {2024},
}
```