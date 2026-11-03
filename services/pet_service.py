from services.dados_simulados import PETS, DIARIOS


def consultar_dados_pet(id_pet: int) -> dict:
    pet = PETS.get(id_pet)
    diarios = DIARIOS.get(id_pet, [])

    if pet is None:
        return {
            "erro": f"Pet com id {id_pet} não encontrado."
        }

    contexto_pet = {
        "nomePet": pet["nomePet"],
        "especie": pet["especie"],
        "raca": pet["raca"],
        "idade": pet["idade"],
        "peso": pet["peso"]
    }

    contexto_diarios = []

    for diario in diarios:
        contexto_diarios.append({
            "dataRegistro": diario["dataRegistro"],
            "humor": diario["humor"],
            "alimentacao": diario["alimentacao"],
            "consumoAgua": diario["consumoAgua"],
            "comportamento": diario["comportamento"],
            "sintomas": diario["sintomas"],
            "observacoes": diario["observacoes"],
            "pesoRegistrado": diario["pesoRegistrado"]
        })

    return {
        "pet": contexto_pet,
        "diarios": contexto_diarios
    }
