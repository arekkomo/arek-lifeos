# Depth Anything V2

Tags: AI Image
Description: New, most accurate Monocular Depth Estimation network
URL: https://laws-sniff-aau.craft.me/XdyJGV1JVP3CYQ
Date Added: January 10, 2025 12:13 AM
Type: Article
Archive: No
Spark: No

![](Depth%20Anything%20V2/stn-juh3bsBj84EaHC5TpzpRUYz0AQfirbwfzEHkbeTF.jpeg)

By HKU, TikTok

![](https://cdn-thumbnails.huggingface.co/social-thumbnails/spaces/depth-anything/Depth-Anything-V2.png)

[Depth Anything V2 - a Hugging Face Space by depth-anything](https://huggingface.co/spaces/depth-anything/Depth-Anything-V2)

[Discover amazing ML apps made by the community](https://huggingface.co/spaces/depth-anything/Depth-Anything-V2)

•

New, most accurate Monocular Depth Estimation network

•

More consistent and precise than latest sota Marigold, and faster

•

It’s more accurate, and works across a larger variety of real-world scenes

•

It can also handle transparent objects, reflective surfaces, and abstract images

![](https://secure-res.craft.do/v2/5RgvxdZNBaiNGx4Rqgch2Xm2vi3WtamQMpzJmNNj21bxB9LUjuBfv3ogW4K8k9XKuzyBfwfNp9paUPtrGwNZPmMu7HVRG7epS4pcWCZSHj8WeZD5VKFcPFqQEXNTJDqApwRcshWWhv1wscVqCrBYi9fhM81DRzwV5RUwnA6eTm7HSyQfQCFhDKK2CMoAgBBfwZn4EXPGYoU4E28EEZ7tuMSdPuiJDq7SSyTbV9p99TaDG1YvHCGZjvVjycsgsWumRBMsXy5wzeab8jgCqt2Tuso82Fxb7MdwCp79t4ypukjgqFRX3Q6kqrd45hJQcG77pZqtcEpS/IMG_DAE88270047B-1.jpg)

•

How? By asking the question: do we really need a new architecture to improve SOTA, or just get better data?

•

It turns out, when you analyze why Monocular Depth Estimation SOTAs still fail in some areas, it’s because of the dataset they’ve been trained on!

•

Existing real-world depth maps datasets are: noisy, old, and low-resolution; they don’t support transparent and reflective surfaces; and they often don’t have good examples for fine details such as bike spokes, tree branches

•

They contain the real-world variation we’re look for, though…

•

Synthetic datasets can (and should) be used. Their depth is precise, and they support depth for transparent and reflective surfaces. But they don't generalize to real-world scenes.

•

I.e. if you train a network purely on synthetic data, it’ll perform badly at estimating depth from images in the real world

•

Their scene variation is necessarily much smaller than the one found in the real world.

•

Less variation = the model won’t work when used in the real world

•

They contain the ultra-precise, pixel-perfect depth we’re looking for, though…

•

Therefore: realize that we need both synthetic and real-world data

•

So how do we get the best of both worlds?

•

Train a teacher model, DINO V2G, only on synthetic data (~300k)

•

It learns to be very precise this way, thanks to the precision of the synthetic depth

•

Then, use this teacher model to parse a large in-the-wild dataset, to produce pseudo-real image-depth pairs (~60M)

•

This dataset is the crucial part of the paper: it’s almost as precise as synthetic depth, but with the variety of scenes that comes from real-world data!

•

It also contains samples from the real world with valid depth on transparent and on reflective surfaces

•

Finally, train a series of student models on the pseudo-real dataset

•

Again, use DINO models, of various size: small, medium, large, and giga

![](https://secure-res.craft.do/v2/5RgvxdZNBaiNGx4Rqgch2Xm2vi3WtamQMpzJmNNj21bxB9LUjuBfv3ogW4K8k9XKuzyBfwfNp9paUPtrGwNZPmMu7HVRG7epS4pcWCZSHj8WeZD5VKFcPFqQEXNTJDqApwRcshWWhv1wscVqCrBYi9fhLyetfGpAU5Uf85u3PCttDvjsDZDdsRVq2WUnm7cspxBQkRyWbx99ujMyZL2MbgWvXtY3hwGwG3BnVifYQ3Yc5D2aDhRdMpqPGBZr4kYrtS2qVtcrPxz6MC6sGYuZ1iciNALS4rCtcsCQGYgsEQCG46sM16bSmf3E2APzXCaTW32LTuU8/IMG_7EF8CDA89B0F-1.jpg)

•

Through the pseudo-real dataset, the student models become much more accurate compared to V1, even though there haven’t been any architectural changes!

![](https://secure-res.craft.do/v2/5RgvxdZNBaiNGx4Rqgch2Xm2vi3WtamQMpzJmNNj21bxB9LUjuBfv3ogW4K8k9XKuzyBfwfNp9paUPtrGwNZPmMu7HVRG7epS4pcWCZSHj8WeZD5VKFcPFqQEXNTJDqApwRcshWWhv1wscVqCrBYi9fhMAth5Hx82ykdVU7hJLs6vwAZhJPNQf2tQ6dX9TMfeF6z7z5G3dt5DSkhySy3yxAoD1gh4jJnvt75YXNZLsHzvcfT3Uy6CZq7u123ormyCHEGcxGnMfEu49DBmvGT6jbUdGXuaYvnsM8YpantbMe9BAa2c8BD1rjx142po2mskcYXiLYc/IMG_48EEE7CAE4B0-1.jpg)