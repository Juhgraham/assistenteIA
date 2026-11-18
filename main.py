import os
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq

load_dotenv(Path(__file__).with_name(".env"))

api_key = os.getenv("GROQ_API_KEY", "").strip()
if not api_key:
    raise SystemExit("Configure GROQ_API_KEY no arquivo .env ou no ambiente antes de executar.")

client = Groq(api_key=api_key)

historico = []

print("Assistente IA iniciado! Digite 'sair' para encerrar.")

while True:
    pergunta = input("\nVocê: ")

    if pergunta.lower() == "sair":
        break

    historico.append({"role": "user", "content": pergunta})

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=historico
    )

    resposta = response.choices[0].message.content
    historico.append({"role": "assistant", "content": resposta})

    print("\nIA:", resposta)
