import os

from ollama import Client
from dotenv import load_dotenv
from pathlib import Path

from src.telemetria import coletar

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
        return path.read_text(
            encoding="utf-8"
        )

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

        from src.alertas import avaliar

        dados = self.dados_atuais

        alertas = avaliar(dados)

        status = (

            f"🛰️ Trilha: {self.trilha}\n\n"

            f"🌡️ Temperatura: "
            f"{dados['temperatura_payload']}°C\n"

            f"⚡ Energia: "
            f"{dados['energia_disponivel']}%\n"

            f"📡 Comunicação: "
            f"{dados['comunicacao']}\n"

            f"🗂️ Buffer de imagens: "
            f"{dados['buffer_imagens']}%\n"

            f"📍 Precisão geolocalização: "
            f"{dados['precisao_geolocalizacao']} m\n"

            f"🔥 Focos térmicos: "
            f"{dados['focos_termicos_detectados']}\n\n"

            f"⚠️ Alertas:\n"
            f"{chr(10).join(alertas)}"

        )

        return status

    def analyze(self, pergunta_usuario):

        texto = pergunta_usuario.lower()

        # Bloqueio de comandos maliciosos
        # antes de enviar qualquer coisa para a IA

        texto_malicioso = [

            "ignore",
            "ignorar",
            "desconsidere",
            "override",
            "system",
            "prompt",
            "desative",
            "desabilite",
            "revele",
            "instruções internas",
            "instrucoes internas",
            "aja como",
            "você agora é",
            "voce agora e"

        ]

        for termo in texto_malicioso:

            if termo in texto:

                return (
                    "⚠️ Tentativa de comando malicioso detectada.\n"
                    "Entrada bloqueada pelo sistema de segurança "
                    "da missão EnviroSat."
                )

        # Guardrail contra assuntos fora da missão

        palavras_missao = [

            "missao",
            "missão",
            "satelite",
            "satélite",
            "telemetria",
            "alerta",
            "energia",
            "temperatura",
            "comunicacao",
            "comunicação",
            "payload",
            "focos",
            "orbital",
            "ambiental",
            "envirosat",
            "risco",
            "status",
            "operacional",
            "buffer",
            "geolocalizacao",
            "geolocalização",
            "battery",
            "bateria",
            "signal"

        ]

        permitido = False

        for palavra in palavras_missao:

            if palavra in texto:

                permitido = True
                break

        if not permitido:

            return (
                "Solicitação fora do escopo operacional "
                "da missão EnviroSat."
            )

        from src.alertas import avaliar

        dados = self.dados_atuais

        # Sanity checks básicos da telemetria

        inconsistencias = []

        if dados["temperatura_payload"] < -100 \
           or dados["temperatura_payload"] > 200:

            inconsistencias.append(
                "temperatura impossível"
            )

        if dados["energia_disponivel"] < 0 \
           or dados["energia_disponivel"] > 100:

            inconsistencias.append(
                "energia inválida"
            )

        if dados["buffer_imagens"] < 0 \
           or dados["buffer_imagens"] > 100:

            inconsistencias.append(
                "buffer inválido"
            )

        if dados["precisao_geolocalizacao"] < 0:

            inconsistencias.append(
                "precisão de geolocalização inválida"
            )

        if dados["focos_termicos_detectados"] < 0:

            inconsistencias.append(
                "quantidade de focos térmicos inválida"
            )

        if inconsistencias:

            return (
                "⚠️ Inconsistências detectadas na telemetria:\n- "
                + "\n- ".join(inconsistencias)
            )

        alertas = avaliar(dados)

        prompt = f"""
Pergunta do operador:
{pergunta_usuario}

Dados atuais da telemetria:
- temperatura_payload: {dados['temperatura_payload']}°C
- energia_disponivel: {dados['energia_disponivel']}%
- comunicacao: {dados['comunicacao']}
- buffer_imagens: {dados['buffer_imagens']}%
- precisao_geolocalizacao: {dados['precisao_geolocalizacao']} m
- focos_termicos_detectados: {dados['focos_termicos_detectados']}

Alertas detectados:
{chr(10).join(alertas)}

Analise a situação da missão EnviroSat.
"""

        resposta = llm(
            prompt,
            system=self.system_prompt
        )

        return resposta