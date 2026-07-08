# Efficient Virtual View Selection for 3D Hand Pose Estimation

Tags: AI Image
URL: https://baowenz.github.io/radegs/
Date Added: January 11, 2025 10:26 AM
Type: Article
Archive: No
Spark: No

![](Efficient%20Virtual%20View%20Selection%20for%203D%20Hand%20Pose%20%206253-eb2f/stn-6ICSWXvTNa1HBpAe6luD0ocN10YfFaE6UJRvsabs.jpeg)

# Abstract

Gaussian Splatting (GS) has proven to be highly effective in novel view synthesis, achieving high-quality and real-time rendering. However, its potential for reconstructing detailed 3D shapes has not been fully explored. Existing methods often suffer from limited shape accuracy due to the discrete and unstructured nature of Gaussian splats, which complicates the shape extraction. While recent techniques like 2D GS have attempted to improve shape reconstruction, they often reformulate the Gaussian primitives in ways that reduce both rendering quality and computational efficiency. To address these problems, our work introduces a rasterized approach to render the depth maps and surface normal maps of general 3D Gaussian splats. Our method not only significantly enhances shape reconstruction accuracy but also maintains the computational efficiency intrinsic to Gaussian Splatting. Our approach achieves a Chamfer distance error comparable to NeuraLangelo on the DTU dataset and similar training and rendering time as traditional Gaussian Splatting on the Tanks & Temples dataset. Our method is a significant advancement in Gaussian Splatting and can be directly integrated into existing Gaussian Splatting-based methods.