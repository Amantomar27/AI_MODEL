import torch
from transformers import StableDiffusionPipeline

# Load Stable Diffusion Model
pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v-1-4-original")
pipe = pipe.to("cuda")

def generate_image(prompt):
    image = pipe(prompt).images[0]
    return image
