# Project Cinematic Models

## Text-to-video-synthesis Model : text-to-video-ms-1.7b

* This model is based on a multi-stage text-to-video generation diffusion model, which inputs a description text and returns a video that matches the text description. Only English input is supported.


## Model description

* The text-to-video generation diffusion model consists of three sub-networks: text feature extraction model, text feature-to-video latent space diffusion model, and video latent space to video visual space model. 

* The overall model parameters are about 1.7 billion. 

* Currently, it only supports English input. The diffusion model adopts a UNet3D structure, and implements video generation through the iterative denoising process from the pure Gaussian noise video.

* This model is meant for research purposes. 

## Use cases

* This model has a wide range of applications and can reason and generate videos based on arbitrary English text descriptions.

* The output mp4 file can be viewed by VLC media player. Some other media players may not view it normally.

## Model limitations and biases

* The model is trained based on public data sets such as Webvid, and the generated results may have deviations related to the distribution of training data.

* This model cannot achieve perfect film and television quality generation.

* The model cannot generate clear text.

* The model is mainly trained with English corpus and does not support other languages ​​at the moment.

* The performance of this model needs to be improved on complex compositional generation tasks.

## Misuse, Malicious Use and Excessive Use

* The model was not trained to realistically represent people or events, so using it to generate such content is beyond the model's capabilities.

* It is prohibited to generate content that is demeaning or harmful to people or their environment, culture, religion, etc.

* Prohibited for pornographic, violent and bloody content generation.

* Prohibited for error and false information generation.

## Training data

* The training data includes LAION5B, ImageNet, Webvid and other public datasets. 

* Webvid dataset has images with water mark from shutterstock.

* Image and video filtering is performed after pre-training such as aesthetic score, watermark score, and deduplication.

