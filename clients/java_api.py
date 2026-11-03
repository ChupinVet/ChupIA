import os

import requests
from dotenv import load_dotenv

load_dotenv()

JAVA_API_URL = os.getenv(
    "JAVA_API_URL",
    "https://javachallenge.onrender.com"
)


def consultar_pet(id_pet: int, token: str) -> dict:
    resposta = requests.get(
        f"{JAVA_API_URL}/pets/{id_pet}",
        headers={"Authorization": f"Bearer {token}"},
        timeout=30
    )
    resposta.raise_for_status()
    return resposta.json()


def consultar_diarios(id_pet: int, token: str) -> dict:
    resposta = requests.get(
        f"{JAVA_API_URL}/diarios/pet/{id_pet}",
        headers={"Authorization": f"Bearer {token}"},
        timeout=30
    )
    resposta.raise_for_status()
    return resposta.json()
