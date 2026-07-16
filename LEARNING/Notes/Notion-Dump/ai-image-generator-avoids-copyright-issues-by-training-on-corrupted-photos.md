---
title: AI Image Generator Avoids Copyright Issues by Training on Corrupted Photos
category: note
summary: Preserved substantive Notion export for AI Image Generator Avoids Copyright Issues by Training on Corrupted Photos.
tags: [notion-import, source-preservation]
sources: 1
updated: 2026-07-16
source_path: raw/notion-dump-ingest-archive/2026-07-16/Batch-01/AI Image Generator Avoids Copyright Issues by Trai 49897c7a30e547219c99af6262a1242f.md
ingested: 2026-07-16
---

# AI Image Generator Avoids Copyright Issues by Training on Corrupted Photos

**Ingest batch:** [[Notion-Dump-Ingest-Batch-01]]  
**Original export:** `raw/notion-dump-ingest-archive/2026-07-16/Batch-01/AI Image Generator Avoids Copyright Issues by Trai 49897c7a30e547219c99af6262a1242f.md`

---

# AI Image Generator Avoids Copyright Issues by Training on Corrupted Photos

Tags: AI Image
Description: Are you cool with this?
URL: https://petapixel.com/2024/05/22/ai-image-generator-avoids-copyright-issues-by-training-on-corrupted-photos/
Date Added: January 11, 2025 10:44 AM
Type: Article
Archive: No
Spark: No

![](AI%20Image%20Generator%20Avoids%20Copyright%20Issues%20by%20Trai/stn-BpHVghZJfKpQppz3HXGQACNaARtwL6psFBPRML6T.jpeg)

May 22, 2024

[Matt Growcoot](https://petapixel.com/author/mattgrowcoot/)

![](https://petapixel.com/assets/uploads/2024/05/Ambient-Diffusion-800x420.jpg)

Even with 93% of the pixels missing in the training data (left), the researcher’s AI image generator still made pictures of people (right).

AI image generators are controversial because they were largely built on copyrighted works of artists and photographers who [did not consent](https://petapixel.com/2024/01/03/court-docs-reveal-midjourney-wanted-to-copy-the-style-of-these-photographers). But how would they feel if corrupted versions of their work were used instead?

[https://app.notion.com](https://app.notion.com)

A research team led by the University of Texas has come up with a model called Ambient Diffusion which they claim “gets around” the issue of copyright and AI image generators by feeding the model images that have pixels missing — in some cases as much as 93%.

“Early efforts suggest the framework is able to continue to generate high-quality samples without ever seeing anything that’s recognizable as the original source images,” [reads a press release.](https://news.utexas.edu/2024/05/20/artificial-intelligence-trained-to-draw-inspiration-from-images-not-copy-them/)

1/1 Continue watchingafter the adVisit Advertiser website[GO TO PAGE](https://petapixel.com/2024/05/22/ai-image-generator-avoids-copyright-issues-by-training-on-corrupted-photos/#)

The project started by training a text-to-image model with images that had pixels partially masked but for Ambient Diffusion the team began experimenting with corrupting images with other types of noise.

![](https://petapixel.com/assets/uploads/2024/05/Screenshot-2024-05-22-at-16.53.11-copy-475x800.jpg)

Left column: The training dataset with different levels of corruption. Right column: Generations from the models trained with the corresponding parameters. As shown, the generations become
slightly worse as we increase the level of corruption, but we can reasonably well learn the distribution even with 91% pixels missing (on average) from each training image.

The first diffusion model was trained with a clean set of 3,000 images of celebrities which spat out “blatant copies” of the training data.

[https://app.notion.com](https://app.notion.com)

[https://app.notion.com](https://app.notion.com)

However, when the researchers began corrupting the training data, randomly masking up to 90 percent of the pixels, the image generator still created “high quality” images of humans but the resulting pictures didn’t look like any of the real-life celebrities.

“Our framework allows for controlling the trade-off between memorization and performance,” says Giannis Daras, a computer science graduate student who led the work. “As the level of corruption encountered during training increases, the memorization of the training set decreases.”

The researchers say that the model didn’t just spit out pictures of noise as some may have expected, although the performance still changed with the quality of the output worsening the more the photos were masked.

“The framework could prove useful for scientific and medical applications, too,” adds Adam Klivans, a professor of computer science, who was involved in the work. “That would be true for basically any research where it is expensive or impossible to have a full set of uncorrupted data, from black hole imaging to certain types of MRI scans.”

Members of the University of California, Berkeley, and MIT were also part of the research team. The paper can be read [here](https://arxiv.org/abs/2305.19256).

***Image credits:** Giannis Daras, Kulin Shah, Yuval Dagan, Aravind Gollakota, Alexandros G. Dimakis, Adam Klivans.*

[News](https://petapixel.com/topic/news/)

[aiimagegenerator](https://petapixel.com/tag/aiimagegenerator/), [Artificial Intelligence](https://petapixel.com/tag/artificial-intelligence/), [copyright](https://petapixel.com/tag/copyright/), [imagendiffusionmodel](https://petapixel.com/tag/imagendiffusionmodel/), [texttoimage](https://petapixel.com/tag/texttoimage/)

PetaPixel articles may include affiliate links; if you buy something through such a link, PetaPixel may earn a commission.

Related Articles

 [Japan Declares AI Training Data Fair Game and ‘Will Not Enforce Copyright’](https://petapixel.com/2023/06/05/japan-declares-ai-training-data-fair-game-and-will-not-enforce-copyright/)

![](https://petapixel.com/assets/uploads/2023/06/Japan-550x288.jpg)

 [Midjourney and Stable Diffusion Ask US Court to Dismiss Artists’ Lawsuit](https://petapixel.com/2023/04/20/midjourney-and-stable-diffusion-ask-us-court-to-dismiss-artists-lawsuit/)

![](https://petapixel.com/assets/uploads/2022/05/Depositphotos_326976748_L-550x288.jpg)

 [Getty Images is Suing AI Image Generator Stable Diffusion](https://petapixel.com/2023/01/17/getty-images-is-suing-ai-image-generator-stable-diffusion/)

![](https://petapixel.com/assets/uploads/2023/01/crowdswithgettylogo-550x288.jpg)

 [An AI Video of the French President Kissing a Man Was Manipulated From Real Photos](https://petapixel.com/2024/08/20/an-ai-video-of-the-french-president-kissing-a-man-was-manipulated-from-real-photos/)

![](https://petapixel.com/assets/uploads/2024/08/Macron-AI-Fake-550x288.jpg)

Discussion

[https://disqus.com/embed/comments/?base=default&f=petapixel&t_i=743663&t_u=http%3A%2F%2Fpetapixel.com%2F2024%2F05%2F22%2Fai-image-generator-avoids-copyright-issues-by-training-on-corrupted-photos%2F&t_e=AI%20Image%20Generator%20Avoids%20Copyright%20Issues%20by%20Training%20on%20Corrupted%20Photos&t_d=AI%20Image%20Generator%20Avoids%20Copyright%20Issues%20by%20Training%20on%20Corrupted%20Photos&t_t=AI%20Image%20Generator%20Avoids%20Copyright%20Issues%20by%20Training%20on%20Corrupted%20Photos&s_o=default#version=b4b86fd8096fd3a413f323515923c7f3](https://disqus.com/embed/comments/?base=default&f=petapixel&t_i=743663&t_u=http%3A%2F%2Fpetapixel.com%2F2024%2F05%2F22%2Fai-image-generator-avoids-copyright-issues-by-training-on-corrupted-photos%2F&t_e=AI%20Image%20Generator%20Avoids%20Copyright%20Issues%20by%20Training%20on%20Corrupted%20Photos&t_d=AI%20Image%20Generator%20Avoids%20Copyright%20Issues%20by%20Training%20on%20Corrupted%20Photos&t_t=AI%20Image%20Generator%20Avoids%20Copyright%20Issues%20by%20Training%20on%20Corrupted%20Photos&s_o=default#version=b4b86fd8096fd3a413f323515923c7f3)

[https://app.notion.com](https://app.notion.com)
