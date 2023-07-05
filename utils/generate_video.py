import torch
from diffusers import DiffusionPipeline, DPMSolverMultistepScheduler
from diffusers.utils import export_to_video
import cv2

def create_video(prompt, output_path='outputs//video.mp4'):
        
    pipe = DiffusionPipeline.from_pretrained("cerspense/zeroscope_v2_576w", torch_dtype=torch.float16)
    pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
    pipe.enable_model_cpu_offload()

    video_frames = pipe(prompt, num_inference_steps=40, height=320, width=576, num_frames=40).frames
    video_path = export_to_video(video_frames, output_path)
    return video_path