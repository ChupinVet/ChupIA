#Simula GET /pets/{id}

PETS = {
    1: {
        "idPet": 1,
        "nomePet": "Nasus",
        "especie": "Cachorro",
        "raca": "Golden Retriever",
        "idade": 6,
        "peso": 30.5,
        "idResponsavel": 1,
        "nomeResponsavel": "João Silva"
    }
}

# Simula GET /diarios/pet/{idPet}

DIARIOS = {
    1: [
        {
            "idDiario": 4,
            "dataRegistro": "2026-06-18",
            "humor": "Mais quieto",
            "alimentacao": "Comeu menos que o normal",
            "consumoAgua": "Normal",
            "comportamento": "Dormiu mais durante o dia",
            "sintomas": "Nenhum",
            "observacoes": "Ficou menos interessado em brincar",
            "pesoRegistrado": 28.2,
            "insightIA": None,
            "idPet": 1,
            "nomePet": "Nasus"
        },
        {
            "idDiario": 3,
            "dataRegistro": "2026-06-17",
            "humor": "Calmo",
            "alimentacao": "Normal",
            "consumoAgua": "Bebeu bem",
            "comportamento": "Brincou menos que o habitual",
            "sintomas": "Nenhum",
            "observacoes": "Passou mais tempo descansando",
            "pesoRegistrado": 28.4,
            "insightIA": None,
            "idPet": 1,
            "nomePet": "Nasus"
        },
        {
            "idDiario": 2,
            "dataRegistro": "2026-06-16",
            "humor": "Feliz",
            "alimentacao": "Normal",
            "consumoAgua": "Bebeu bem",
            "comportamento": "Brincou normalmente",
            "sintomas": "Nenhum",
            "observacoes": "Rotina normal",
            "pesoRegistrado": 28.5,
            "insightIA": None,
            "idPet": 1,
            "nomePet": "Nasus"
        },
        {
            "idDiario": 1,
            "dataRegistro": "2026-06-15",
            "humor": "Feliz",
            "alimentacao": "Normal",
            "consumoAgua": "Bebeu bem",
            "comportamento": "Brincou normalmente durante o dia",
            "sintomas": "Nenhum",
            "observacoes": "Sem alterações importantes",
            "pesoRegistrado": 28.5,
            "insightIA": None,
            "idPet": 1,
            "nomePet": "Nasus"
        }
    ]
}
