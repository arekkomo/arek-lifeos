# MotionLCM: Real-time Controllable Motion Generation via Latent Consistency Model

Tags: AI Video
Description: MotionLCM: Real-time Controllable Motion Generation via Latent Consistency Model
URL: https://dai-wenxun.github.io/MotionLCM-page/
Date Added: January 11, 2025 10:19 AM
Type: Article
Archive: No
Spark: No

![](MotionLCM%20Real-time%20Controllable%20Motion%20Generation%20f3ae-30aa/stn-JSRmbhVfJkTP5prqlqRORpI1dHZ8tPm7TbOZavO3.jpeg)

[Ling-Hao Chen](https://lhchen.top/)1, [Jingbo Wang](https://wangjingbo1219.github.io/)2, [Jinpeng Liu](https://moonsliu.github.io/)1, [Bo Dai](https://daibo.info/)2, [Yansong Tang](https://andytang15.github.io/)1

[**ECCV 2024**](https://eccv2024.ecva.net/)

1Tsinghua University, 2Shanghai AI Laboratory

[arXiv](https://arxiv.org/abs/2404.19759)

[Video](https://www.youtube.com/watch?v=BhrGmJYaRE4)

[Code](https://github.com/Dai-Wenxun/MotionLCM) [Blogpost](https://research.lhchen.top/blogpost/motionlcm) [Demo](https://huggingface.co/spaces/wxDai/MotionLCM)

## Online Demo

# MotionLCM: Real-time Controllable Motion Generation via Latent Consistency Model

## [Wenxun Dai1](https://github.com/Dai-Wenxun/)   [Ling-Hao Chen](https://lhchen.top/)1   [Jingbo Wang](https://wangjingbo1219.github.io/)2   [Jinpeng Liu](https://moonsliu.github.io/)1   [Bo Dai](https://daibo.info/)2   [Yansong Tang](https://andytang15.github.io/)1

## 1Tsinghua University   2Shanghai AI Laboratory

Text prompt

Motion length

Motion duration in seconds: [1.8s, 9.8s] (FPS = 20).

Inference steps

Number of inference steps.

CFG

Classifier-free diffusion guidance.

GenerateClear

Inference info (runtime and device)

Real-time inference cannot be achieved using the free CPU. Local GPU deployment is recommended.

Examples

a person does a jump

a person waves both arms in the air.

The person takes 4 steps backwards.

this person bends forward as if to bow.

The person was pushed but did not fall.

a man walks forward in a snake like pattern.

a man paces back and forth along the same line.

with arms out to the sides a person walks forward

A man bends down and picks something up with his right hand.

The man walked forward, spun right on one foot and walked back to his original position.

a person slightly bent over with right hand pressing against the air walks forward slowly

Video

Video

Video

Video

Video

Video

Video

Video

![](https://dai-wenxun.github.io/MotionLCM-page/static/images/teaser_v2.png)

## Abstract

This work introduces MotionLCM, extending controllable motion generation to a real-time level. Existing methods for spatial control in text-conditioned motion generation suffer from significant runtime inefficiency. To address this issue, we first propose the motion latent consistency model (MotionLCM) for motion generation, building upon the latent diffusion model (MLD). By employing one-step (or few-step) inference, we further improve the runtime efficiency of the motion latent diffusion model for motion generation. To ensure effective controllability, we incorporate a motion ControlNet within the latent space of MotionLCM and enable explicit control signals (e.g., pelvis trajectory) in the vanilla motion space to control the generation process directly, similar to controlling other latent-free diffusion models for motion generation. By employing these techniques, our approach can generate human motions with text and control signals in real-time. Experimental results demonstrate the remarkable generation and controlling capabilities of MotionLCM while maintaining real-time runtime efficiency.

## Video

[https://www.youtube.com/embed/BhrGmJYaRE4?rel=0&showinfo=0](https://www.youtube.com/embed/BhrGmJYaRE4?rel=0&showinfo=0)

### Text-to-Motion (1-step, ~30ms/sample)

**“the person is jogging around.”**

**“a man walks forward in a snake like pattern.”**

**“the person is doing a dance move.”**

**“a hunched individual slowly wobbles forward in a drunken manner.”**

**“a person slightly bent over with right hand pressing against the air walks forward slowly”**

**“a person runs forward and stops short.”**

**“with arms out to the sides a person walks forward”**

**“a person walks in a counter counterclockwise circle.”**

**“a person does a jump”**

**“a person waves both arms in the air.”**

**“a person is doing jumping jacks”**

**“the man is throwing his right hand”**

**“this person bends forward as if to bow.”**

**“a person holds their arms near their face and searches left and right.”**

**“a man paces back and forth along the same line.”**

**“a person walks clockwise in a large curve while swinging their arms.”**

**“the person is jogging around.”**

**“a man walks forward in a snake like pattern.”**

**“the person is doing a dance move.”**

**“a hunched individual slowly wobbles forward in a drunken manner.”**

**“a person slightly bent over with right hand pressing against the air walks forward slowly”**

**“a person runs forward and stops short.”**

**“with arms out to the sides a person walks forward”**

**“a person walks in a counter counterclockwise circle.”**

**“a person does a jump”**

**“a person waves both arms in the air.”**

**“a person is doing jumping jacks”**

**“the man is throwing his right hand”**

**“this person bends forward as if to bow.”**

**“a person holds their arms near their face and searches left and right.”**

**“a man paces back and forth along the same line.”**

**“a person walks clockwise in a large curve while swinging their arms.”**

**“the person is jogging around.”**

**“a man walks forward in a snake like pattern.”**

**“the person is doing a dance move.”**

**“a hunched individual slowly wobbles forward in a drunken manner.”**

**“a person slightly bent over with right hand pressing against the air walks forward slowly”**

**“a person runs forward and stops short.”**

**“with arms out to the sides a person walks forward”**

### Motion Control (1-step, ~34ms/sample, Dense signals on pelvis)

**“a person walks using a handrail with his right hand.”**

**“a man walks around in a clockwise circle.”**

**“a person walks forward, turns around and sits on a chair.”**

**“a person taking a huge diagonal step.”**

**“the person was pushed but did not fall”**

**“a person jumps to his left.”**

**“a person walks using a handrail with his right hand.”**

**“a man walks around in a clockwise circle.”**

**“a person walks forward, turns around and sits on a chair.”**

**“a person taking a huge diagonal step.”**

**“the person was pushed but did not fall”**

**“a person jumps to his left.”**

**“a person walks using a handrail with his right hand.”**

**“a man walks around in a clockwise circle.”**

**“a person walks forward, turns around and sits on a chair.”**

**“a person taking a huge diagonal step.”**

**“the person was pushed but did not fall”**

**“a person jumps to his left.”**

**“a person walks using a handrail with his right hand.”**

### Motion Control (1-step, ~34ms/sample, Sparse signals on pelvis)

**“a person jauntily skips forward”**

**“a person walks quickly and intentionally in zig-zag pattern forward.”**

**“a man crawls forward on his stomach”**

**“person is walking with his arms out like he is balancing.”**

**“a person jauntily skips forward”**

**“a person walks quickly and intentionally in zig-zag pattern forward.”**

**“a man crawls forward on his stomach”**

**“person is walking with his arms out like he is balancing.”**

**“a person jauntily skips forward”**

**“a person walks quickly and intentionally in zig-zag pattern forward.”**

**“a man crawls forward on his stomach”**

**“person is walking with his arms out like he is balancing.”**

**“a person jauntily skips forward”**

**“a person walks quickly and intentionally in zig-zag pattern forward.”**

**“a man crawls forward on his stomach”**

## Pipeline

![](https://dai-wenxun.github.io/MotionLCM-page/static/images/pipeline.png)

## Results

![](https://dai-wenxun.github.io/MotionLCM-page/static/images/quantitative_t2m.png)

![](https://dai-wenxun.github.io/MotionLCM-page/static/images/quantitative_mc.png)

## BibTeX

```
@article{motionlcm,
      title={MotionLCM: Real-time Controllable Motion Generation via Latent Consistency Model},
      author={Dai, Wenxun and Chen, Ling-Hao and Wang, Jingbo and Liu, Jinpeng and Dai, Bo and Tang, Yansong},
      journal={arXiv preprint arXiv:2404.19759},
      year={2024}
}
```