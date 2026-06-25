from groq import Groq

client = Groq(api_key="coloque sua chave aqui, no readme tem as instruções")

historico = []

print("🤖 Assistente IA iniciado! Digite 'sair' para encerrar.")

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