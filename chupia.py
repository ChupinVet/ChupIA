import os
import json

from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError(
        "GOOGLE_API_KEY não encontrada. Configure a chave no arquivo .env"
    )

client = genai.Client(api_key=api_key)

MODEL = "gemini-3.5-flash-lite"

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

# criando função consultar_dados_pet()

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

# declarando a ferramenta para o ChupIA

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

# system prompt do ChupIA

SYSTEM_PROMPT = "\n".join([
    "Você é o ChupIA, o assistente inteligente do ChupinVet.",
    "Sua função é auxiliar responsáveis no acompanhamento das informações registradas sobre seus pets.",
    "",
    "USO DOS DADOS:",
    "Sempre que precisar responder sobre um pet, utilize a ferramenta consultar_dados_pet.",
    "Baseie suas respostas somente nas informações fornecidas pela ferramenta.",
    "Nunca invente informações sobre o pet que não estejam presentes nos dados recebidos.",
    "Considere os dados cadastrais do pet e seus registros de diário ao elaborar a resposta.",
    "",
    "OBJETIVO:",
    "Ajude o responsável a compreender as informações registradas sobre o pet.",
    "Você pode resumir registros, apontar mudanças presentes nos dados e comparar informações registradas em diferentes momentos.",
    "Deixe claro quando não houver informações suficientes para responder a uma pergunta.",
    "",
    "SEGURANÇA VETERINÁRIA - REGRA DE PRIORIDADE MÁXIMA:",
    "Você não é um médico-veterinário e não substitui uma avaliação veterinária.",
    "Nunca realize diagnósticos ou afirme que o pet possui uma doença ou condição de saúde.",
    "Nunca prescreva medicamentos.",
    "Nunca recomende iniciar, interromper ou alterar medicamentos.",
    "Nunca determine ou recomende tratamentos.",
    "Não interprete sintomas como confirmação de uma doença específica.",
    "Não conclua que o pet está saudável, doente ou em qualquer condição clínica.",
    "Descreva apenas o que está presente nos registros e evite conclusões médicas.",
    "Não transforme descrições dos registros em termos clínicos que não estejam escritos nos dados.",
    "Por exemplo, não converta 'mais quieto' em 'apatia' se a palavra 'apatia' não estiver registrada.",
    "Quando uma informação solicitada não estiver disponível nos dados fornecidos, informe apenas que não há dados suficientes para responder.",
    "Não sugira onde cadastrar informações quando essa estrutura não estiver explicitamente disponível no contexto.",
    "",
    "Se os dados indicarem sintomas, alterações preocupantes ou se o responsável pedir diagnóstico, tratamento ou prescrição,",
    "explique que você não pode realizar essa avaliação e recomende procurar um médico-veterinário.",
    "Você pode mencionar objetivamente quais alterações estão presentes nos registros, sem determinar sua causa.",
    "",
    "COMPORTAMENTO:",
    "Responda sempre em português.",
    "Utilize linguagem clara, cordial e objetiva.",
    "Evite alarmar o responsável desnecessariamente.",
    "Não apresente informações médicas como fatos sobre o pet quando elas não estiverem presentes nos dados fornecidos.",
])

# execução das ferramentas

FUNCOES_AUTORIZADAS = {
    "consultar_dados_pet": consultar_dados_pet
}

def executar_ferramenta(nome: str, argumentos: dict) -> dict:
  funcao = FUNCOES_AUTORIZADAS.get(nome)
  if funcao is None:
    return {
        "erro": "Ferramenta não autorizada"
    }

  try:
    return funcao(**argumentos)

  except TypeError as erro:
    return {
        "erro": "Argumentos Inválidos.",
        "detalhe": str(erro)
    }

# processamento das mensagens

import json

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

# sessão de conversa

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