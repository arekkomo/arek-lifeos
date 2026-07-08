# EMOPortraits: Emotion-enhanced Multimodal One-shot Head Avatars

Tags: AI Video
URL: https://neeek2303.github.io/EMOPortraits/
Date Added: January 11, 2025 10:23 AM
Type: Article
Archive: No
Spark: No

![](EMOPortraits%20Emotion-enhanced%20Multimodal%20One-shot%20/stn-03Yor5tXxPJQt6oqjriJidvh2eZxYNOaF6eBiB0I.jpeg)

![](https://neeek2303.github.io/EMOPortraits/static/images/toni.png)

[Antoni Bigata](chrome-extension://ldmmifpegigmeammaeckplhnjbbpccmm/popup/index.html)
[Casademunt](chrome-extension://ldmmifpegigmeammaeckplhnjbbpccmm/popup/index.html)

![](https://neeek2303.github.io/EMOPortraits/static/images/dino.png)

[Konstantinos](chrome-extension://ldmmifpegigmeammaeckplhnjbbpccmm/popup/index.html)
[Vougioukas](chrome-extension://ldmmifpegigmeammaeckplhnjbbpccmm/popup/index.html)

![](https://neeek2303.github.io/EMOPortraits/static/images/zoe.png)

[Zoe](chrome-extension://ldmmifpegigmeammaeckplhnjbbpccmm/popup/index.html)
[Landgraf](chrome-extension://ldmmifpegigmeammaeckplhnjbbpccmm/popup/index.html)

![](https://neeek2303.github.io/EMOPortraits/static/images/stavros.png)

[Stavros](chrome-extension://ldmmifpegigmeammaeckplhnjbbpccmm/popup/index.html)
[Petridis](chrome-extension://ldmmifpegigmeammaeckplhnjbbpccmm/popup/index.html)

![](https://neeek2303.github.io/EMOPortraits/static/images/maja.png)

[Maja](chrome-extension://ldmmifpegigmeammaeckplhnjbbpccmm/popup/index.html)
[Pantic](chrome-extension://ldmmifpegigmeammaeckplhnjbbpccmm/popup/index.html)

[Imperial College London](https://www.imperial.ac.uk/)

CVPR 2024

- 
    
    ### [**ArXiv**](https://arxiv.org/abs/2404.19110)
    
- 
    
    ### [**Paper PDF**](https://neeek2303.github.io/EMOPortraits/static/emoportraits_cvpr.pdf)
    
- 
    
    ### [**Dataset (to be released by 06/2024)**](https://github.com/neeek2303/FEED)
    
- 
    
    ### [**Code (to be released by 07/2024)**](https://github.com/neeek2303/EMOPortraits)
    

## Abstract

Head avatars animated by visual signals are increasingly popular in scenarios where the animator and character differ, a challenging yet practical approach. Our analysis revealed limitations in the existing model's handling of intense facial movements. To address this, we introduced the EMOPortraits model, which significantly improves the realism of intense and asymmetric expressions, achieving top results in emotion transfer. We also added a speech-driven mode to enhance audio-visual facial animation. Additionally, we created a unique multi-view video dataset to better represent intense and varied expressions, addressing a notable gap in current datasets.

![](https://neeek2303.github.io/EMOPortraits/static/images/more_img/traser.png)

We propose a method to instantly create high-resolution human avatars through a two-stage training process, with an optional audio-driven phase for video generation from a single image and audio input. Our standard training approach involves selecting two random frames—source and driver—from our dataset at each step. The model adapts the driver frame's motion and expressions onto the source frame to generate the final image. Effective learning is achieved when both frames originate from the same video, enhancing the model's accuracy in matching the driver frame.

## Main scheme

![](https://neeek2303.github.io/EMOPortraits/static/images/more_img/EP_sch.png)

## Speech driven examples

## BibTeX

```
@misc{drobyshev2024emoportraits,
      title={EMOPortraits: Emotion-enhanced Multimodal One-shot Head Avatars}, 
      author={Nikita Drobyshev and Antoni Bigata Casademunt and Konstantinos Vougioukas and Zoe Landgraf and Stavros Petridis and Maja Pantic},
      year={2024},
      eprint={2404.19110},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```