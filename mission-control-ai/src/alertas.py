def avaliar(dados):
    """Avalia os dados da missão e gera alertas."""

    alertas = []

    # Temperatura crítica

    if dados["temperatura_payload"] > 80:

        alertas.append(
            "🔥 ALERTA CRÍTICO: superaquecimento do payload."
        )

    # Energia baixa

    if dados["energia_disponivel"] < 20:

        alertas.append(
            "⚡ ALERTA: energia abaixo do nível seguro."
        )

    # Falha de comunicação

    if dados["comunicacao"] == 0:

        alertas.append(
            "📡 ALERTA: perda de comunicação com o satélite."
        )

    # Buffer cheio

    if dados["buffer_imagens"] > 85:

        alertas.append(
            "🛰️ ALERTA: buffer de imagens próximo do limite."
        )

    # Muitos focos térmicos

    if dados["focos_termicos_detectados"] > 10:

        alertas.append(
            "🌳 ALERTA AMBIENTAL: múltiplos focos térmicos detectados."
        )

    # Sem alertas

    if len(alertas) == 0:

        alertas.append(
            "✅ Missão operando normalmente."
        )

    return alertas