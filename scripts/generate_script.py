"""
generate_script.py – Genererar ett kort Gen Z-inspirerat manus från ett ämne (prompt).
Delar upp manuset i scener med överdrivna, absurda repliker som passar TikTok-stil.
Returnerar en lista med manusrader, en per scen.
"""

import openai
import os

# Hämta API-nyckel från .env
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_script(topic, project_id):
    prompt = f"""
You're a Gen Z TikTok scriptwriter. Write a short viral skit (max 5 lines)
about this topic: "{topic}"

Style:
- Gen Z humor (absurd, over-the-top, sarcastic)
- Short, snappy scenes
- Each line is one scene, like: Scene 1: "text"

Return only the script.
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=1.1,
            max_tokens=300
        )

        raw_script = response['choices'][0]['message']['content']
        lines = [line.strip() for line in raw_script.split("\n") if line.strip() and ":" in line]
        return lines

    except Exception as e:
        print(f" Error generating script: {e}")
        return [f"Scene 1: This is a fallback script because GPT failed for topic: {topic}"]
