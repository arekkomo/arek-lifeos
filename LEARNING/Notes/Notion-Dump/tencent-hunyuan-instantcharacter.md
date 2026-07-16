---
title: Tencent-Hunyuan/InstantCharacter
category: note
summary: Preserved substantive Notion export for Tencent-Hunyuan/InstantCharacter.
tags: [notion-import, source-preservation]
sources: 1
updated: 2026-07-16
source_path: raw/notion-dump-ingest-archive/2026-07-16/Batch-04/Tencent-Hunyuan InstantCharacter 462cefd8a4c548129d3ba1c7cd966771.md
ingested: 2026-07-16
---

# Tencent-Hunyuan/InstantCharacter

**Ingest batch:** [[Notion-Dump-Ingest-Batch-04]]  
**Original export:** `raw/notion-dump-ingest-archive/2026-07-16/Batch-04/Tencent-Hunyuan InstantCharacter 462cefd8a4c548129d3ba1c7cd966771.md`

---

# Tencent-Hunyuan/InstantCharacter

Tags: AI Image
Description: InstantCharacter is an innovative, tuning-free method designed to achieve character-preserving generation from a single image, supporting a variety of downstream tasks.
URL: https://github.com/Tencent-Hunyuan/InstantCharacter
Date Added: June 4, 2025 3:15 PM
Type: Github
Archive: No
Spark: No

![](https://github.com/Tencent-Hunyuan/InstantCharacter/raw/main/assets/1_lite.png)

# InstantCharacter: Personalize Any Characters with a Scalable Diffusion Transformer Framework

[**Jiale Tao**](https://github.com/JialeTao)1 · [**Yanbing Zhang**](https://github.com/Monalissaa)1 · [**Qixun Wang**](https://github.com/wangqixun)12✝ · [**Yiji Cheng**](https://www.linkedin.com/in/yiji-cheng-a8b922213/)1 · [**Haofan Wang**](https://haofanwang.github.io/)2 · [**Xu Bai**](https://huggingface.co/baymin0220)2 · Zhengguang Zhou 12 · [**Ruihuang Li**](https://scholar.google.com/citations?user=8CfyOtQAAAAJ&hl=zh-CN) 1 · [**Linqing Wang**](https://scholar.google.com/citations?user=Hy12lcEAAAAJ&hl=en) 12 · Chunyu Wang 1 · Qin Lin 1 · Qinglin Lu 1*

1Hunyuan, Tencent · 2InstantX Team

✝tech lead · *corresponding authors

  

[](https://camo.githubusercontent.com/9a47c9404471ba20f80320a4d0619a180cfa76fd308e1f9d2128005cc172850d/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50726f6a6563742d506167652d677265656e)

[](https://camo.githubusercontent.com/d6b4b1e610ecc1fe8ec9b99d4764cd757bc01ff06e1cc4d89fed05e607703484/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f546563686e697175652d5265706f72742d726564)

[](https://camo.githubusercontent.com/a4ff28c1dbabfaa46915ab215390308c2415c77b4b180e78909c08d74c174ad8/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f25463025394625413425393725323048756767696e67253230466163652d5370616365732d626c7565)

InstantCharacter is an innovative, tuning-free method designed to achieve character-preserving generation from a single image, supporting a variety of downstream tasks.

![](https://github.com/Tencent-Hunyuan/InstantCharacter/raw/main/assets/1_lite.png)

## Release

- [2025/05/14] 🔥 Thanks to [Zeyu Long](https://github.com/Antinomy20001) for optimizing VRAM usage - now supports [offload-inference](https://github.com/Tencent-Hunyuan/InstantCharacter/blob/main/offload_infer_demo.py) under 22GB VRAM.
- [2025/04/21] 🔥 Thanks to [jax-explorer](https://github.com/jax-explorer) for providing the [ComfyUI Wrapper](https://github.com/jax-explorer/ComfyUI-InstantCharacter).
- [2025/04/18] 🔥 We release the [demo](https://huggingface.co/spaces/InstantX/InstantCharacter) [checkpoints](https://huggingface.co/InstantX/InstantCharacter/) and [code](https://github.com/Tencent/InstantCharacter).
- [2025/04/02] 🔥 We launch the [project page](https://instantcharacter.github.io/).

## Download

You can directly download the model from [Huggingface](https://huggingface.co/InstantX/InstantCharacter).

```
huggingface-cli download --resume-download Tencent/InstantCharacter --local-dir checkpoints --local-dir-use-symlinks False
```

If you cannot access to Huggingface, you can use [hf-mirror](https://hf-mirror.com/) to download models.

```
export HF_ENDPOINT=https://hf-mirror.com
huggingface-cli download --resume-download Tencent/InstantCharacter --local-dir checkpoints --local-dir-use-symlinks False
```

Once you have prepared all models, the folder tree should be like:

```
  .
  ├── assets
  ├── checkpoints
  ├── models
  ├── infer_demo.py
  ├── pipeline.py
  └── README.md
```

## Usage

```
# !pip install transformers accelerate diffusers huggingface_cli
import torch
from PIL import Image
from pipeline import InstantCharacterFluxPipeline
# Step 1 Load base model and adapter
ip_adapter_path = 'checkpoints/instantcharacter_ip-adapter.bin'
base_model = 'black-forest-labs/FLUX.1-dev'
image_encoder_path = 'google/siglip-so400m-patch14-384'
image_encoder_2_path = 'facebook/dinov2-giant'
seed = 123456
pipe = InstantCharacterFluxPipeline.from_pretrained(base_model, torch_dtype=torch.bfloat16)
pipe.to("cuda")
pipe.init_adapter(
    image_encoder_path=image_encoder_path, 
    image_encoder_2_path=image_encoder_2_path, 
    subject_ipadapter_cfg=dict(subject_ip_adapter_path=ip_adapter_path, nb_token=1024), 
)
# Step 2 Load reference image
ref_image_path = 'assets/girl.jpg'  # white background
ref_image = Image.open(ref_image_path).convert('RGB')
# Step 3 Inference without style
prompt = "A girl is playing a guitar in street"
image = pipe(
    prompt=prompt, 
    num_inference_steps=28,
    guidance_scale=3.5,
    subject_image=ref_image,
    subject_scale=0.9,
    generator=torch.manual_seed(seed),
).images[0]
image.save("flux_instantcharacter.png")
```

You can use style lora 

![](https://github.com/Tencent-Hunyuan/InstantCharacter/raw/main/assets/style.png)

```
# download style lora
huggingface-cli download --resume-download InstantX/FLUX.1-dev-LoRA-Ghibli  --local-dir checkpoints/style_lora/ --local-dir-use-symlinks False
huggingface-cli download --resume-download InstantX/FLUX.1-dev-LoRA-Makoto-Shinkai  --local-dir checkpoints/style_lora/ --local-dir-use-symlinks False
```

```
# You can also use other style lora
# Step 3 Inference with style
lora_file_path = 'checkpoints/style_lora/ghibli_style.safetensors'
trigger = 'ghibli style'
prompt = "A girl is playing a guitar in street"
image = pipe.with_style_lora(
    lora_file_path=lora_file_path,
    trigger=trigger,
    prompt=prompt, 
    num_inference_steps=28,
    guidance_scale=3.5,
    subject_image=ref_image,
    subject_scale=0.9,
    generator=torch.manual_seed(seed),
).images[0]
image.save("flux_instantcharacter_style_ghibli.png")
# Step 3 Inference with style
lora_file_path = 'checkpoints/style_lora/Makoto_Shinkai_style.safetensors'
trigger = 'Makoto Shinkai style'
prompt = "A girl is playing a guitar in street"
image = pipe.with_style_lora(
    lora_file_path=lora_file_path,
    trigger=trigger,
    prompt=prompt, 
    num_inference_steps=28,
    guidance_scale=3.5,
    subject_image=ref_image,
    subject_scale=0.9,
    generator=torch.manual_seed(seed),
).images[0]
image.save("flux_instantcharacter_style_Makoto.png")
```

## More case

Animal character are relatively unstable. 

![](https://github.com/Tencent-Hunyuan/InstantCharacter/raw/main/assets/more_case.png)

## Acknowledgment

- Our work is sponsored by [HuggingFace](https://huggingface.co/) and [fal.ai](https://fal.ai/).

![](https://github.com/Tencent-Hunyuan/InstantCharacter/raw/main/assets/thanks_hf_fal.jpg)

- Thanks to the model JY Duan.

![](https://github.com/Tencent-Hunyuan/InstantCharacter/raw/main/assets/thanks_jyduan.jpg)

![](https://github.com/Tencent-Hunyuan/InstantCharacter/raw/main/assets/show.png)

## Cite

If you find InstantCharacter useful for your research and applications, please cite us using this BibTeX:

```
@article{tao2025instantcharacter,
  title={InstantCharacter: Personalize Any Characters with a Scalable Diffusion Transformer Framework},
  author={Tao, Jiale and Zhang, Yanbing and Wang, Qixun and Cheng, Yiji and Wang, Haofan and Bai, Xu and Zhou, Zhengguang and Li, Ruihuang and Wang, Linqing and Wang, Chunyu and others},
  journal={arXiv preprint arXiv:2504.12395},
  year={2025}
}
```

---

How to run it:

```bash

```

---
