# 🚀 Mission Control AI — EnviroSat Guardian

Sistema inteligente de monitoramento espacial com IA generativa para análise operacional da missão EnviroSat.

---

# 👨‍💻 Integrantes

- Rafael Gandolfi — RM: 569036 — Turma: 1CCPI
- Guilherme Miranda — RM: 573107 — Turma: 1CCPI
- Carlos Eduardo — RM: 572949 — Turma: 1CCPI

---

# 🌎 O que o projeto faz

O Mission Control AI é um sistema de monitoramento espacial desenvolvido em Python para simular operações de um satélite ambiental da trilha EnviroSat.

O sistema coleta dados simulados de telemetria, identifica falhas operacionais automaticamente e utiliza Inteligência Artificial com o modelo llama3.1 via Ollama Local para interpretar riscos da missão.

A solução:
- monitora parâmetros críticos;
- identifica alertas automaticamente;
- gera análises contextualizadas;
- recomenda ações operacionais;
- protege contra prompt injection e uso indevido da IA.

---

# 🛰️ Persona atendida

O sistema foi desenvolvido para operadores espaciais, engenheiros de missão e equipes de monitoramento ambiental responsáveis pelo acompanhamento operacional de satélites ambientais.

A solução também pode auxiliar órgãos ambientais responsáveis pelo monitoramento de incêndios florestais e riscos ambientais.

---

# ⚙️ Tecnologias utilizadas

## Linguagem
- Python 3.10+

## Inteligência Artificial
- Ollama Local
- Modelo llama3.1

## Bibliotecas
- ollama
- python-dotenv
- rich
- prompt-toolkit
- pyfiglet

---

# 🧠 Arquitetura utilizada

O projeto utiliza Ollama Local com o modelo llama3.1 executado localmente.

Diferente da arquitetura baseada em Ollama Cloud apresentada nos exemplos iniciais da disciplina, o grupo optou por execução local visando:
- independência de APIs externas;
- menor custo operacional;
- facilidade de testes;
- maior estabilidade durante demonstrações;
- maior controle do ambiente.

---

# 📁 Estrutura do projeto

```txt
mission-control-ai/
│
├── main.py
├── banner_ascii.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
│
├── src/
│   ├── __init__.py
│   ├── ui.py
│   ├── engine.py
│   ├── telemetria.py
│   └── alertas.py
│
├── prompts/
│   ├── system_prompt.md
│   ├── system_prompt_v1.md
│   ├── system_prompt_v2.md
│   └── system_prompt_v3.md
│
├── data/
│   └── cenarios.json
│
└── assets/
```

---

# ▶️ Como executar

## 1. Clone o repositório

```bash
git clone https://github.com/RafaelGandolfiG/global-solution-1sem-IA-1CCPI.git
```

---

## 2. Crie o ambiente virtual

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / MacOS

```bash
python -m venv .venv
source .venv/bin/activate
```

---

## 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

## 4. Configure o arquivo `.env`

Crie um arquivo `.env` na raiz:

```env
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=llama3.1
```

---

## 5. Execute o Ollama

```bash
ollama run llama3.1
```

---

## 6. Execute o sistema

```bash
python main.py
```

---

# 🧠 Funcionalidades implementadas

✅ Simulação de telemetria espacial

✅ Alertas automáticos

✅ Integração com IA generativa

✅ Interface CLI interativa

✅ Geração dinâmica de cenários

✅ Análise contextualizada da missão

✅ Versionamento de prompts

✅ Guardrails contra prompt injection

✅ Anti-hallucination

✅ Validação operacional da telemetria

✅ Bloqueio de assuntos fora da missão

✅ Detecção de telemetria maliciosa

---

# 📊 Telemetria monitorada

O sistema monitora:
- temperatura do payload;
- energia disponível;
- comunicação orbital;
- buffer de imagens;
- precisão geolocalização;
- focos térmicos ambientais.

---

# 🚨 Sistema de alertas

O sistema identifica automaticamente:
- superaquecimento;
- energia crítica;
- perda de comunicação;
- buffer elevado;
- baixa precisão geolocalização;
- múltiplos focos térmicos.

Também são utilizados níveis de severidade:
- INFO
- WARNING
- CRITICAL

---

# 📈 Thresholds operacionais

## Temperatura do payload
- NORMAL: até 70°C
- WARNING: 71°C até 85°C
- CRITICAL: acima de 85°C

## Energia disponível
- NORMAL: acima de 60%
- WARNING: entre 30% e 60%
- CRITICAL: abaixo de 30%

## Comunicação
- NORMAL: ONLINE
- CRITICAL: OFFLINE

## Buffer de imagens
- NORMAL: até 70%
- WARNING: 71% até 90%
- CRITICAL: acima de 90%

## Precisão geolocalização
- NORMAL: até 5m
- WARNING: entre 5m e 15m
- CRITICAL: acima de 15m

## Focos térmicos
- NORMAL: até 3
- WARNING: 4 até 10
- CRITICAL: acima de 10

---

# 🤖 Inteligência Artificial

O projeto utiliza o modelo llama3.1 via Ollama Local para:
- interpretar telemetria;
- analisar riscos operacionais;
- recomendar ações corretivas;
- explicar impactos terrestres;
- auxiliar operadores da missão.

---

# 🧠 Justificativa da escolha do modelo llama3.1

O modelo llama3.1 foi escolhido por apresentar:
- boa interpretação contextual;
- respostas estruturadas;
- integração simples com Python;
- funcionamento local via Ollama;
- baixo custo operacional.

A utilização local do modelo também permitiu:
- independência de APIs externas;
- execução offline;
- maior estabilidade durante testes;
- maior controle do ambiente do sistema.

---

# 🧪 Evolução dos prompts

O projeto utiliza versionamento de prompts para demonstrar a evolução da engenharia de prompt aplicada ao sistema.

## system_prompt_v1.md
Versão inicial contendo:
- papel básico da IA;
- contexto da missão;
- estrutura simples de resposta.

## system_prompt_v2.md
Versão intermediária adicionando:
- thresholds operacionais;
- severidade;
- guardrails básicos;
- redução de hallucination.

## system_prompt_v3.md
Versão final contendo:
- schema formal da telemetria;
- anti prompt injection;
- anti role-switch;
- anti-hallucination;
- proteção contra telemetria maliciosa;
- política de prioridade operacional;
- tratamento de inconsistências;
- restrições de domínio.

O arquivo `system_prompt.md` utiliza a versão final mais robusta do sistema.

---

# 🔐 Segurança e guardrails

O projeto implementa mecanismos de segurança para reduzir:
- prompt injection;
- jailbreak;
- hallucination;
- mudança indevida de contexto;
- sobrescrita de instruções;
- telemetria maliciosa.

O sistema:
- bloqueia assuntos externos;
- detecta comandos maliciosos;
- valida inconsistências;
- restringe domínio operacional;
- ignora instruções embutidas na telemetria;
- impede vazamento de instruções internas.

---

# 🧪 Cenários de teste demonstrados

## 1. Operação normal
Todos os parâmetros dentro da faixa segura.

## 2. Superaquecimento crítico
Temperatura acima do limite operacional.

## 3. Falha de comunicação
Satélite operando sem contato orbital.

## 4. Incêndio ambiental
Múltiplos focos térmicos detectados.

## 5. Falha crítica geral
Combinação simultânea de múltiplos alertas.

## 6. Prompt Injection
Tentativas de alterar comportamento da IA foram bloqueadas.

## 7. Role Switching
Tentativas de transformar a IA em chatbot casual foram bloqueadas.

## 8. Telemetria maliciosa
Instruções escondidas em payloads foram detectadas e ignoradas.

---

# 🌎 Proposta de valor / modelo de negócio

## 1. Qual problema terrestre esta missão resolve?

O projeto auxilia no monitoramento ambiental e na detecção rápida de incêndios florestais através da análise automatizada de telemetria espacial.

A missão EnviroSat permite identificar focos térmicos, falhas operacionais e riscos ambientais continuamente.

---

## 2. Quem paga pela solução?

A solução pode operar em modelo híbrido entre setor público e privado.

### Setor público
- INPE
- IBAMA
- Defesa Civil
- órgãos ambientais

### Setor privado
- agronegócio
- monitoramento ambiental
- seguradoras
- pesquisa climática

---

## 3. Métrica de impacto

Se o satélite operar de forma saudável durante 1 ano, a missão poderá auxiliar no monitoramento contínuo de mais de 50 mil hectares ambientais e reduzir significativamente o tempo de resposta em incêndios florestais.

---

## 4. Modelo de negócio

O modelo proposto utiliza:
- monitoramento como serviço;
- assinatura de dados ambientais;
- análise orbital inteligente via IA;
- plataforma SaaS.

---

# 📸 Demonstração do sistema

## Status crítico da missão

![Status crítico](assets/screenshot_status.png)

---

## Análise contextual da IA

![Análise IA](assets/screenshot_alerta.png)

---

## Teste de guardrails

![Guardrails](assets/screenshot_guardrails.png)

---

# 🧠 System Prompt

O system prompt utilizado está em:

```txt
prompts/system_prompt.md
```

O sistema utiliza:
- thresholds operacionais;
- schema formal;
- severidade operacional;
- anti-hallucination;
- anti prompt injection;
- política de prioridade;
- validação contextual.

---

# ⚠️ Limitações conhecidas

- O sistema utiliza dados simulados.
- Não existe conexão com satélites reais.
- Não há persistência em banco de dados.
- A aplicação funciona exclusivamente via terminal.
- O sistema não possui histórico persistente de telemetria.

---

# 🎬 Vídeo de demonstração

🎥 https://www.youtube.com/watch?v=SEU_VIDEO

> Vídeo configurado como “Não listado”.

---

# 📌 Comandos disponíveis

| Comando | Função |
|---|---|
| `/help` | Lista comandos |
| `/status` | Exibe telemetria |
| `/novo` | Gera novo cenário |
| `/about` | Informações do projeto |
| `/clear` | Limpa terminal |
| `/exit` | Encerra sistema |

---

# 🛰️ Exemplo de uso

```txt
❯ /status

🌡️ Temperatura: 91°C
⚡ Energia: 30%
📡 Comunicação: ONLINE
🗂️ Buffer de imagens: 82%
📍 Precisão geolocalização: 7.14 m
🔥 Focos térmicos: 11

⚠️ ALERTAS:
- ALERTA CRÍTICO: superaquecimento do payload.
- WARNING: energia abaixo do ideal.
- WARNING: buffer de imagens elevado.
- WARNING: precisão geolocalização moderada.
- ALERTA AMBIENTAL: múltiplos focos térmicos detectados.
```

---

# 📚 Disciplina

Global Solution 2026.1 — FIAP  
Prompt Engineering and AI