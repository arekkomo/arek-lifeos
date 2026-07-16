# X-Portrait 2: Highly Expressive Portrait Animation

Tags: AI Avatar, AI Video
Description: X-Portrait 2: Highly Expressive Portrait Animation
URL: https://byteaigc.github.io/X-Portrait2/
Date Added: January 11, 2025 1:17 PM
Type: Article
Archive: No
Spark: No

![](X-Portrait%202%20Highly%20Expressive%20Portrait%20Animation/stn-gKLaGiWVDjwsgkVOLeI4Em1jXBMQU2gjkv6OCdKh.jpeg)

[Hongyi Xu](https://hongyixu37.github.io/homepage/)1, [Guoxian Song](https://guoxiansong.github.io/homepage/index.html)1, [You Xie](https://scholar.google.com/citations?user=FV0eXhQAAAAJ&hl=en)1, [Chenxu Zhang](https://zhangchenxu528.github.io/)1, [Xiu Li](https://lixiulive.com/)1, [Linjie Luo](http://linjieluo.com/)1, [Jinli Suo](https://scholar.google.com/citations?user=e4lel8QAAAAJ&hl=zh-CN)2, [Yebin Liu](http://www.liuyebin.com/)2,

1ByteDance Inc., 2Tsinghua University

Portrait animation technology provides a ultra-low cost and highly effective way to creating expressive, realistic character animations and video footages: users only need to provide a static portrait image and a driving performance video, and the model can then use these inputs to generate videos by transferring the driving expression to the subject in the portrait. This can drastically reduce the complexity of existing motion capture, character animation and content creation pipeline.

## Introducing X-Portrait 2

We introduce X-Portrait 2, which builds upon our previous work X-Portrait and brings the expressiveness of portrait animation to a whole new level. To achieve this, we build a state-of-the-art expression encoder model that implicitly encodes every minuscule expressions from the input by training it on large-scale datasets. This encoder is then combined with powerful generative diffusion models to generate fluid and expressive videos. Our X-Portrait 2 model can transfer subtle and minuscule facial expressions from the actors as well as challenging expressions including pouting, tougue-out, cheek-puffing and frowning. High fidelity of emotion preservation can also be achieved in the generated videos.

## Appearance and Motion Disentanglement

We ensure strong disentanglement of appearance and motion in training our expression encoder such that the encoder only pay attention to the expression-related information in the driving video. Our model can achieve strong cross-style and cross-domain expression transfer, covering both realistic portraits and cartoon images. This makes our model highly adaptive to a wide range of use cases including real-world storytelling, character animation, virtual agents and visual effects.

## Comparison to State-of-the-Art Methods

Comparing to state-of-the-art methods, such as [X-Portrait](https://byteaigc.github.io/x-portrait/) and recently-released [Runyway Act-One](https://runwayml.com/research/introducing-act-one), our model can faithfully transfer fast head movements, minuscule expression changes and strong personal emotions. These aspects are crucial for high-quality animated content creation, such as those in the animation and movie productions.

## Acknowledgment & Disclaimer

The video clips used as driving videos on this webpage are sourced from [Pexels](https://www.pexels.com/), [NeRSemble dataset](https://tobias-kirschstein.github.io/nersemble/), [DFEW dataset](https://dfew-dataset.github.io/), and movie Fences (2016), No Strings Attached (2011), It Ends With Us (2024), I Need You (2010), Face Off (1997) and The Shining (1980). The static images used as reference are sourced from [Pexels](https://www.pexels.com/), [Midjourney](https://www.midjourney.com/home) and [Deviantart](https://www.deviantart.com/). These materials are used solely for research and demonstration purposes under the principles of fair use, and no copyright infringement is intended. If you are a copyright holder and believe that our use of your video materials is inappropriate or violates copyright laws, please [contact us](mailto:linjie.luo@bytedance.com), and we will promptly address the matter. This webpage is based on [nerfies](https://nerfies.github.io/) template.