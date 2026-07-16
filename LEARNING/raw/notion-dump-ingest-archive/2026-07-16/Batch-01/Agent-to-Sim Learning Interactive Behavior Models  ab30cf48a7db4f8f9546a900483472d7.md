# Agent-to-Sim: Learning Interactive Behavior Models from Casual Longitudinal Videos

Tags: AI Video
URL: https://gengshan-y.github.io/agent2sim-www/
Date Added: January 9, 2025 3:43 PM
Type: Article
Archive: No
Spark: No

![](Agent-to-Sim%20Learning%20Interactive%20Behavior%20Models%20/stn-OSvOazf5joiCAcaqkzAKY8AwmLCUbsu1k6jA4FPT.jpeg)

[Gengshan Yang1](https://gengshan-y.github.io/)

[Andrea Bajcsy2](https://www.cs.cmu.edu/~abajcsy/)

[Shunsuke Saito1👶🏻](https://shunsukesaito.github.io/)

[Angjoo Kanazawa3👶🏻](https://people.eecs.berkeley.edu/~kanazawa/)

1Codec Avatar Labs, Meta

2Carnegie Mellon University

3UC Berkeley

👶🏻 The last two authors equally mentored this project by both having babies

TL;DR: From monocular videos collected across a long time horizon (e.g., 1 month), we learn interactive behavior models of an agent grounded in 3D.

[https://www.youtube.com/embed/ocA22lAnmFs?si=zzVU1UQqZBtTs9Ip](https://www.youtube.com/embed/ocA22lAnmFs?si=zzVU1UQqZBtTs9Ip)

## Abstract

We present Agent-to-Sim (ATS), a framework for learning interactive behavior models of 3D agents from casual longitudinal video collections. Different from prior works that rely on marker-based tracking and multiview cameras, ATS learns natural behaviors of animal and human agents non-invasively through video observations recorded over a long time-span (e.g., a month) in a single environment. Modeling 3D behavior of an agent requires persistent 3D tracking (e.g., knowing which point corresponds to which) over a long time period. To obtain such data, we develop a coarse-to-fine registration method that tracks the agent and the camera over time through a canonical 3D space, resulting in a complete and persistent spacetime 4D representation. We then train a generative model of agent behaviors using paired data of perception and motion of an agent queried from the 4D reconstruction. ATS enables real-to-sim transfer from video recordings of an agent to an interactive behavior simulator. We demonstrate results on pets (e.g., cat, dog, bunny) and human given monocular RGBD videos captured by a smartphone.

[**[Paper]**](https://arxiv.org/abs/2410.16259) [**[Code]**](https://github.com/facebookresearch/agent2sim)

## Method Overview

![](https://gengshan-y.github.io/agent2sim-www/framework.jpg)

Agent-to-sim learns agent behavior models in 3 steps. 1) Register the scene and the agent in every video to their canonical 3D space; 2) Build a persistent 4D (3D+time) representation that contains the agent, the scene and the observer (camera). 3) Train a generative behavior model with disentangled control signals: environment, past, and the observer.

## Results: 4D Reconstruction

Left: Reconstructions from the camera view; Right: reconstructions of the environment, the agent, and the observer from bird's-eye view. Full results on each video collection: [[cat]](https://gengshan-y.github.io/agent2sim-www/materials/cat.html), [[human]](https://gengshan-y.github.io/agent2sim-www/materials/human), [[bunny]](https://gengshan-y.github.io/agent2sim-www/materials/bunny/), [[dog]](https://gengshan-y.github.io/agent2sim-www/materials/dog).

## Interaction Behavior Generation

We use the 4D reconstruction as the training data to learn an agent behavior simulator. The simulator can run at interactive speeds as you can see below.

**1. Environment awareness**. Our agent is aware of its environment. It can generate multiple environment-aware motiong given a start state.

**2. Observer awareness**. In a video, there is always someone taking the video! Since we train from video we can model how the agent would move differently given the observer motion (red triangles).

**3. Autopilot**. Our agent can also generate its own goals, which enables generating an agent behavior over a long time horizaton, conditioned on the environment and the past.

**4. User control**. We can also control the motion of an agent by manually setting the goal (the blue phere).

**5. Interactivity control**. We can control the *interactivity* of the agent by changing the classifier-free-guidance score. A higher score corresponds to an agent that us more likely to follow the conditioning signal, as shown in the first video; a lower score means the agent is more likely to move independent of the conditioning signal, as shown in the second video.

## Ablation: Conditioning Signals

**Envoronment code**. Removing environment code produces a trajectory penetrating into the wall.

**Past code**. Removing past code introduces sudden jumps between adjacent trajectory segments.

## Visualizations: Hierarchical Motion Denoising

### Goal denoising (w/ different conditioning signals)

Scenario: Exploring a room

```
 Conditioned on environment.

 Conditioned on environment and past trajectory.

 Conditioned on environment, past trajectory, and user trajectory.
```

### Path denoising (w/ different conditioning signals)

Scenario: Jumping off the sofa

```
 No environment conditioning.

 Environment conditioning.
```

### Body motion denoising

Scenario: Following a path

## Bibtex

@article{yang2024ats,
title={Agent-to-Sim: Learning Interactive Behavior Models from Casual Longitudinal Videos},
author={Yang, Gengshan and Bajcsy Andrea and Saito, Shunsuke and Kanazawa, Angjoo},
journal={arXiv preprint arXiv:2410.16259},
year={2024}
}

## Acknowledgments

We would like to thank Rawal Khirodkar, Junxuan Li, Alexander Richard, Michael Zollhoefer, Kris Kitani, and Yaser Sheikh for discussion and valuable suggestions, and Codec Avatars Team for helping with data collection.