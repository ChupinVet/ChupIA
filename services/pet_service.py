import os
import token
from dotenv import load_dotenv
from clients.java_api import fazer_login, consultar_pet, consultar_diarios
load_dotenv()


def consultar_dados_pet(id_pet: int) -> dict:
    try:
        token = fazer_login()

        pet = consultar_pet(id_pet, token)
        resposta_diarios = consultar_diarios(id_pet, token)

    except Exception:
        return {
            "erro": "Não foi possível autenticar ou consultar os dados na API Java."
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
