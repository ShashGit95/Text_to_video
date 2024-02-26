import torch
from diffusers import DiffusionPipeline, DPMSolverMultistepScheduler
# from diffusers.utils import export_to_video
from cinematic_client.utilities import export_to_video
from PIL import Image



output_folder_path = 'static/output_video'

# Generate video
def create_video(text_prompt: str):

    global video_frames
    prompt = text_prompt

    # Customize the output name
    vid_name_1 = 'before_upscale'

    # Create pipeline
    pipe = DiffusionPipeline.from_pretrained("cerspense/zeroscope_v2_576w", torch_dtype=torch.float16)

     # Optimize for GPU memory
    # if torch.cuda.is_available():
    pipe.enable_model_cpu_offload()
        
    # Create video
    pipe.unet.enable_forward_chunking(chunk_size=1, dim=1)
    pipe.enable_vae_slicing()

    video_duration_seconds = 3
    num_frames = video_duration_seconds * 8
    # Set output path
    output_name = f'{output_folder_path}/{vid_name_1}.mp4'  
    video_frames = pipe(prompt, num_frames=num_frames).frames
    # video_frames = video_frames.reshape(-1, 256, 256, 3)
    video_path = export_to_video(video_frames, output_video_path=output_name)

    return video_path


# Upscale the video
def upscale_video(text_prompt: str):

    output_folder_path = 'static/upscaled_video'

    prompt = text_prompt

    # Customize the output name after upscaling
    vid_name_2 = 'after_upscale'

    # Load pipeline
    pipe = DiffusionPipeline.from_pretrained("cerspense/zeroscope_v2_XL", torch_dtype=torch.float16)
    pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)

    # Optimize for GPU memory
    if torch.cuda.is_available():
        pipe.enable_model_cpu_offload()
   
    pipe.unet.enable_forward_chunking(chunk_size=1, dim=1)
    pipe.enable_vae_slicing()

    # Generate the upscaled video
    video = [Image.fromarray(frame).resize((1024, 576)) for frame in video_frames]
    output_name = f'{output_folder_path}/{vid_name_2}.mp4'
    video_frames = pipe(prompt, video=video, strength=0.66).frames
    video_path = export_to_video(video_frames, output_video_path=output_name)

    return video_path
