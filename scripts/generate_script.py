import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_script(topic: str) -> str:
    prompt = f"""
    Write a short, viral TikTok script in English (max 80 words) about: "{topic}".
    
    Style:
    - Gen Z humor
    - Random, exaggerated reactions
    - Meme references or viral phrases (e.g. “bro thinks he’s him”, “this ain’t no ballerina cappuccino”, “nah cause why is it kinda slay”)
    - End with a punchline or ironic twist
    """

    response = client.chat.completions.create(
        model="gpt-4", 
        messages=[
        {"role": "system", "content": "You are a humorous Gen Z TikTok script writer specialized in viral videos, Be funny, sarcastic, and internet-aware, Always make it sound like something from the 'For You Page'."},
        {"role": "user", "content": f"Create a script for a video about: {topic}"}
        ]
    )

    return response.choices[0].message.content.strip()
