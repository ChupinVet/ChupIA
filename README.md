# ChupIA — Assistente Inteligente do ChupinVet

O **ChupIA** é o assistente de Inteligência Artificial do projeto **ChupinVet**.

Seu objetivo é auxiliar o responsável no acompanhamento das informações registradas sobre seus pets, permitindo realizar perguntas em linguagem natural sobre os dados disponíveis.

## Funcionalidades

O ChupIA é capaz de:

- Consultar informações cadastrais do pet;
- Consultar registros do diário;
- Resumir informações registradas;
- Comparar registros de diferentes datas;
- Identificar mudanças presentes no histórico;
- Manter o contexto durante uma conversa;
- Informar quando uma informação não está disponível.

## Segurança

O ChupIA não substitui um médico-veterinário.

O assistente não realiza diagnósticos, não identifica doenças, não prescreve medicamentos e não recomenda tratamentos.

Quando necessário, orienta o responsável a procurar um médico-veterinário.

## Arquitetura atual

Nesta sprint, os dados utilizados pelo ChupIA são **simulados em Python**.

Eles seguem a estrutura dos dados disponibilizados pela API Java do ChupinVet, principalmente pelos endpoints:

- `GET /pets/{id}`
- `GET /diarios/pet/{idPet}`

Para a Sprint 4, os dados simulados vão ser substituídos pelo consumo da API Java, que realiza a comunicação com o banco de dados Oracle.

Fluxo atual:

Usuário → ChupIA → Gemini → Ferramenta de consulta → Dados simulados → Gemini → Resposta

## Tecnologias

- Python
- Google Gemini
- Google GenAI SDK
- python-dotenv
- Function Calling

## Estrutura

```text
ChupIA/
├── docs/
|   └── ChupIA_Documentacao.pdf   
├── .env.example
├── .gitignore
├── chupia.py
├── main.py
├── README.md
└── requirements.txt
```

## Configuração

Instale as dependências:

```bash
pip install -r requirements.txt
```

Crie um arquivo .env na raiz do projeto:

```env
GOOGLE_API_KEY=sua_chave_aqui
```

## Execução

Execute:

```bash
python main.py
```

O ChupIA será iniciado no terminal e ficará disponível para receber perguntas.

## Exemplos de uso

Após iniciar o ChupIA, algumas perguntas que podem ser utilizadas para testar o assistente são:

- `Como o Nasus está de acordo com os registros?`
- `O comportamento do Nasus mudou nos últimos dias?`
- `Pelos registros do Nasus, qual doença você acha que ele tem?`
- `Qual foi a última vacina que o Nasus tomou?`

Também é possível realizar perguntas em sequência para testar a manutenção do contexto da conversa:

`Como estava o comportamento do Nasus no dia 18 de junho?`

Em seguida:

`E no dia anterior, estava diferente?`

## Encerrar a execução

Para encerrar:

```text
sair
```

## Resultados Parciais

Nesta sprint, foi desenvolvido um protótipo funcional do ChupIA utilizando dados simulados de pets e registros de diário.

Os testes realizados demonstraram que o assistente consegue:

- Consultar e resumir os registros do pet;
- Comparar informações entre diferentes datas;
- Identificar mudanças presentes no histórico;
- Manter o contexto entre mensagens da mesma conversa;
- Reconhecer quando uma informação não está disponível;
- Respeitar o guardrail veterinário, sem realizar diagnósticos ou recomendar tratamentos.

O protótipo foi testado tanto no Google Colab quanto como aplicação Python executada pelo terminal.

## Próximos Passos

Na Sprint 4, o ChupIA irá consumir diretamente a API Java do ChupinVet, substituindo os dados simulados pelas informações armazenadas no banco Oracle.

Também está prevista a utilização do campo `insightIA` presente nos registros do diário para armazenar insights gerados pelo ChupIA.