# Generating Worlds

Tags: AI Image
Description: Today we're sharing our first step towards spatial intelligence: an AI system that generates 3D worlds from a single image.
URL: https://www.worldlabs.ai/blog
Date Added: January 9, 2025 11:56 PM
Type: Tool
Archive: No
Spark: No

![](Generating%20Worlds/stn-Ws2Khb8aNzacLaHXXzHjLeVEslihkmwgnEBtunZ5.jpeg)

Dec 2, 2024

Today we're sharing our first step towards spatial intelligence: an AI system that generates 3D worlds from a single image. This lets you step into any image and explore it in 3D.

Beyond the input image, all is generated:

Input Image

3D World

Most GenAI tools make 2D content like images or videos. Generating in 3D instead improves control and consistency. This will change how we make movies, games, simulators, and other digital manifestations of our physical world.

In this post you'll explore our generated worlds, rendered live in your browser. You'll also experience different camera effects, 3D effects, and dive into classic paintings. Finally, you'll see how creators are already building with our models.

## Explore a World

It's your turn to explore some worlds!

Below we show 3D worlds generated from fantastical images[[1]](https://www.worldlabs.ai/blog#footnote1) and everyday photos.[[2]](https://www.worldlabs.ai/blog#footnote2)

Use arrow keys or WASD to move, and click and drag with your mouse to look around:

![](https://wlt-ai-cdn.art/wed-v1//well_village/pane_preview.jpg)

Explore the generated world

Use WASD keys to move

![](https://www.worldlabs.ai/img/wasd.png)

Click and drag to look around

![](https://www.worldlabs.ai/img/mouse.png)

Out of bounds

![](https://wlt-ai-cdn.art/wed-v1//well_village/preview.jpg)

![](https://wlt-ai-cdn.art/wed-v1//space_mountains/preview.jpg)

![](https://wlt-ai-cdn.art/wed-v1//marble_palace/preview.jpg)

![](https://wlt-ai-cdn.art/wed-v1//blobby_sakura/preview.jpg)

![](https://wlt-ai-cdn.art/wed-v1//garden_arches/preview_polaroid.jpg)

![](https://wlt-ai-cdn.art/wed-v1//ny_art2/preview_polaroid.jpg)

![](https://wlt-ai-cdn.art/wed-v1//yosemite3/preview_polaroid.jpg)

![](https://wlt-ai-cdn.art/wed-v1//teotihuacan/preview_polaroid.jpg)

Not seeing interactive 3D? [Click here](https://www.worldlabs.ai/blog?fallback=true).

## Camera Effects

Once a scene is generated, it is rendered live in the browser using a virtual camera. Precise control over this camera enables artistic photographic effects.

We can simulate a shallow [depth of field](https://en.wikipedia.org/wiki/Depth_of_field), where only objects at a certain distance from the camera are in focus:

Near

Far

![](https://wlt-ai-cdn.art/wed-v1//cartoon_halloween/pane_preview.jpg)

Move the slider to adjust the focus distance

Use WASD keys to move

![](https://www.worldlabs.ai/img/wasd.png)

Click and drag to look around

![](https://www.worldlabs.ai/img/mouse.png)

Out of bounds

![](https://wlt-ai-cdn.art/wed-v1//cartoon_halloween/preview.jpg)

![](https://wlt-ai-cdn.art/wed-v1//castle_grounds/preview.jpg)

![](https://wlt-ai-cdn.art/wed-v1//ball_alley/preview.jpg)

![](https://wlt-ai-cdn.art/wed-v1//cartoon_room/preview.jpg)

We can also simulate a [dolly zoom](https://en.wikipedia.org/wiki/Dolly_zoom) which adjusts a camera's position and [field of view](https://en.wikipedia.org/wiki/Angle_of_view_(photography)) at the same time:

Wide

Narrow

![](https://wlt-ai-cdn.art/wed-v1//golden_library/pane_preview.jpg)

Move the slider to dolly zoom

You can't move in this scene

Out of bounds

![](https://wlt-ai-cdn.art/wed-v1//golden_library/preview.jpg)

![](https://wlt-ai-cdn.art/wed-v1//mountain_gate/preview.jpg)

![](https://wlt-ai-cdn.art/wed-v1//red_chair/preview.jpg)

![](https://wlt-ai-cdn.art/wed-v1//city_portrait/preview.jpg)

## 3D Effects

Most generative models predict pixels. Predicting a 3D scene instead has many benefits:

- **Persistent Reality:** Once a world is generated, it's there to stay. The scene won't change behind your back if you look away and come back.
- **Real-Time Control:** After generating a scene, you can move around it in real-time. You can linger on the details of a flower, or peek around a corner to see what is revealed.
- **Correct Geometry:** Our generated worlds obey basic physical rules of 3D geometry. They have a sense of solidity and depth that contrasts with the dream-like nature of some AI-generated video.

The simplest way to visualize the 3D scene is a *depth map* where each pixel is colored by its distance to the camera:

ColorDepth

NearFar

![](https://www.worldlabs.ai/img/depthmap.jpg)

![](https://wlt-ai-cdn.art/wed-v1//mossy_path/pane_preview.jpg)

Change effects with the buttons above

Use WASD keys to move

![](https://www.worldlabs.ai/img/wasd.png)

Click and drag to look around

![](https://www.worldlabs.ai/img/mouse.png)

Out of bounds

![](https://wlt-ai-cdn.art/wed-v1//mossy_path/preview.jpg)

![](https://wlt-ai-cdn.art/wed-v1//sandy_market/preview.jpg)

![](https://wlt-ai-cdn.art/wed-v1//bw_graveyard/preview.jpg)

![](https://wlt-ai-cdn.art/wed-v1//mushroom_bridge/preview.jpg)

We can use the 3D scene structure to build *interactive* effects — click on the scene to interact with it!

SonarSpotlightRippleNone

![](https://wlt-ai-cdn.art/wed-v1//pink_pillar/pane_preview.jpg)

Click to interact!

Use WASD keys to move

![](https://www.worldlabs.ai/img/wasd.png)

Click and drag to look around

![](https://www.worldlabs.ai/img/mouse.png)

Out of bounds

![](https://wlt-ai-cdn.art/wed-v1//pink_pillar/preview.jpg)

![](https://wlt-ai-cdn.art/wed-v1//grassy_library/preview.jpg)

![](https://wlt-ai-cdn.art/wed-v1//brick_alley/preview.jpg)

![](https://wlt-ai-cdn.art/wed-v1//castle_arcade/preview.jpg)

We can also build effects that passively animate the scene:

RustleWavesColor WaveNone

![](https://wlt-ai-cdn.art/wed-v1//sakura_path/pane_preview.jpg)

Change effects with the buttons above

Use WASD keys to move

![](https://www.worldlabs.ai/img/wasd.png)

Click and drag to look around

![](https://www.worldlabs.ai/img/mouse.png)

Out of bounds

![](https://wlt-ai-cdn.art/wed-v1//sakura_path/preview.jpg)

![](https://wlt-ai-cdn.art/wed-v1//christmas_bridge/preview.jpg)

![](https://wlt-ai-cdn.art/wed-v1//forest_mushroom/preview.jpg)

![](https://wlt-ai-cdn.art/wed-v1//jungle_vortex/preview.jpg)

## Step into Paintings

World generation allows you to experience iconic pieces of art in a new way. We generated worlds from our favorite pieces[[3]](https://www.worldlabs.ai/blog#footnote3) by van Gogh, Hopper, Seurat, and Kandinsky.

Anything not in the original painting was generated by our model.

![](https://wlt-ai-cdn.art/wed-v1//vangogh_cafe/pane_preview.jpg)

Explore the generated world

Use WASD keys to move

![](https://www.worldlabs.ai/img/wasd.png)

Click and drag to look around

![](https://www.worldlabs.ai/img/mouse.png)

Out of bounds

![](https://wlt-ai-cdn.art/wed-v1//vangogh_cafe/preview_museum.jpg)

![](https://wlt-ai-cdn.art/wed-v1//hopper_nighthawk/preview_museum.jpg)

![](https://wlt-ai-cdn.art/wed-v1//seurat_avray/preview_museum.jpg)

![](https://wlt-ai-cdn.art/wed-v1//kandinsky_murnau1/preview_museum.jpg)

## Creative Workflows

3D world generation naturally composes with other AI tools. This allows creators to work with tools they already know to enable new experiences.

For example, we can create worlds from text by first generating an image using a text-to-image model. Different models have their own style which our worlds can inherit.

Here we generate four variants of the same scene using different text-to-image models,[[4]](https://www.worldlabs.ai/blog#footnote4) all using the same prompt:

A vibrant cartoon-style teenager's bedroom with a bed covered in colorful blankets, a cluttered desk with a computer, posters on the walls, and scattered sports gear. A guitar leans against the wall, and a cozy, patterned rug is in the center. Light from a window adds a warm, youthful vibe to the room.

![](https://wlt-ai-cdn.art/wed-v1//cartoon_bedroom_flux/pane_preview.jpg)

Explore the generated world

Use WASD keys to move

![](https://www.worldlabs.ai/img/wasd.png)

Click and drag to look around

![](https://www.worldlabs.ai/img/mouse.png)

Out of bounds

![](https://wlt-ai-cdn.art/wed-v1//cartoon_bedroom_flux/preview.jpg)

![](https://wlt-ai-cdn.art/wed-v1//cartoon_bedroom_mj/preview.jpg)

![](https://wlt-ai-cdn.art/wed-v1//cartoon_bedroom_ig/preview.jpg)

![](https://wlt-ai-cdn.art/wed-v1//cartoon_bedroom_dalle/preview.jpg)

We've given a few creators an early sneak peek at our technology to begin experimenting with the possibilities enabled by a 3D-native generative AI workflow.

[Eric Solorio](https://x.com/8bit_e) shows how our models fill a gap in his creative workflow, making it easy to stage characters within scenes and direct precise camera movements:

Your browser does not support video playback.

[Brittani Natali](https://x.com/brittaninatali) lays out carefully crafted camera paths through our generated worlds to evoke different moods across three short films, using a workflow combining World Labs' technology with tools like Midjourney, Runway, Suno, ElevenLabs, Blender, and CapCut:

Your browser does not support video playback.

## Looking Ahead

These results are our first early preview of generating 3D worlds. We are hard at work improving the size and fidelity of our generated worlds, and experimenting with new ways for users to interact with them.

Keep up with our future releases via our [waitlist](https://forms.gle/tkfW7yMqMsCXWw4F7), or get in touch at [hello@worldlabs.ai](mailto:hello@worldlabs.ai).

If you're excited to help us realize this vision, [join us](https://jobs.ashbyhq.com/worldlabs)!

*This post was produced by the World Labs technical staff.*

[1] Unless otherwise specified, all images on this page were generated using FLUX 1.1 [pro], Ideogram, or Midjourney. [[↩]](https://www.worldlabs.ai/blog#ref1)

[2] Photo credits: Keunhong Park, Ben Mildenhall. [[↩]](https://www.worldlabs.ai/blog#ref2)

[3] From left to right:
[*Café Terrace at Night*](https://en.wikipedia.org/wiki/Caf%C3%A9_Terrace_at_Night), [Vincent van Gogh](https://en.wikipedia.org/wiki/Vincent_van_Gogh), 1888;
[*Nighthawks*](https://en.wikipedia.org/wiki/Nighthawks_(Hopper)), [Edward Hopper](https://en.wikipedia.org/wiki/Edward_Hopper), 1942;
[*Ville D' Avray, White Houses*](https://www.liverpoolmuseums.org.uk/artifact/ville-d-avray-white-houses), [Georges Pierre Seurat](https://en.wikipedia.org/wiki/Georges_Seurat), 1882;
[*Murnau - Landscape with Green House*](https://www.sothebys.com/en/auctions/ecatalogue/2017/impressionist-modern-art-evening-sale-l17006/lot.47.html), [Wassily Kandinsky](https://en.wikipedia.org/wiki/Wassily_Kandinsky), 1908
[[↩]](https://www.worldlabs.ai/blog#ref3)

[4] From left to right: FLUX, Midjourney, Ideogram, DALL-E [[↩]](https://www.worldlabs.ai/blog#ref4)