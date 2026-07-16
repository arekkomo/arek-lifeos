# physx-omni/PhysX-Omni

Tags: AI 3D Model, Github
Description: First unified framework generating simulation-ready 3D assets (rigid, deformable, articulated) with material, kinematics, affordance properties. Ships PhysXVerse dataset + PhysX-Bench.
URL: https://github.com/physx-omni/PhysX-Omni
Date Added: May 31, 2026 11:06 AM
Type: Github
Archive: No
Spark: No

## About

PhysX-Omni generates simulation-ready 3D assets across all physics categories in a unified model. Includes PhysXVerse dataset and PhysX-Bench 6-axis evaluation framework.

**GitHub:** [https://github.com/physx-omni/PhysX-Omni](https://github.com/physx-omni/PhysX-Omni)

**Dataset:** [https://huggingface.co/datasets/PhysX-Omni/PhysXVerse](https://huggingface.co/datasets/PhysX-Omni/PhysXVerse)

**Project:** [https://physx-omni.github.io/](https://physx-omni.github.io/)

## Capabilities

- Rigid, deformable, and articulated 3D asset generation
- Geometry + material + kinematics + affordance + scale properties
- PhysXVerse dataset + PhysX-Bench 6-axis evaluation

## VFX / Filmmaking Use Cases

- Generate physically accurate props for simulations in Blender/DaVinci
- Create articulated assets with correct joint structure for VFX animation
- Populate generated scenes with physically simulatable objects

## How to Run

```bash
git clone --recurse-submodules https://github.com/physx-omni/PhysX-Omni.git
. ./setup.sh --new-env --basic --xformers --flash-attn
pip install transformers==4.50.0 qwen-vl-utils 'accelerate>=0.26.0'
```