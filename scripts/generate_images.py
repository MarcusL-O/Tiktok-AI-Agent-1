"""
generate_images.py Genererar AI-bilder (DALL·E 3) för varje scen i manuset.
Varje scenrad används som prompt till DALL·E. Alla bilder sparas i assets/images.
Returnerar en lista med filvägar till bilderna.
"""

import openai
import os
from utils.file_utils import save_image_from_url

# Hämta API-nyckel från .env
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_images_for_script(script_scenes, project_id):
    image_paths = []
    for idx, line in enumerate(script_scenes):
        try:
            scene_text = line.split(":", 1)[1].strip()
            dalle_prompt = f"{scene_text}, cartoon style, vibrant, exaggerated, cinematic lighting"

            response = openai.Image.create(
                model="dall-e-3",
                prompt=dalle_prompt,
                n=1,
                size="1024x1024"
            )

            image_url = response['data'][0]['url']
            filename = f"{project_id}_scene_{idx+1}.png"
            save_path = os.path.join("assets/images", filename)
            save_image_from_url(image_url, save_path)
            image_paths.append(save_path)

            print(f"[✅] Image saved: {save_path}")

        except Exception as e:
            print(f" Failed to generate image for scene {idx+1}: {e}")

    return image_paths
