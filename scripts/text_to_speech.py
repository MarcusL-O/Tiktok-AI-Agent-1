"""
text_to_speech.py – Skapar AI-röst (TTS) för varje scenrad i manuset.
Använder ElevenLabs API. Sparar varje ljudfil i assets/audio/.
Returnerar en lista med filvägar till röstklippen.
"""

import os
import requests
from dotenv import load_dotenv

load_dotenv()

ELEVEN_API_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID")  # Du kan ha flera röster – byt enkelt i .env

HEADERS = {
    "xi-api-key": ELEVEN_API_KEY,
    "Content-Type": "application/json"
}

def generate_voiceover(script_scenes, project_id):
    audio_paths = []

    for idx, line in enumerate(script_scenes):
        try:
            scene_text = line.split(":", 1)[1].strip()
            url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

            body = {
                "text": scene_text,
                "model_id": "eleven_multilingual_v2",
                "voice_settings": {
                    "stability": 0.4,
                    "similarity_boost": 0.75
                }
            }

            response = requests.post(url, headers=HEADERS, json=body)
            if response.status_code != 200:
                raise Exception(response.text)

            filename = f"{project_id}_scene_{idx+1}.mp3"
            save_path = os.path.join("assets/audio", filename)

            with open(save_path, 'wb') as f:
                f.write(response.content)

            print(f"[🎙️] Voiceover saved: {save_path}")
            audio_paths.append(save_path)

        except Exception as e:
            print(f"Failed to generate voice for scene {idx+1}: {e}")

    return audio_paths
