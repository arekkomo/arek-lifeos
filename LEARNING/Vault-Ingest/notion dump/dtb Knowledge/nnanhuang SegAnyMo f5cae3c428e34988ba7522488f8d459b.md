# nnanhuang/SegAnyMo

Tags: AI Roto
Description: Tool that segments any moving object in videos by processing 2D tracks and depth maps to generate precise masks
URL: https://github.com/nnanhuang/SegAnyMo
Date Added: June 5, 2025 9:29 AM
Type: Github
Archive: No
Spark: No

SegAnyMo (Segment Any Motion in Videos) is a tool that processes 2D tracks and depth maps from videos to segment moving objects. It works by:

- **Capturing motion patterns:** It uses a motion encoder to process input 2D tracks and depth maps, generating featured tracks.
- **Decoding dynamic trajectories:** A tracks decoder then integrates DINO features with the featured tracks, separating motion and semantic information to obtain dynamic trajectories.
- **Generating moving object masks:** Finally, it uses SAM2 to group dynamic tracks that belong to the same object, producing fine-grained moving object masks.

---

![](nnanhuang%20SegAnyMo/stn-C4ac1tHgokrQlceehxhKCUJmRHfnPl7L8u18mIME.jpeg)