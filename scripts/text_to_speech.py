import requests
import os
from dotenv import load_dotenv

load_dotenv()

def text_to_speech(text, filename="assets/audio/output.mp3"):
    api_key = os.getenv("ELEVEN_API_KEY")
    voice_id = "21m00Tcm4TlvDq8ikWAM"  # Rachel – English female
    # Du kan byta ut voice_id mot en annan röst från Eleven Labs
    # HÄR KAN DU LÄGGA TILL E ANNAN RÖST 

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

    headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json"
    }

    payload = {
        "text": text,
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.7
        }
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        print("AI-röst skapad:", filename)
    else:
        print(" Något gick fel:", response.text)
