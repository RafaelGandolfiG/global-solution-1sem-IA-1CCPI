# 🚀 Mission Control AI — EnviroSat Guardian

Sistema inteligente de monitoramento espacial com IA generativa para análise de telemetria ambiental da missão EnviroSat.

---

# 👨‍💻 Integrantes

- Rafael Gandolfi — RM: 569036 — Turma: 1CCPI
- Guilherme Miranda — RM: 573107 — Turma: 1CCPI
- Carlos Eduardo — RM: 572949 — Turma: 1CCPI

---

# 🌳 O que o projeto faz

O Mission Control AI é uma plataforma de monitoramento espacial desenvolvida em Python para simular operações de um satélite ambiental da trilha EnviroSat.

O sistema coleta dados simulados de telemetria, identifica situações críticas automaticamente e utiliza Inteligência Artificial com o modelo llama3.1 via Ollama para interpretar riscos operacionais da missão.

A IA é capaz de:
- analisar falhas críticas
- explicar impactos terrestres
- recomendar ações operacionais
- auxiliar operadores em tempo real

---

# 🛰️ Persona atendida

O sistema foi desenvolvido para auxiliar operadores espaciais e engenheiros responsáveis pelo monitoramento de satélites ambientais.

A solução também pode apoiar equipes de monitoramento climático e órgãos ambientais responsáveis pela identificação de incêndios florestais e riscos ambientais.

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

Crie um arquivo `.env` na raiz do projeto:

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

✅ Monitoramento ambiental da missão

✅ Alertas automáticos

✅ Integração com IA generativa

✅ Interface CLI interativa

✅ Geração dinâmica de cenários

✅ Análise contextualizada por IA

✅ Recomendações operacionais

✅ Banner ASCII personalizado

✅ Guardrails contra prompt injection

✅ Validação operacional da telemetria

---

# 📊 Telemetria monitorada

O sistema monitora:

- temperatura do payload
- energia disponível
- comunicação orbital
- buffer de imagens
- precisão geolocalização
- focos térmicos

---

# 🚨 Sistema de alertas

O sistema identifica automaticamente:

- superaquecimento
- perda de comunicação
- energia crítica
- buffer elevado
- múltiplos focos térmicos

O sistema também utiliza níveis de severidade:
- INFO
- WARNING
- CRITICAL

---

# 🤖 Inteligência Artificial

O projeto utiliza o modelo llama3.1 via Ollama Local para:

- interpretar os dados da missão
- analisar riscos operacionais
- gerar respostas contextualizadas
- recomendar ações corretivas
- explicar impactos terrestres

---

## Justificativa da escolha do modelo llama3.1

O modelo llama3.1 foi escolhido por oferecer boa capacidade de interpretação contextual, geração de respostas estruturadas e integração simples com o Ollama Local.

A utilização do llama3.1 permitiu executar o sistema localmente sem dependência de APIs pagas externas, facilitando o desenvolvimento, testes e demonstrações do projeto.

Além disso, o modelo apresentou desempenho satisfatório na análise de telemetria espacial, interpretação de alertas críticos e geração de recomendações operacionais contextualizadas.

Outro fator importante foi a facilidade de integração com Python através da biblioteca Ollama, permitindo comunicação direta entre o sistema de monitoramento e a IA generativa.

---

# 🧪 Evolução dos prompts

O projeto utiliza versionamento de prompts para demonstrar a evolução da engenharia de prompt aplicada ao sistema.

## system_prompt_v1.md
Versão inicial contendo:
- papel básico da IA
- contexto da missão
- estrutura de resposta

## system_prompt_v2.md
Versão intermediária adicionando:
- thresholds operacionais
- níveis de severidade
- guardrails básicos
- redução de hallucination

## system_prompt_v3.md
Versão final contendo:
- schema formal da telemetria
- anti prompt injection
- proteção contra telemetria maliciosa
- política de prioridade operacional
- tratamento de inconsistências
- regras anti-hallucination
- restrições de domínio

O arquivo `system_prompt.md` utiliza a versão final mais robusta do sistema.

---

# 🔐 Segurança e guardrails

O projeto implementa mecanismos de segurança para reduzir:
- prompt injection
- hallucination
- mudança indevida de contexto
- telemetria maliciosa
- sobrescrita de regras operacionais

O sistema:
- bloqueia assuntos fora da missão
- ignora instruções maliciosas
- valida inconsistências na telemetria
- impede respostas fora do domínio EnviroSat

---

# 🧪 Cenários de teste demonstrados

## 1. Operação normal
Todos os parâmetros dentro do nível seguro.

## 2. Superaquecimento crítico
Temperatura acima do limite operacional.

## 3. Falha de comunicação
Satélite operando sem contato com a estação terrestre.

## 4. Incêndio ambiental
Múltiplos focos térmicos detectados.

## 5. Falha crítica geral
Combinação simultânea de múltiplos alertas críticos.

## 6. Prompt Injection
Tentativas de alterar o comportamento da IA foram bloqueadas pelos guardrails.

---

# 🌎 Proposta de valor / modelo de negócio

## 1. Qual problema terrestre esta missão resolve?

O projeto auxilia no monitoramento ambiental e na detecção rápida de incêndios florestais através da análise automatizada de telemetria espacial.

A missão EnviroSat permite identificar focos térmicos, falhas operacionais e riscos ambientais de forma contínua, contribuindo para redução de danos ambientais e resposta mais rápida de equipes responsáveis pelo combate a incêndios.

Além disso, o sistema pode apoiar operações de preservação ambiental e monitoramento climático em áreas críticas.

---

## 2. Quem paga pela solução?

A solução pode operar em modelo híbrido entre setor público e privado.

### Setor público
- INPE
- IBAMA
- Defesa Civil
- órgãos ambientais estaduais

### Setor privado
- empresas de monitoramento ambiental
- agronegócio
- seguradoras ambientais
- centros privados de pesquisa climática

---

## 3. Métrica de impacto

Se o satélite operar de forma saudável durante 1 ano, a missão poderá auxiliar no monitoramento contínuo de mais de 50 mil hectares de áreas ambientais e reduzir significativamente o tempo de resposta em incêndios florestais.

A solução pode contribuir para:
- detecção antecipada de focos de incêndio
- redução de danos ambientais
- melhoria da tomada de decisão operacional
- monitoramento ambiental contínuo em regiões críticas

---

## 4. Modelo de negócio

O modelo proposto é baseado em:
- monitoramento como serviço
- assinatura de dados ambientais
- integração com plataformas ambientais
- análise orbital inteligente via IA

A solução pode operar no formato SaaS (Software as a Service), fornecendo dados ambientais, alertas automatizados e análises inteligentes para órgãos públicos e empresas privadas.

---

# 📸 Demonstração do sistema

## Status crítico da missão

![Status crítico da missão](assets/screenshot_status.png)

---

## Análise da IA sobre a missão

![Análise da IA](assets/screenshot_alerta.png)

---

## Teste de guardrails

![Guardrails contra prompt injection](assets/screenshot_guardrails.png)

---

# 🧠 System Prompt

O system prompt utilizado está localizado em:

```txt
prompts/system_prompt.md
```

O sistema utiliza:
- thresholds operacionais
- schema formal de telemetria
- anti-hallucination
- proteção contra prompt injection
- validação contextual
- política de prioridade operacional

---

# ⚠️ Limitações conhecidas

- O sistema utiliza dados simulados.
- Não existe conexão com satélites reais.
- O projeto não utiliza banco de dados.
- A aplicação opera exclusivamente via terminal.
- As respostas da IA podem variar dependendo do contexto da missão.
- O sistema não realiza persistência histórica da telemetria.

---

# 🎬 Vídeo de demonstração

🎥 https://www.youtube.com/watch?v=SEU_VIDEO

> Vídeo configurado como "Não listado".

---

# 📌 Comandos disponíveis

| Comando | Função |
|---|---|
| `/help` | Lista comandos disponíveis |
| `/status` | Exibe telemetria atual |
| `/novo` | Gera novo cenário |
| `/about` | Informações do projeto |
| `/clear` | Limpa o terminal |
| `/exit` | Encerra o sistema |

---

# 🛰️ Exemplo de uso

```txt
❯ /status

🌡️ Temperatura: 88°C
⚡ Energia: 14%
📡 Comunicação: OFFLINE
🔥 Focos térmicos: 13

⚠️ ALERTA CRÍTICO:
- superaquecimento do payload
- perda de comunicação
- energia crítica
- múltiplos focos térmicos
```

---

# 📚 Disciplina

Global Solution 2026.1 — FIAP  
Prompt Engineering and AI

---