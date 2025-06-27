import os
import requests
from PIL import Image, ImageDraw, ImageFont
from dotenv import load_dotenv

load_dotenv()

def add_text_overlay(image_path, text):
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)

    # Justera fontväg beroende på system – detta funkar för Mac
    font_path = "/Library/Fonts/Arial Bold.ttf"
    font_size = 48
    font = ImageFont.truetype(font_path, font_size)

    # Placera text längst ner på bilden
    x = 50
    y = img.height - 100
    draw.text((x, y), text, font=font, fill="white")

    img.save(image_path)
    print("🖍️ Text overlay tillagd på bilden.")

def generate_image(topic: str, output_path="assets/images/generated/output.png"):
    api_key = os.getenv("OPENAI_API_KEY")
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    prompt = f"""
    Generate a surreal and humorous image based on the topic: "{topic}". 
    Make it look like a viral meme or TikTok-core image. Style should be chaotic, exaggerated, and absurd.
    
    Examples:
    - A cat in a tuxedo playing saxophone in space
    - A crocodile drinking iced coffee in a nightclub
    - A chicken breakdancing on the moon with sunglasses

    Keep it colorful and eye-catching, like it's meant for Gen Z meme content.
    """

    data = {
        "model": "dall-e-3",
        "prompt": prompt.strip(),
        "n": 1,
        "size": "1024x1024"
    }

    response = requests.post(
        "https://api.openai.com/v1/images/generations",
        headers=headers,
        json=data
    )

    if response.status_code == 200:
        image_url = response.json()['data'][0]['url']
        image_data = requests.get(image_url).content
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "wb") as f:
            f.write(image_data)
        print(f"🖼️ Meme-bild skapad och sparad som: {output_path}")

        # Lägg på texten över bilden
        add_text_overlay(output_path, topic)
    else:
        print("Kunde inte generera bild:", response.text)
