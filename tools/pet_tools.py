FERRAMENTAS = [
    {
        "type": "function",
        "name": "consultar_dados_pet",
        "description": (
            "Consulta os dados cadastrais e os registros do diário "
            "de um pet do ChupinVet. Use esta ferramenta quando precisar "
            "de informações sobre o pet para responder ao responsável."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "id_pet": {
                    "type": "integer",
                    "description": "ID do pet selecionado no ChupinVet"
                }
            },
            "required": ["id_pet"]
        }
    }
]