"""
main.py Kontrollerar hela AI-agentens arbetsflöde stegvis.

Flöde:
1. Läser ett prompt-ämne (kan hårdkodas eller laddas dynamiskt)
2. Genererar ett Gen Z-manus via OpenAI
3. Skapar en bild för varje scen
4. Skapar en AI-röstfil (TTS) för varje scen
5. Lägger till text-overlay på bilden
6. Väljer (valfritt) musik
7. Bygger en färdig video från alla komponenter
"""

import os
from scripts.generate_script import generate_script
from scripts.generate_images import generate_images_for_script
from scripts.text_to_speech import generate_voiceover
from scripts.overlay_text import add_text_to_images
from scripts.select_music import select_background_music
from scripts.create_video import create_final_video
from utils.file_utils import create_output_dirs

# 1. Prompt – hårdkodad för test
topic = "Why Gen Z can't handle silence"  # ← Byt detta för ny video

# 2. Skapa mappar för att spara filer
project_id = topic.replace(" ", "_").lower()
create_output_dirs(project_id)

# 3. Generera manus
script_scenes = generate_script(topic, project_id)

# 4. Generera bilder för varje scen i manuset
image_paths = generate_images_for_script(script_scenes, project_id)

# 5. Skapa röstfiler för varje scen
audio_paths = generate_voiceover(script_scenes, project_id)

# 6. Lägg text-overlay (repliken) på varje bild
add_text_to_images(script_scenes, image_paths, project_id)

# 7. Välj bakgrundsmusik (frivilligt)
music_path = select_background_music(project_id)

# 8. Skapa slutlig video
create_final_video(image_paths, audio_paths, music_path, project_id)

print(f"\n✅ Klar! Video sparad i: assets/output/{project_id}.mp4")
