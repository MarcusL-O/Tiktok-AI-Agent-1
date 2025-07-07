import os
import requests
from PIL import Image
from io import BytesIO

def generate_images_for_script(script_scenes, project_id):
    image_paths = []
    for idx, scene in enumerate(script_scenes):
        try:
            prompt = scene.split(":", 1)[1].strip()
            response = requests.post(
                "https://api.openai.com/v1/images/generations",
                headers={
                    "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "dall-e-3",
                    "prompt": prompt,
                    "n": 1,
                    "size": "1024x1024"
                }
            )
            image_url = response.json()["data"][0]["url"]
            image_data = requests.get(image_url).content
            image_path = f"assets/images/{project_id}_scene_{idx+1}.png"
            with open(image_path, "wb") as f:
                f.write(image_data)
            print(f"[✅] Image saved: {image_path}")
            image_paths.append(image_path)
        except Exception as e:
            print(f"[❌] Failed to generate image: {e}")
    return image_paths
