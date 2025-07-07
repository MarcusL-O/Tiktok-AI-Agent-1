import os
from scripts.generate_script import generate_script
from scripts.generate_images_for_script import generate_images_for_script
from scripts.generate_video_runway import generate_runway_video
from scripts.text_to_speech import generate_voiceover
from scripts.create_video import create_final_video
from utils.file_utils import create_output_dirs


topic = "An orange cat robs a liquor store and escapes dramatically"
project_id = topic.replace(" ", "_").lower()
create_output_dirs(project_id)

script_scenes = generate_script(topic, project_id)
first_scene = script_scenes[0]
from utils.text_utils import clean_prompt
scene_text = clean_prompt(first_scene.split(":", 1)[1].strip())
if not scene_text or len(scene_text) < 10:
    scene_text = "An orange cat walks into a liquor store wearing sunglasses"


image_paths = generate_images_for_script([first_scene], project_id)
image_path = image_paths[0]

video_path = f"assets/output/{project_id}_final.mp4"
generate_runway_video(image_path=image_path, prompt_text=scene_text, duration_seconds=5, output_path=video_path)

audio_paths = generate_voiceover([first_scene], project_id)
audio_path = audio_paths[0]

create_final_video([video_path], [audio_path], music_path=None, project_id=project_id)

print(f"\n✅ Klar! Video sparad i: assets/output/{project_id}.mp4")