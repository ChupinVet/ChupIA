import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError(
        "GOOGLE_API_KEY não encontrada. Configure a chave no arquivo .env"
    )

MODEL = "gemini-3.5-flash-lite"

client = genai.Client(api_key=GOOGLE_API_KEY)