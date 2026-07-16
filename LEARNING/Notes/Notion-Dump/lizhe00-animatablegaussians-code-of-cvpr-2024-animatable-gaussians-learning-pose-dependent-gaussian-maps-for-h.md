---
title: lizhe00/AnimatableGaussians: Code of [CVPR 2024] "Animatable Gaussians: Learning Pose-dependent Gaussian Maps for High-fidelity Human Avatar Modeling"
category: note
summary: Preserved substantive Notion export for lizhe00/AnimatableGaussians: Code of [CVPR 2024] "Animatable Gaussians: Learning Pose-dependent Gaussian Maps for High-fidelity Human Avatar Modeling".
tags: [notion-import, source-preservation]
sources: 1
updated: 2026-07-16
source_path: raw/notion-dump-ingest-archive/2026-07-16/Batch-04/lizhe00 AnimatableGaussians Code of [CVPR 2024] An 4c370c7d8bf846d5816a118011ccef8b.md
ingested: 2026-07-16
---

# lizhe00/AnimatableGaussians: Code of [CVPR 2024] "Animatable Gaussians: Learning Pose-dependent Gaussian Maps for High-fidelity Human Avatar Modeling"

**Ingest batch:** [[Notion-Dump-Ingest-Batch-04]]  
**Original export:** `raw/notion-dump-ingest-archive/2026-07-16/Batch-04/lizhe00 AnimatableGaussians Code of [CVPR 2024] An 4c370c7d8bf846d5816a118011ccef8b.md`

---

# lizhe00/AnimatableGaussians: Code of [CVPR 2024] "Animatable Gaussians: Learning Pose-dependent Gaussian Maps for High-fidelity Human Avatar Modeling"

Tags: AI Video
Description: Code of [CVPR 2024] "Animatable Gaussians: Learning Pose-dependent Gaussian Maps for High-fidelity Human Avatar Modeling" - lizhe00/AnimatableGaussians
URL: https://github.com/lizhe00/AnimatableGaussians
Date Added: January 11, 2025 12:35 PM
Type: Github
Archive: No
Spark: No

![](lizhe00%20AnimatableGaussians%20Code%20of%20%5BCVPR%202024%5D%20An/stn-Kt2riwIALJgopEiXXd3wQM4cdjn6C4JaSBQzcZAH.jpeg)

News

- `09/15/2024` Release the [templates](https://github.com/user-attachments/files/17004283/ActorsHQ_templates.zip) of ActorsHQ (Actor01 & Actor04) to facilitate training.
- `05/22/2024` 📢 **An extension work of Animatable Gaussians for human avatar relighting is available [here](https://animatable-gaussians.github.io/relight). Welcome to check it!**
- `03/11/2024` The code has been released. Welcome to have a try!
- `03/11/2024` [AvatarReX](https://github.com/lizhe00/AnimatableGaussians/blob/master/AVATARREX_DATASET.md) dataset, a high-resolution multi-view video dataset for avatar modeling, has been released.
- `02/27/2024` Animatable Gaussians is accepted by CVPR 2024!

# **Animatable Gaussians**: Learning Pose-dependent Gaussian Maps for High-fidelity Human Avatar Modeling

## CVPR 2024

[Zhe Li](https://lizhe00.github.io/) 1, [Zerong Zheng](https://zhengzerong.github.io/) 2, [Lizhen Wang](https://lizhenwangt.github.io/) 1, [Yebin Liu](https://www.liuyebin.com/) 1

1Tsinghua Univserity 2NNKosmos Technology

### [Projectpage](https://animatable-gaussians.github.io/) · [Paper](https://arxiv.org/pdf/2311.16096.pdf) · [Video](https://www.youtube.com/watch?v=kOmZxD0HxZI)

teaser.mp4

***Abstract**: Modeling animatable human avatars from RGB videos is a long-standing and challenging problem. Recent works usually adopt MLP-based neural radiance fields (NeRF) to represent 3D humans, but it remains difficult for pure MLPs to regress pose-dependent garment details. To this end, we introduce Animatable Gaussians, a new avatar representation that leverages powerful 2D CNNs and 3D Gaussian splatting to create high-fidelity avatars. To associate 3D Gaussians with the animatable avatar, we learn a parametric template from the input videos, and then parameterize the template on two front & back canonical Gaussian maps where each pixel represents a 3D Gaussian. The learned template is adaptive to the wearing garments for modeling looser clothes like dresses. Such template-guided 2D parameterization enables us to employ a powerful StyleGAN-based CNN to learn the pose-dependent Gaussian maps for modeling detailed dynamic appearances. Furthermore, we introduce a pose projection strategy for better generalization given novel poses. Overall, our method can create lifelike avatars with dynamic, realistic and generalized appearances. Experiments show that our method outperforms other state-of-the-art approaches.*

## Demo Results

We show avatars animated by challenging motions from [AMASS](https://amass.is.tue.mpg.de/) dataset.

basketball.mp4 More results (click to expand) football.mp4 dancing.mp4 irish_dancing.mp4

# Installation

1. Clone this repo.
    
    git clone https://github.com/lizhe00/AnimatableGaussians.git
    
    # or
    
    git clone git@github.com:lizhe00/AnimatableGaussians.git
    
2. Install environments.
    
    # install requirements
    
    pip install -r requirements.txt
    
    # install diff-gaussian-rasterization-depth-alpha
    
    cd gaussians/diff_gaussian_rasterization_depth_alpha
    python setup.py install
    cd ../..
    
    # install styleunet
    
    cd network/styleunet
    python setup.py install
    cd ../..
    
3. Download [SMPL-X](https://smpl-x.is.tue.mpg.de/download.php) model, and place pkl files to `./smpl_files/smplx`.

# Data Preparation

## AvatarReX, ActorsHQ or THuman4.0 Dataset

1. Download [AvatarReX](https://github.com/lizhe00/AnimatableGaussians/blob/master/AVATARREX_DATASET.md), [ActorsHQ](https://www.actors-hq.com/dataset), or [THuman4.0](https://github.com/ZhengZerong/THUman4.0-Dataset) datasets.
2. Data preprocessing. We provide two manners below. The first way is recommended if you plan to employ our pretrained models, because the renderer utilized in preprocessing may cause slight differences.
    1. (Recommended) Download our preprocessed files from [PREPROCESSED_DATASET.md](https://github.com/lizhe00/AnimatableGaussians/blob/master/PREPROCESSED_DATASET.md), and unzip them to the root path of each character.
    2. Follow the instructions in [gen_data/GEN_DATA.md](https://github.com/lizhe00/AnimatableGaussians/blob/master/gen_data/GEN_DATA.md#Preprocessing) to preprocess the dataset.

*Note for ActorsHQ dataset: 1) **DATA PATH.** The subject from ActorsHQ dataset may include more than one sequences, but we only utilize the first sequence, i.e., `Sequence1`. The root path is `ActorsHQ/Actor0*/Sequence1`. 2) **SMPL-X Registration.** We provide SMPL-X fitting for ActorsHQ dataset. You can download it from [here](https://drive.google.com/file/d/1DVk3k-eNbVqVCkLhGJhD_e9ILLCwhspR/view?usp=sharing), and place `smpl_params.npz` at the corresponding root path of each subject.*

## Customized Dataset

Please refer to [gen_data/GEN_DATA.md](https://github.com/lizhe00/AnimatableGaussians/blob/master/gen_data/GEN_DATA.md) to run on your own data.

# Avatar Training

Take `avatarrex_zzr` from AvatarReX dataset as an example, run:

```
python main_avatar.py -c configs/avatarrex_zzr/avatar.yaml --mode=train
```

After training, the checkpoint will be saved in `./results/avatarrex_zzr/avatar`.

# Avatar Animation

1. Download pretrained checkpoint from [PRETRAINED_MODEL.md](https://github.com/lizhe00/AnimatableGaussians/blob/master/PRETRAINED_MODEL.md), unzip it to `./results/avatarrex_zzr/avatar`, or train the network from scratch.
2. Download [THuman4.0_POSE](https://drive.google.com/file/d/1pbToBV6klq6-dXCorwjjsmnINXZCG8n9/view?usp=sharing) or [AMASS](https://amass.is.tue.mpg.de/) dataset for acquiring driving pose sequences. We list some awesome pose sequences from AMASS dataset in [configs/awesome_amass_poses.yaml](https://github.com/lizhe00/AnimatableGaussians/blob/master/configs/awesome_amass_poses.yaml). Specify the testing pose path in [configs/avatarrex_zzr/avatar.yaml#L57](https://github.com/lizhe00/AnimatableGaussians/blob/master/configs/avatarrex_zzr/avatar.yaml#L57).
3. Run:
    
    python main_avatar.py -c configs/avatarrex_zzr/avatar.yaml --mode=test
    

You will see the animation results like below in `./test_results/avatarrex_zzr/avatar`.

example_animation.mp4

# Evaluation

We provide evaluation metrics and example codes of comparison with body-only avatars in [eval/comparison_body_only_avatars.py](https://github.com/lizhe00/AnimatableGaussians/blob/master/eval/comparison_body_only_avatars.py).

# Todo

- Release the code.
- Release AvatarReX dataset.
- Release all the checkpoints and preprocessed dataset. Cancelled due to graduation. Please run on other cases yourself with the provided [configs](https://github.com/lizhe00/AnimatableGaussians/blob/master/configs).

# Acknowledgement

Our code is based on these wonderful repos:

- [3D Gaussian Splatting](https://github.com/graphdeco-inria/diff-gaussian-rasterization) and its [adapted version](https://github.com/ashawkey/diff-gaussian-rasterization)
- [StyleAvatar](https://github.com/LizhenWangT/StyleAvatar)

# Citation

If you find our code or data is helpful to your research, please consider citing our paper.

@inproceedings{li2024animatablegaussians,
title={Animatable Gaussians: Learning Pose-dependent Gaussian Maps for High-fidelity Human Avatar Modeling},
author={Li, Zhe and Zheng, Zerong and Wang, Lizhen and Liu, Yebin},
booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
year={2024}
}
