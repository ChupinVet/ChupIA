import os
from dotenv import load_dotenv
from clients.java_api import consultar_pet, consultar_diarios
load_dotenv()


def consultar_dados_pet(id_pet: int) -> dict:
    token = os.getenv("JAVA_API_TOKEN")

    if not token:
        return {
            "erro": "Token de acesso à API Java não configurado."
        }

    try:
        pet = consultar_pet(id_pet, token)
        resposta_diarios = consultar_diarios(id_pet, token)

    except Exception as erro:
        return {
            "erro": f"Não foi possível consultar a API Java: {erro}"
        }

    contexto_pet = {
        "nomePet": pet.get("nomePet"),
        "especie": pet.get("especie"),
        "raca": pet.get("raca"),
        "idade": pet.get("idade"),
        "peso": pet.get("peso")
    }

    contexto_diarios = []

    for diario in resposta_diarios.get("content", []):
        contexto_diarios.append({
            "dataRegistro": diario.get("dataRegistro"),
            "humor": diario.get("humor"),
            "alimentacao": diario.get("alimentacao"),
            "consumoAgua": diario.get("consumoAgua"),
            "comportamento": diario.get("comportamento"),
            "pesoRegistrado": diario.get("pesoRegistrado")
        })

    return {
        "pet": contexto_pet,
        "diarios": contexto_diarios
    }
