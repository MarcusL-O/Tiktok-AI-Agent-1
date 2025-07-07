import os
import base64
import requests
from runwayml import RunwayML, TaskFailedError

def encode_image_to_data_uri(image_path):
    with open(image_path, "rb") as f:
        image_data = f.read()
        base64_image = base64.b64encode(image_data).decode("utf-8")
        extension = os.path.splitext(image_path)[-1].lower().replace('.', '')
        return f"data:image/{extension};base64,{base64_image}"

def generate_runway_video(image_path, prompt_text, duration_seconds, output_path):
    api_key = os.getenv("RUNWAY_VIDEO_KEY")
    if not api_key:
        raise ValueError("RUNWAY_VIDEO_KEY is missing from .env or environment.")

    # 🔐 Extra skydd: Avbryt om prompten är tom
    if not prompt_text:
        raise ValueError("Prompt text is empty – can't generate video.")  # <-- NYTT

    client = RunwayML(api_key=api_key)
    data_uri = encode_image_to_data_uri(image_path)

    print("\n[DEBUG] Prompt skickas till Runway:")
    print(prompt_text)
    print("[DEBUG] Bildstorlek (bytes):", os.path.getsize(image_path))

    print(f"[🎬] Generating video with Runway for: {prompt_text}")

    try:
        # 🛑 Bonusfix: Dubbelkolla igen innan vi skickar till modellen
        if not prompt_text:
            print("[❌] Tom prompt_text skickas – avbryter.")  # <-- NYTT
            return

        task = client.image_to_video.create(
            model="gen4_turbo",
            prompt_image=data_uri,
            prompt_text=prompt_text,
            ratio="1280:720",
            duration=duration_seconds
        ).wait_for_task_output()

        video_url = task.output[0]["video"]
        video_data = requests.get(video_url)
        with open(output_path, "wb") as f:
            f.write(video_data.content)

        print(f"[✅] Runway video saved: {output_path}")
        return output_path

    except TaskFailedError as e:
        raise Exception(f"Runway task failed: {e.task_details}")

    except Exception as e:
        raise Exception(f"Runway API call error: {e}")
