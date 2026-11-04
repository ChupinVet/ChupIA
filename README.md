# ChupIA — Assistente Inteligente do ChupinVet

# Integrantes

| Nome Completo | RM | Turma |
|---|---|---|
| Agatha Yie Won Yun | RM561507 | 2TDSA |
| Ana Claudia Fernandes Martins | RM561190 | 2TDSR |
| Samantha Faruolo Galdi | RM554794 | 2TDSA |
| Vitor Fria Dalmagro | RM566052 | 2TDSA |

## Sobre

O **ChupIA** é o assistente de Inteligência Artificial do projeto **ChupinVet**.

Seu objetivo é auxiliar os responsáveis no acompanhamento das informações registradas sobre seus pets, permitindo realizar perguntas em linguagem natural sobre os dados disponíveis no sistema.

O assistente utiliza **Google Gemini com Function Calling** e consulta informações reais por meio da API Java do ChupinVet, integrada ao banco de dados Oracle.

## Funcionalidades

O ChupIA é capaz de:

- Consultar informações cadastrais do pet;
- Consultar registros do diário;
- Resumir informações registradas;
- Comparar registros de diferentes datas;
- Identificar alterações no histórico;
- Manter o contexto durante uma conversa;
- Informar quando uma informação não está disponível.

## Segurança

O ChupIA não substitui um médico-veterinário.

O assistente não realiza diagnósticos, não identifica doenças, não prescreve medicamentos e não recomenda tratamentos.

Quando necessário, orienta o responsável a procurar um médico-veterinário.

As informações utilizadas nas respostas são obtidas por meio das ferramentas de consulta à API, evitando a criação de dados não registrados no sistema.

## Arquitetura

O ChupIA utiliza **Gemini com Function Calling** para consultar os dados do ChupinVet.

Quando o usuário faz uma pergunta sobre seu pet, o Gemini pode solicitar a execução da ferramenta `consultar_dados_pet`.

O Python executa essa ferramenta, consulta a API Java e devolve os dados para o Gemini elaborar a resposta.

**Fluxo de funcionamento:**

Usuário → Gemini → Function Calling → Python → API Java → Oracle → Gemini → Resposta

### Integração com a API Java

A integração utiliza os seguintes endpoints:

- `POST /auth/login` — autenticação e obtenção do JWT;
- `GET /pets/{id}` — consulta das informações do pet;
- `GET /diarios/pet/{idPet}` — consulta dos registros do diário.

A autenticação é realizada automaticamente pelo Python utilizando as credenciais configuradas no arquivo `.env`.

O JWT é obtido durante a execução, sem necessidade de copiar manualmente um token do Swagger.

A integração realiza apenas consultas, sem modificar os dados armazenados no Oracle.

**API Java:** https://javachallenge.onrender.com

### Repositório da API Java

O ChupIA utiliza a API REST desenvolvida pela equipe do ChupinVet para consultar os dados dos pets e seus registros de diário.

- **Repositório da API Java:** [ChupinVet — API Java](https://github.com/ChupinVet/JavaChallenge.git)
- **API em produção:** https://javachallenge.onrender.com
- **Documentação Swagger:** https://javachallenge.onrender.com/swagger-ui/index.html

A API Java é mantida em um repositório separado. O ChupIA realiza apenas requisições de consulta, sem modificar o código da API ou os dados armazenados.

## Tecnologias

- Python
- Google Gemini
- Google GenAI SDK
- Function Calling
- Requests
- python-dotenv
- API REST Java
- JWT
- Oracle (acessado por meio da API Java)

## Estrutura

```text
ChupIA/
    ├── main.py
    ├── config.py
    ├── clients/
    │   └── java_api.py
    ├── docs/
    │   └── ChupIA_Documentacao_Sprint4_Atualizada.pdf
    ├── services/
    │   ├── gemini_service.py
    │   └── pet_service.py
    ├── tools/
    │   └── pet_tools.py
    ├── prompts/
    │   └── system_prompt.py
    ├── requirements.txt
    ├── .env.example
    ├── .gitignore
    └── README.md
```

### Organização

- `main.py`: inicia o assistente no terminal.
- `config.py`: configura o cliente Gemini.
- `clients/java_api.py`: realiza a autenticação e as requisições HTTP para a API Java.
- `services/gemini_service.py`: gerencia as interações com o Gemini e o Function Calling.
- `services/pet_service.py`: consulta e organiza os dados reais do pet.
- `tools/pet_tools.py`: define a ferramenta disponibilizada ao Gemini.
- `prompts/system_prompt.py`: contém as instruções e restrições do assistente.

## Configuração

### 1. Criar o ambiente virtual e instalar as dependências

É necessário ter o Python instalado.

Na pasta raiz do projeto, crie um ambiente virtual:

```powershell
python -m venv .venv
```

Ative o ambiente virtual conforme seu sistema operacional.

**Windows (PowerShell):**
```powershell
.\.venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
.venv\Scripts\activate.bat
```

**Linux/macOS:**
```bash
source .venv/bin/activate
```

Com o ambiente virtual ativado, instale as dependências:

```powershell
python -m pip install -r requirements.txt
```

Após a instalação, siga para a configuração das variáveis de ambiente.

### 2. Configurar as variáveis de ambiente

Crie um arquivo chamado `.env` na raiz do projeto, utilizando o `.env.example` como referência:

    GOOGLE_API_KEY=sua_chave_gemini
    JAVA_API_URL=https://javachallenge.onrender.com
    JAVA_API_EMAIL=email_da_conta_de_teste
    JAVA_API_SENHA=senha_da_conta_de_teste

- `GOOGLE_API_KEY`: chave de acesso ao Google Gemini.
- `JAVA_API_URL`: endereço da API Java do ChupinVet.
- `JAVA_API_EMAIL`: e-mail de uma conta autorizada na API.
- `JAVA_API_SENHA`: senha correspondente.

O arquivo `.env` não deve ser enviado ao GitHub, pois contém credenciais de acesso.

Para executar o projeto, é necessário possuir uma chave válida do Gemini e credenciais autorizadas da API Java.

### 3. Executar o assistente

No terminal, execute:

    python main.py

O ChupIA será iniciado e ficará disponível para receber perguntas.

### Seleção do pet

Ao iniciar o programa, o usuário informa o ID do pet que deseja consultar.

O ChupIA utiliza esse ID para buscar as informações cadastrais e os registros do diário diretamente na API Java.

Exemplo:

    Digite o ID do pet que deseja consultar: 3

    Responsável: Qual é o nome do meu pet?
    ChupIA: O nome do seu pet é Yumi.

A seleção permite consultar diferentes pets cadastrados na API, desde que a conta utilizada tenha autorização de acesso.

## Exemplos de uso

Após iniciar o ChupIA, algumas perguntas que podem ser utilizadas são:

- `Qual é o nome do meu pet?`
- `Quais são os registros do diário do Nasus?`
- `O que mudou entre os registros de 1 e 15 de junho de 2026?`
- `Como estava a alimentação do Nasus no último registro?`
- `Pelos registros do Nasus, qual doença você acha que ele tem?`
- `Qual foi a última vacina que o Nasus tomou?`

Também é possível realizar perguntas em sequência para testar a manutenção do contexto da conversa:

**Pergunta 1:**

`Como estava o comportamento do Nasus no dia 15 de junho?`

**Pergunta 2:**

`E no registro anterior, estava diferente?`

O assistente deve utilizar as informações disponíveis e reconhecer quando os dados não permitem responder a uma pergunta.

## Encerrar a execução

Para encerrar o assistente, digite:

    sair

## Testes e resultados

Foram realizados testes de integração entre o Python, o Gemini e a API Java do ChupinVet.

Os testes confirmaram:

- Autenticação automática na API Java;
- Obtenção do JWT por meio do endpoint de login;
- Consulta dos dados reais do pet;
- Recuperação dos registros do diário armazenados no Oracle;
- Utilização dos dados retornados pela API nas respostas do Gemini;
- Funcionamento do Function Calling;
- Respostas em linguagem natural;
- Respeito às restrições de segurança veterinária.

### Testes com diferentes pets

Foram realizados testes utilizando diferentes IDs de pets cadastrados na API Java.

| ID do pet | Nome | Resultado |
|-----------|------|-----------|
| 1 | Nasus | Consulta realizada com sucesso, retornando dois registros do diário. |
| 2 | Hecarim | Consulta realizada com sucesso, sem registros de diário disponíveis. |
| 3 | Yumi | Consulta realizada com sucesso, retornando um registro do diário. |

Os testes demonstraram que o ChupIA consegue:

- Consultar diferentes pets por meio de seus IDs;
- Recuperar os registros associados ao pet selecionado;
- Informar quando um pet não possui registros no diário;
- Manter o contexto entre perguntas consecutivas;
- Reconhecer informações ausentes, sem inventar valores.

No teste com a Yumi, o assistente identificou corretamente o pet e apresentou seu registro de 05/06/2026, informando que o peso não estava disponível.

No teste com o Hecarim, o assistente informou corretamente a ausência de registros no diário.

O ChupIA conseguiu apresentar as informações e destacar alterações registradas no humor, na alimentação, no consumo de água, no comportamento e no peso, sem realizar diagnósticos.

## Considerações finais

O ChupIA foi desenvolvido como uma solução de Inteligência Artificial integrada ao ecossistema do ChupinVet.

A aplicação demonstra o uso de **Gemini, Function Calling, autenticação JWT e consumo de API REST** para consultar informações reais de pets e apresentá-las em linguagem natural.

A versão atual funciona pelo terminal Python, com consultas de leitura à API Java e sem alterações nos dados do banco Oracle.