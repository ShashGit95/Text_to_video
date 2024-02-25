# Project Cinematic 12_22_2023 Demo

## client 1.0 | model 1.0
 

## Demo Scope

* Create a 25-second-long video using text prompt in Google Colab.

## Demo Loom

https://www.loom.com/share/15feca5bb4e245a0a16f00bdfb52d5b2?sid=a244c963-c734-4b41-83a2-ce305ecf781a


### Text-to-video-synthesis in Google colab.

* Generate 25 seconds long video clip in the Google colab using diffusion model. 

* "text-to-video-ms-1.7b" model from Hugginh face is used to generate video. 

* The notebook "Cinematic_longVideo.ipynb" is designed to generate a 25-second-long video. You can find it in the "notebooks" folder.

* It takes a relatively longer time and utilizes 16 GB VRAM (GPU). 

* To optimize GPU performance, the following code snippet is used:

`pipe.enable_model_cpu_offload()` : This method call likely indicates that the model's computations are being offloaded to the CPU instead of being solely processed on the GPU. Offloading computations to the CPU can be useful in scenarios where the GPU memory is limited, and the CPU has more available memory. This can help prevent running out of GPU memory and potentially lead to more efficient memory usage.


`pipe.enable_vae_slicing()` : mechanism to reduce the memory footprint of a Variational Autoencoder (VAE) by slicing or partitioning the input data in a memory-efficient manner.


* You can check generated output video as Duck_is_swimming_25_sec_long video.mp4 in the files folder.



