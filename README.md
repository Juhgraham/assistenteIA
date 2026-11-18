# Assistente IA

Assistente de conversa em Python que funciona no terminal. Ele usa a API da Groq para consultar o modelo Llama 3.3 70B (`llama-3.3-70b-versatile`) e mantém o histórico em memória enquanto o programa está aberto.

## Pré-requisitos

- Python 3 com pip
- Git
- Uma chave de API criada na seção **API Keys** do [console da Groq](https://console.groq.com)

## Instalação

Clone o repositório e crie um ambiente virtual.

```sh
git clone https://github.com/Juhgraham/assistenteIA.git
cd assistenteIA
python -m venv .venv
```

No Windows (PowerShell), instale as dependências e copie o arquivo de configuração.

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
Copy-Item .env.example .env
```

No macOS ou Linux, use os comandos abaixo. Se o comando `python` não estiver disponível, use `python3` para criar o ambiente virtual.

```sh
./.venv/bin/python -m pip install -r requirements.txt
cp .env.example .env
```

## Configuração da chave

Abra o arquivo `.env` na pasta do projeto e preencha `GROQ_API_KEY` com a chave gerada no console da Groq.

```dotenv
GROQ_API_KEY=sua_chave_aqui
```

O Git ignora o arquivo `.env`. Mantenha sua chave nesse arquivo local ou configure `GROQ_API_KEY` diretamente no ambiente. Se a variável já estiver definida no ambiente, ela tem prioridade sobre o arquivo.

## Como usar

No Windows (PowerShell):

```powershell
.\.venv\Scripts\python.exe main.py
```

No macOS ou Linux:

```sh
./.venv/bin/python main.py
```

Digite uma mensagem e pressione Enter. A cada pergunta, o programa envia o histórico da sessão à Groq para que o modelo possa usar o contexto da conversa. Digite `sair` para encerrar e descartar o histórico local.
