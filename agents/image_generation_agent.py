import torch
from diffusers import StableDiffusionPipeline
import os

class ImageGenerationAgent:
    """
    Generates a product image using Stable Diffusion based on product_name/category.
    Saves to static/images/{product_id}.png if not already generated.
    """
    def __init__(self, model_name="runwayml/stable-diffusion-v1-5", output_folder="static/images"):
        self.output_folder = output_folder
        device = "cuda" if torch.cuda.is_available() else "cpu"

        print("[DEBUG] Loading Stable Diffusion model, this might take a while...")
        self.pipe = StableDiffusionPipeline.from_pretrained(
            model_name,
            torch_dtype=torch.float16 if device == "cuda" else torch.float32
        )
        self.pipe.to(device)

    def generate_image(self, product_id, product_name, category):
        prompt = f"A professional product photo of a {product_name} in the {category} category, studio lighting, highly detailed."
        print(f"[DEBUG] Generating image for {product_id} with prompt: {prompt}")

        image = self.pipe(prompt).images[0]

        # Ensure output folder exists
        os.makedirs(self.output_folder, exist_ok=True)
        out_path = os.path.join(self.output_folder, f"{product_id}.png")
        image.save(out_path)
        print(f"[DEBUG] Saved image to {out_path}")
        return out_path
