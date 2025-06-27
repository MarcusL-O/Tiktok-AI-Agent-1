import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_script(topic: str) -> str:
    prompt = f"Skriv ett TikTok-manus med max 100 ord, underhållande, om ämnet: {topic}"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # eller gpt-4 om du har tillgång
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()
