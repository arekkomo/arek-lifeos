# Sharing models and custom nodes in ComfyUI — Magnopus

Tags: AI Image
Description: Here at Magnopus, as we’ve begun to use ComfyUI, we needed a way to share models and custom nodes among project team members. We wanted to save storage space and speed up ComfyUI onboarding by configuring resources once in a shared location, and here’s how we did it.
URL: https://www.magnopus.com/blog/sharing-models-and-custom-nodes-in-comfyui
Date Added: January 11, 2025 12:27 PM
Type: Article
Archive: No
Spark: No

![](Sharing%20models%20and%20custom%20nodes%20in%20ComfyUI%20%E2%80%94%20Magno/stn-CwNGlTdyS9PUZl39WdT1QeRTopIoYtBTdGheEMwG.jpeg)

![](https://images.squarespace-cdn.com/content/v1/618131cf8cd8e779321e9666/5dc4e8d5-5c8d-452c-8b5a-4d40de25d03a/image2.png)

Image generated using ComfyUI

The ability to create content in response to image or text-based prompts using Generative AI is a burgeoning interest in the sphere of Artificial Intelligence. Stable Diffusion models are a family of Generative AI models which was spearheaded by *Stability AI* in 2022 and are gaining in popularity. Stable Diffusion models are open-source and allow you to train new models on your own datasets. While all diffusion models enable generating images from prompts, the technology used for Stable Diffusion requires less processing power and is more readily utilized on consumer-grade graphics cards. [ComfyUI](https://github.com/comfyanonymous/ComfyUI) is a popular node-based Stable Diffusion  graphical user interface (GUI)  that generates images in response to positive and negative prompts.

The Stable Diffusion process requires a model checkpoint as a basis for generating images. [CivitAI](https://civitai.com/) and [Hugging Face](https://huggingface.co/models?other=stable-diffusion) are popular sites for downloading models.

While ComfyUI’s default nodes provide basic capabilities for generating images, it’s likely that you will need to install additional nodes for more advanced processing. Additional nodes are available from a variety of sources. [ComfyUI Nodes Info](https://ltdrdata.github.io/) has links to more than 700 Github repositories.

### **Our need**

By default, ComfyUI accesses models and nodes via ‘models’ and ‘custom_nodes’ folders that are part of its individual installation folder hierarchy. Here at Magnopus, we wanted to benefit from an installation that would be shared among project team members.

A shared installation addresses some downsides of working with ComfyUI. The files for the models and nodes take a lot of storage space. With individual installs, new users need to put the necessary models and nodes in place, which is time-consuming. Also, versions used across the team can easily get out of sync.

### **Our solution**

We filled this need with ComfyUI’s ‘--extra-model-paths-config’ command-line argument and pointed it to a shared network drive.  At first glance, one might think that this argument is used to specify paths for models only. In fact, its value is a yaml file that points to additional locations for models as well as custom nodes.

Using a centralized drive created several efficiencies in our use of ComfyUI. We saved disk space by avoiding multiple installs of large files. Onboarding was faster because the models and custom nodes were immediately available for new users. By using one copy of the files, versioning was easily managed. Updates were instantly available to everyone. Cloud-based resources became an option, providing flexibility, scalability, and accessibility for team members working remotely or in distributed environments.

### **Sample configuration**

In this example, ‘extra_model_paths.yaml’ is in ‘X:\comfyui_models` which has subfolders ‘models’ and ‘custom_nodes’. The X drive in this example is mapped to a networked folder which allows for easy sharing of the models and nodes. The contents of the yaml file are shown below.

It was brought to our attention after publishing this article that while ComfyUI itself remains secure, a malicious custom node called "ComfyUI_LLMVISION" was uploaded by a user and contained code designed to steal sensitive user information, including browser passwords, credit card details, and browsing history. **Though this particular custom node is unrelated to this article, we wanted to remind you to remain vigilant when integrating third-party components into your workflows.** Read more about this particular incident [here](https://www.vpnmentor.com/news/comfyui-malicious-custom-node/).