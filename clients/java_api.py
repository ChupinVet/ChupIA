import os

import requests
from dotenv import load_dotenv

load_dotenv()

JAVA_API_URL = os.getenv(
    "JAVA_API_URL",
    "https://javachallenge.onrender.com"
)

def fazer_login() -> str:
    email = os.getenv("JAVA_API_EMAIL")
    senha = os.getenv("JAVA_API_SENHA")

    if not email or not senha:
        raise ValueError(
            "Credenciais da API Java não configuradas no .env."
        )

    resposta = requests.post(
        f"{JAVA_API_URL}/auth/login",
        json={
            "email": email,
            "senha": senha
        },
        timeout=60
    )

    resposta.raise_for_status()

    dados = resposta.json()
    token = dados.get("token")

    if not token:
        raise ValueError("A API Java não retornou um token JWT.")

    return token

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
