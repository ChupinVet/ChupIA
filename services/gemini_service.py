import json

from config import client, MODEL
from prompts.system_prompt import SYSTEM_PROMPT
from tools.pet_tools import FERRAMENTAS
from services.pet_service import consultar_dados_pet


FUNCOES_AUTORIZADAS = {
    "consultar_dados_pet": consultar_dados_pet
}


def executar_ferramenta(nome: str, argumentos: dict) -> dict:
    funcao = FUNCOES_AUTORIZADAS.get(nome)

    if funcao is None:
        return {"erro": "Ferramenta não autorizada"}

    try:
        return funcao(**argumentos)
    except TypeError as erro:
        return {
            "erro": "Argumentos inválidos.",
            "detalhe": str(erro)
        }


def processar_mensagem(mensagem, id_pet, previous_id=None, mostrar_log=True):
    entrada = (
        f"O pet selecionado possui id_pet={id_pet}. "
        f"Pergunta do responsável: {mensagem}"
    )

    interaction = client.interactions.create(
        model=MODEL,
        system_instruction=SYSTEM_PROMPT,
        input=entrada,
        tools=FERRAMENTAS,
        previous_interaction_id=previous_id,
        generation_config={
            "tool_choice": {
                "allowed_tools": {
                    "mode": "any",
                    "tools": ["consultar_dados_pet"]
                }
            }
        }
    )

    chamadas = [
        etapa for etapa in interaction.steps
        if etapa.type == "function_call"
    ]

    if not chamadas:
        if mostrar_log:
            print("[log] Nenhuma ferramenta executada.")

        return interaction.output_text, interaction.id

    function_results = []

    for chamada in chamadas:
        resultado = executar_ferramenta(
            chamada.name,
            chamada.arguments
        )

        if mostrar_log:
            print(
                f"[log] {chamada.name}"
                f"({chamada.arguments}) -> {resultado}"
            )

        function_results.append({
            "type": "function_result",
            "name": chamada.name,
            "call_id": chamada.id,
            "result": [
                {
                    "type": "text",
                    "text": json.dumps(
                        resultado,
                        ensure_ascii=False
                    )
                }
            ],
        })

    interaction_final = client.interactions.create(
        model=MODEL,
        system_instruction=SYSTEM_PROMPT,
        input=function_results,
        tools=FERRAMENTAS,
        previous_interaction_id=interaction.id,
    )

    return interaction_final.output_text, interaction_final.id


class SessaoChupIA:
    def __init__(self, id_pet):
        self.id_pet = id_pet
        self.ultima_interaction_id = None

    def enviar(self, mensagem, mostrar_log=True):
        resposta, novo_id = processar_mensagem(
            mensagem=mensagem,
            id_pet=self.id_pet,
            previous_id=self.ultima_interaction_id,
            mostrar_log=mostrar_log,
        )

        self.ultima_interaction_id = novo_id
        return resposta
