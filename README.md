# 🤖 Assistente IA

Um assistente de IA simples no terminal usando a API gratuita do Groq com o modelo LLaMA 3.

## 🚀 Como usar

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/assistenteIA.git
cd assistenteIA
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Crie sua chave de API gratuita
- Acesse [console.groq.com](https://console.groq.com)
- Crie uma conta (pode entrar com Google)
- Vá em **API Keys** → **Create API Key**
- Copie a chave gerada

### 4. Adicione sua chave no código
Abra o arquivo `main.py` e substitua no campo `api_key`:
```python
client = Groq(api_key="cole_sua_chave_aqui")
```

### 5. Execute
```bash
python main.py
```

## 💬 Como funciona

- Digite sua mensagem e pressione Enter
- O assistente responde usando o modelo **LLaMA 3.3 70B** via Groq
- O histórico da conversa é mantido durante a sessão
- Digite `sair` para encerrar

## 📦 Tecnologias

- [Python](https://www.python.org/)
- [Groq API](https://console.groq.com) — gratuita, sem cartão
- [LLaMA 3.3 70B](https://groq.com) — modelo de linguagem da Meta

## ⚠️ Atenção

Nunca compartilhe seu `api_key` publicamente. Cada um deve usar sua própria chave gerada no Groq.