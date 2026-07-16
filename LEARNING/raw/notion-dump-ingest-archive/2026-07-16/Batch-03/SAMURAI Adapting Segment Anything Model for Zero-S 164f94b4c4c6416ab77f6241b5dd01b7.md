# SAMURAI: Adapting Segment Anything Model for Zero-Shot Visual Tracking with Motion-Aware Memory

Tags: AI Video
URL: https://yangchris11.github.io/samurai/
Date Added: January 11, 2025 1:07 PM
Type: Article
Archive: No
Spark: No

![](SAMURAI%20Adapting%20Segment%20Anything%20Model%20for%20Zero-S/stn-1ahVEzjKhvYhrnLvkXfR33zWXaQ5RH50KVpT12u0.jpeg)

[Hsiang-Wei Huang](https://hsiangwei0903.github.io/)1, [Wenhao Chai](https://rese1f.github.io/)1, [Zhongyu Jiang](https://zhyjiang.github.io/)1, [Jenq-Neng Hwang](https://people.ece.uw.edu/hwang/)1

1University of Washington

[arXiv](https://arxiv.org/abs/2411.11922)

[Code](https://github.com/yangchris11/samurai)

[Raw Results](https://drive.google.com/drive/folders/1ssiDmsC7mw5AiItYQG4poiR1JgRq305y?usp=sharing)

1917 (2019), directed by Sam Mendes.

Gameplay from Sekiro: Shadows Die Twice (2019) and Black Myth: Wukong (2024).

Sport scenes from NFL (2024), FIFA (2022), NBA (2024), and Olympics (2024).

Choreographies of Loco by ITZY (2021) and Easy by Le Sserafim (2023).

Disclaimer: The videos included in this demonstration are the property of their respective owners. They are used only for academic and research purposes.

## Abstract

The Segment Anything Model 2 (SAM 2) has demonstrated strong performance in object segmentation tasks but faces challenges in visual object tracking, particularly when managing crowded scenes with fast-moving or self-occluding objects. Furthermore, the fixed-window memory approach in the original model does not consider the quality of memories selected to condition the image features for the next frame, leading to error propagation in videos. This paper introduces SAMURAI, an enhanced adaptation of SAM 2 specifically designed for visual object tracking. By incorporating temporal motion cues with the proposed motion-aware memory selection mechanism, SAMURAI effectively predicts object motion and refines mask selection, achieving robust, accurate tracking without the need for retraining or fine-tuning. SAMURAI operates in real-time and demonstrates strong zero-shot performance across diverse benchmark datasets, showcasing its ability to generalize without fine-tuning. In evaluations, SAMURAI achieves significant improvements in success rate and precision over existing trackers, with a 7.1% AUC gain on LaSOT-ext and a 3.5% AO gain on GOT-10k. Moreover, it achieves competitive results compared to fully supervised methods on LaSOT, underscoring its robustness in complex tracking scenarios and its potential for real-world applications in dynamic environments.

![](https://yangchris11.github.io/samurai/website/img/teaser.png)

**Figure 1:** The overview of our SAMURAI visual object tracker.

## Results

![](https://yangchris11.github.io/samurai/website/img/main_result_table.png)

**Table 1:** Zero-shot tracking results on LaSOT, LaSOT-ext, and GOT-10k.

![](https://yangchris11.github.io/samurai/website/img/additional_result_table.png)

**Table 2:** Zero-shot tracking results on additional benchmarks: TrackingNet, NFS, and OTB-100.

![](https://yangchris11.github.io/samurai/website/img/baseline_result_table.png)

**Table 3:** Comparison between proposed SAMURAI and the baseline SAM 2 on LaSOT and LaSOT-ext.

## BibTeX

```
        @misc{yang2024samurai,
              title={SAMURAI: Adapting Segment Anything Model for Zero-Shot Visual Tracking with Motion-Aware Memory}, 
              author={Cheng-Yen Yang and Hsiang-Wei Huang and Wenhao Chai and Zhongyu Jiang and Jenq-Neng Hwang},
              year={2024},
              eprint={2411.11922},
              archivePrefix={arXiv},
              primaryClass={cs.CV},
              url={https://arxiv.org/abs/2411.11922}, 
        }
```