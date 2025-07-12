import os
from groq import Groq
from dotenv import load_dotenv
from utils.prompt_utils import wrap_prompt_for_llm
from utils.config import DEFAULT_MODEL

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_manim_code(prompt: str) -> str:
    formatted = wrap_prompt_for_llm(prompt)
    response = client.chat.completions.create(
        model=DEFAULT_MODEL,
        messages=[
            {"role": "system", "content": "You are a Manim expert."},
            {"role": "user", "content": formatted}
        ],
        max_tokens=2048,
        temperature=0.3,
    )
    return response.choices[0].message.content.strip()
