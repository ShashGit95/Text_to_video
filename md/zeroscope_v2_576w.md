# Project Cinematic Models

## Text-to-video-synthesis Model : zeroscope_v2_576w

* A watermark-free Modelscope-based video model optimized for producing high-quality 16:9 compositions and a smooth video output. 

* This model was trained from the original weights using 9,923 clips and 29,769 tagged frames at 24 frames, 576x320 resolution.

* zeroscope_v2_576w uses 7.9gb of vram when rendering 30 frames at 576x320

* zeroscope_v2_567w is specifically designed for upscaling with zeroscope_v2_XL using vid2vid in the 1111 text2video extension by kabachuha. 

* Leveraging this model as a preliminary step allows for superior overall compositions at higher resolutions in zeroscope_v2_XL, permitting faster exploration in 576x320 before transitioning to a high-resolution render. 

* See some example outputs that have been upscaled to 1024x576 using zeroscope_v2_XL. 