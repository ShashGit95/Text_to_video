# Project Cinematic 12_08_2023 Demo

## client 1.0 | model 1.0
 

## Demo Scope

* Create video from a text prompt in the Google colab.

## Demo Loom

https://www.loom.com/share/e299cd23255848548f557d6680d77512?sid=1b7d3c45-26b6-41b5-ad87-56f0783345d3


### Text-to-video-synthesis in Google colab.

* You can check the 'Cinematic_shortVideo.ipynb' notebook in the 'notebooks' folder to generate short videos.

* Generate short video clip in the Google colab using diffusion model. 

* "text-to-video-ms-1.7b" model from Hugginh face is used to generate video. 


#### Text-to-video-synthesis Model in Open Domain

* This model is based on a multi-stage text-to-video generation diffusion model, which inputs a description text and returns a video that matches the text description. Only English input is supported.


#### Model description

* The text-to-video generation diffusion model consists of three sub-networks: text feature extraction model, text feature-to-video latent space diffusion model, and video latent space to video visual space model.

*  The overall model parameters are about 1.7 billion. Currently, it only supports English input. 

* The diffusion model adopts a UNet3D structure, and implements video generation through the iterative denoising process from the pure Gaussian noise video.

* This model has a wide range of applications and can reason and generate videos based on arbitrary English text descriptions.

# Generated video


https://github.com/williamboomer87/project-cinematic/assets/113249314/d1c63919-b4a2-4876-8492-33d57a8d998c

