import os
from datetime import datetime

from scripts.generate_script import generate_script
from scripts.text_to_speech import text_to_speech
from scripts.create_video import create_video
from scripts.generate_images import generate_image, add_text_overlay

# === Steg 0: Sätt upp mappstruktur ===
topic = "What if cats ruled the world?"
timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
project_dir = f"projects/video_{timestamp}"

images_dir = os.path.join(project_dir, "images")
audio_dir = os.path.join(project_dir, "audio")
output_path = os.path.join(project_dir, "final.mp4")

os.makedirs(images_dir, exist_ok=True)
os.makedirs(audio_dir, exist_ok=True)

# === Steg 1: Generera manus ===
script = generate_script(topic)
print("📝 Script:", script)

# === Steg 2: Generera bild baserat på manus ===
image_path = os.path.join(images_dir, "image_0.png")
generate_image(script, image_path)

# === Steg 2.5: Lägg till text på bilden ===
add_text_overlay(image_path, script)

# === Steg 3: Konvertera till AI-röst ===
audio_path = os.path.join(audio_dir, "output.mp3")
text_to_speech(script, audio_path)

# === Steg 4: Skapa video ===
create_video(image_path, audio_path, output_path)
