import random
from datetime import datetime


def coletar():
    """Gera dados simulados de telemetria para a trilha EnviroSat."""

    dados = {
        "trilha": "EnviroSat",
        "timestamp": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),

        "temperatura_payload": random.randint(20, 95),
        "energia_disponivel": random.randint(5, 100),
        "comunicacao": random.choice([0, 1]),
        "buffer_imagens": random.randint(0, 100),
        "precisao_geolocalizacao": round(random.uniform(1.0, 30.0), 2),
        "focos_termicos_detectados": random.randint(0, 15)
    }

    return dados