# Stability-AI/stable-point-aware-3d: SPAR3D: Stable Point-Aware Reconstruction of 3D Objects from Single Images

Tags: AI 3D Model
Description: SPAR3D: Stable Point-Aware Reconstruction of 3D Objects from Single Images - Stability-AI/stable-point-aware-3d
URL: https://github.com/Stability-AI/stable-point-aware-3d
Date Added: January 12, 2025 11:59 AM
Type: Github
Archive: No
Spark: No

![](Stability-AI%20stable-point-aware-3d%20SPAR3D%20Stable%20P/stn-CTdBBkx546t4iLXnebKSAGOf0bGfqI4Ry2phHl0M.jpeg)

# SPAR3D: Stable Point-Aware Reconstruction of 3D Objects from Single Images

  

[](https://camo.githubusercontent.com/3dd2ff9d5874de26111dfc879d281ba873cc9c6487e9b0740b1f3a13e3341959/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f41727869762d323530312e30343638392d4233314231422e737667)

[](https://camo.githubusercontent.com/83827315399b234faca720572e4860e60d1f33b21782f01ba772df5ca725afe9/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2546302539462541342539372532304d6f64656c5f436172642d48756767696e67666163652d6f72616e6765)

[](https://camo.githubusercontent.com/f5e28842fbb4447dc991bee486fbb849ca12c9c2d1ff517e69c2576e1083eb74/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f25463025394625413425393725323047726164696f25323044656d6f2d48756767696e67666163652d6f72616e6765)

![](https://github.com/Stability-AI/stable-point-aware-3d/raw/main/demo_files/turntable.gif)

This is the official codebase for **SPAR3D**, a state-of-the-art open-source model for **fast** feedforward 3D mesh reconstruction from a single image using a point cloud conditioning to improve the quality of the reconstruction.

![](https://github.com/Stability-AI/stable-point-aware-3d/raw/main/demo_files/comp.gif)

SPAR3D is based on [Stable Fast 3D](https://github.com/Stability-AI/stable-fast-3d) but improves upon the backside of the mesh by conditioning on a point cloud. This point cloud can be generated from an image using our included point cloud denoising model. This point cloud can even be edited easily in external tools or our included gradio demo. With that missing backside details can be fixed. We further improve the prediction quality of materials using novel contributions. We achieve all of this while still maintaining the fast inference speeds.

## Getting Started

### Installation

Ensure your environment is:

- Python >= 3.8 (Depending on PyTorch version >3.9)
- Optional: CUDA has to be available
- For Windows **(experimental)**: Visual Studio 2022
- Has PyTorch installed according to your platform: [https://pytorch.org/get-started/locally/](https://pytorch.org/get-started/locally/) [Make sure the Pytorch CUDA version matches your system's.]
- Update setuptools by `pip install -U setuptools==69.5.1`
- Install wheel by `pip install wheel`

Then, install the remaining requirements with `pip install -r requirements.txt`. If remeshing is required, install the additional requirements with `pip install -r requirements-remesh.txt`. For the gradio demo, an additional `pip install -r requirements-demo.txt` is required.

### Requesting Access and Login

Our model is gated at [Hugging Face](https://huggingface.co/):

1. Log in to Hugging Face and request access [here](https://huggingface.co/stabilityai/stable-point-aware-3d).
2. Create an access token with read permissions [here](https://huggingface.co/settings/tokens).
3. Run `huggingface-cli login` in the environment and enter the token.

### Low VRAM Mode

To run SPAR3D with low VRAM mode, set the environment variable `SPAR3D_LOW_VRAM=1`. By default, SPAR3D consumes 10.5GB of VRAM. This mode will reduce the VRAM consumption to roughly 7GB but in exchange the model will be slower. The `run.py` script also supports the `--low-vram-mode` flag.

### Windows Support **(experimental)**

To run Stable Fast 3D on Windows, you must install Visual Studio (currently tested on VS 2022) and the appropriate PyTorch and CUDA versions. Then, follow the installation steps as mentioned above.

Note that Windows support is **experimental** and not guaranteed to give the same performance and/or quality as Linux.

### CPU Support

CPU backend will automatically be used if no GPU is detected in your system. Note that this will be really slow.

If you have a GPU but are facing issues and want to use the CPU backend instead, set the environment variable `SPAR3D_USE_CPU=1` to force the CPU backend. The `run.py` script also supports the `--device=cpu` flag.

### Manual Inference

python run.py demo_files/examples/fish.png --output-dir output/

This will save the reconstructed 3D model as a GLB file to `output/`. You can also specify more than one image path separated by spaces. The default options takes about **6GB VRAM** for a single image input.

You may also use `--texture-resolution` to specify the resolution in pixels of the output texture and `--remesh_option` to specify the remeshing operation (None, Triangle, Quad).

For detailed usage of this script, use `python run.py --help`.

### Local Gradio App

python gradio_app.py

## ComfyUI extension

Custom nodes and an [example workflow](https://github.com/Stability-AI/stable-point-aware-3d/blob/main/demo_files/workflows/spar3d_example.json) are provided for [ComfyUI](https://github.com/comfyanonymous/ComfyUI).

To install:

- Clone this repo into `custom_nodes`:

$ cd ComfyUI/custom_nodes
$ git clone https://github.com/Stability-AI/stable-point-aware-3d

- Install dependencies:

$ cd stable-point-aware-3d
$ pip install -r requirements.txt

- Optional for remeshing:

$ pip install -r requirements-remesh.txt

- Restart ComfyUI

## Remesher Options:

-`none`: mesh unchanged after generation. No CPU overhead.

-`triangle`: verticies and edges are rearranged to form a triangle topography. Implementation is from: *"[A Remeshing Approach to Multiresolution Modeling](https://github.com/sgsellan/botsch-kobbelt-remesher-libigl)" by M. Botsch and L. Kobbelt*. CPU overhead expected.

-`quad`: verticies and edges are rearanged in quadrilateral topography with a proper quad flow. The quad mesh is split into triangles for export with GLB. Implementation is from *"[Instant Field-Aligned Meshes](https://github.com/wjakob/instant-meshes)" from Jakob et al.*. CPU overhead expected.

Additionally the target vertex or face count can be specified. This is not a hard constraint but a rough count the method aims to create. This target is ignored if the remesher is set to `none`.

## Citation

@article{spar3d2025,
title={{SPAR3D}: Stable Point-Aware Reconstruction of {3D} Objects from Single Images},
author={Huang, Zixuan and Boss, Mark and Vasishta, Aaryaman and Rehg, James Matthew and Jampani, Varun},
journal={arXiv preprint},
year={2025}
}