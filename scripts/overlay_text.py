"""
overlay_text.py – Lägger in repliken (scen-texten) som overlay på varje bild.
Stilen är överdriven, TikTok-liknande (stor text, centrerad, vit med svart kant).
Bilderna skrivs över i assets/images/.
"""

from PIL import Image, ImageDraw, ImageFont
import os

def add_text_to_images(script_scenes, image_paths, project_id):
    for idx, (line, image_path) in enumerate(zip(script_scenes, image_paths)):
        try:
            scene_text = line.split(":", 1)[1].strip()

            img = Image.open(image_path).convert("RGBA")
            draw = ImageDraw.Draw(img)

            # Fontstorlek och typ (byt till annan font om du vill ha TikTok-look)
            font_path = "assets/fonts/Impact.ttf"  # ← du kan byta till t.ex. Anton.ttf, Bangers, etc
            font_size = 64

            if not os.path.exists(font_path):
                print(f" Font not found at {font_path}, using default.")
                font = ImageFont.load_default()
            else:
                font = ImageFont.truetype(font_path, font_size)

            # Radbrytning vid behov (max bredd)
            max_width = img.width - 100
            wrapped = wrap_text(scene_text, font, max_width, draw)

            # Centrera texten
            text_height = sum([draw.textsize(line, font=font)[1] for line in wrapped])
            y = (img.height - text_height) // 2

            for line in wrapped:
                text_width, text_height = draw.textsize(line, font=font)
                x = (img.width - text_width) // 2

                # Skugga (svart kant)
                draw.text((x+2, y+2), line, font=font, fill="black")
                draw.text((x-2, y+2), line, font=font, fill="black")
                draw.text((x+2, y-2), line, font=font, fill="black")
                draw.text((x-2, y-2), line, font=font, fill="black")

                # Text (vit)
                draw.text((x, y), line, font=font, fill="white")
                y += text_height + 5

            img.save(image_path)
            print(f"[📝] Text overlay added: {image_path}")

        except Exception as e:
            print(f" Failed to overlay text on image {idx+1}: {e}")


def wrap_text(text, font, max_width, draw):
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        test_line = f"{current_line} {word}".strip()
        width, _ = draw.textsize(test_line, font=font)
        if width <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word

    if current_line:
        lines.append(current_line)

    return lines
