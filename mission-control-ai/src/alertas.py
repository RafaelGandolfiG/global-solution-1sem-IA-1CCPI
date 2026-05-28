def avaliar(dados):

    alertas = []

    temperatura = dados["temperatura_payload"]
    energia = dados["energia_disponivel"]
    comunicacao = dados["comunicacao"]
    buffer = dados["buffer_imagens"]
    precisao = dados["precisao_geolocalizacao"]
    focos = dados["focos_termicos_detectados"]

    # TEMPERATURA

    if temperatura > 85:

        alertas.append(
            "🔥 ALERTA CRÍTICO: superaquecimento do payload."
        )

    elif temperatura >= 71:

        alertas.append(
            "⚠️ WARNING: temperatura elevada do payload."
        )

    # ENERGIA

    if energia < 30:

        alertas.append(
            "⚡ ALERTA CRÍTICO: energia em nível crítico."
        )

    elif energia <= 60:

        alertas.append(
            "⚠️ WARNING: energia abaixo do ideal."
        )

    # COMUNICAÇÃO

    if comunicacao == 0 \
       or comunicacao == "OFFLINE":

        alertas.append(
            "📡 ALERTA: perda de comunicação com o satélite."
        )

    # BUFFER

    if buffer > 90:

        alertas.append(
            "🗂️ ALERTA CRÍTICO: buffer próximo do limite."
        )

    elif buffer >= 71:

        alertas.append(
            "⚠️ WARNING: buffer de imagens elevado."
        )

    # GEOLOCALIZAÇÃO

    if precisao > 15:

        alertas.append(
            "📍 ALERTA: baixa precisão geolocalização."
        )

    elif precisao > 5:

        alertas.append(
            "⚠️ WARNING: precisão geolocalização moderada."
        )

    # FOCOS TÉRMICOS

    if focos > 10:

        alertas.append(
            "🔥 ALERTA AMBIENTAL: múltiplos focos térmicos detectados."
        )

    elif focos >= 4:

        alertas.append(
            "⚠️ WARNING: focos térmicos acima do normal."
        )

    if len(alertas) == 0:

        alertas.append(
            "✅ Nenhum alerta crítico detectado."
        )

    return alertas