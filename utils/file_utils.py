import os
import requests

def create_output_dirs(project_id):
    os.makedirs("assets/images", exist_ok=True)
    os.makedirs("assets/audio", exist_ok=True)
    os.makedirs("assets/output", exist_ok=True)
    os.makedirs("assets/music", exist_ok=True)

def save_image_from_url(url, path):
    response = requests.get(url)
    with open(path, 'wb') as f:
        f.write(response.content)
