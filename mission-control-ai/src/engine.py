import os

from ollama import Client
from dotenv import load_dotenv
from pathlib import Path

from src.telemetria import coletar
from src.alertas import avaliar

load_dotenv()

TRILHA = "envirosat"

host = os.getenv("OLLAMA_HOST")
model = os.getenv("OLLAMA_MODEL")

client = Client(host=host)


def llm(prompt, system=None, max_tokens=800, temperature=0.3):
    messages = []

    if system:
        messages.append({
            "role": "system",
            "content": system
        })

    messages.append({
        "role": "user",
        "content": prompt
    })

    try:
        response = client.chat(
            model=model,
            messages=messages,
            options={
                "num_predict": max_tokens,
                "temperature": temperature
            }
        )

        return response["message"]["content"]

    except Exception as e:
        return f"⚠️ Erro ao consultar IA: {e}"


def load_system_prompt():
    path = Path("prompts/system_prompt.md")

    if path.exists():
        return path.read_text(encoding="utf-8")

    return "Você é um assistente."


class MissionEngine:

    def __init__(self):
        self.trilha = TRILHA
        self.system_prompt = load_system_prompt()
        self.dados_atuais = coletar()

    def is_ready(self):
        return True

    def gerar_nova_telemetria(self):
        self.dados_atuais = coletar()
        return self.dados_atuais

    def status_snapshot(self):
        dados = self.dados_atuais
        alertas = avaliar(dados)

        status = (
            f"🛰️ Trilha: {self.trilha}\n\n"

            f"🌡️ Temperatura: {dados['temperatura_payload']}°C\n"
            f"⚡ Energia: {dados['energia_disponivel']}%\n"
            f"📡 Comunicação: {'ONLINE' if dados['comunicacao'] == 1 else 'OFFLINE'}\n"
            f"🗂️ Buffer de imagens: {dados['buffer_imagens']}%\n"
            f"📍 Precisão geolocalização: {dados['precisao_geolocalizacao']} m\n"
            f"🔥 Focos térmicos: {dados['focos_termicos_detectados']}\n\n"

            f"⚠️ Alertas:\n"
            f"{chr(10).join(alertas)}"
        )

        return status

    def analyze(self, pergunta_usuario):
        dados = self.dados_atuais
        alertas = avaliar(dados)

        prompt = f"""
Pergunta do operador:
{pergunta_usuario}

Dados atuais da telemetria:
- Temperatura: {dados['temperatura_payload']}°C
- Energia: {dados['energia_disponivel']}%
- Comunicação: {dados['comunicacao']}
- Buffer de imagens: {dados['buffer_imagens']}%
- Precisão geolocalização: {dados['precisao_geolocalizacao']} m
- Focos térmicos: {dados['focos_termicos_detectados']}

Alertas detectados:
{chr(10).join(alertas)}

Analise a situação da missão EnviroSat.
"""

        resposta = llm(
            prompt,
            system=self.system_prompt
        )

        return resposta