# 🏗️ SICE — Sistema Inteligente de Controle Energético de Colônias

**Projeto Acadêmico — FIAP**  
Documentação Oficial do Sistema de Gestão Energética para Ambientes Extremos  
**Versão:** 1.0 | **Data:** Maio de 2026 | **Status:** Funcional

---

## 📋 Sumário

1. [Visão Geral](#1-visão-geral)
2. [Características do Sistema](#2-características-do-sistema)
3. [Arquitetura Modular e Equipe](#3-arquitetura-modular-e-equipe)
4. [Estrutura de Diretórios do Projeto](#4-estrutura-de-diretórios-do-projeto)
5. [Requisitos e Instalação](#5-requisitos-e-instalação)
6. [Guia de Uso e Exemplos de Execução](#6-guia-de-uso-e-exemplos-de-execução)
7. [Estruturas de Dados e Complexidade](#7-estruturas-de-dados-e-complexidade)
8. [Algoritmos e Modelos Implementados](#8-algoritmos-e-modelos-implementados)
9. [Motor de Regras de Decisão](#9-motor-de-regras-de-decisão)
10. [Cenário de Teste Padrão](#10-cenário-de-teste-padrão)

---

## 1. 🎯 Visão Geral

O SICE (Sistema Inteligente de Controle Energético de Colônias) é um sistema interativo de simulação e tomada de decisão energética para uma colônia instalada em ambiente hostil.

O sistema monitora o equilíbrio entre geração de energia (solar e eólica), armazenamento em banco de baterias e consumo dos módulos ativos — aplicando um motor de regras para emitir alertas e sugestões operacionais, além de prever a geração futura a partir de modelos de regressão linear ajustados com dados históricos.

O objeto central é a classe `Colonia`, que agrega todos os módulos, sistemas de energia e parâmetros ambientais, servindo como entrada única para todas as funções de análise e decisão.

---

## 2. ⭐ Características do Sistema

- **Menu Interativo Multi-Nível:** Navegação por três áreas funcionais — Configuração, Regras e Previsão — implementada com `match/case` (Python 3.10+).

- **Gestão de Módulos Dinâmica:** O operador cadastra módulos e sistemas de energia em tempo de execução; o estado da colônia é mantido em memória ao longo de toda a sessão através de uma instância única de `Colonia`.

- **Motor de 7 Regras Independentes:** Cada ciclo de análise avalia todas as condições em sequência e acumula as recomendações pertinentes, sem interromper a avaliação ao encontrar a primeira ocorrência. Ao final, uma recomendação de `INFORMAÇÃO` com o plano de módulos por prioridade é sempre gerada.

- **Previsão por Regressão Linear:** Modelos ajustados com `numpy.polyfit` sobre séries históricas fornecem previsão pontual de geração eólica (entrada: m/s) e solar (entrada: % de radiação).

- **Visualização Integrada:** Quatro gráficos matplotlib disponíveis no menu de Previsão: histórico eólico, histórico solar, previsão eólica com ponto anotado e previsão solar com ponto anotado.

- **Análise de Suficiência:** Compara automaticamente a energia prevista com o consumo atual da colônia e classifica o resultado como `ALERTA` (insuficiente) ou `SUGESTÃO` (suficiente).

---

## 3. 🏗️ Arquitetura Modular e Equipe

O projeto separa responsabilidades em cinco frentes coordenadas pelo programa principal:

```text
┌──────────────────────────────────────────────────────────────────────────┐
│                          PROGRAMA PRINCIPAL                              │
│                              (main.py)                                   │
│                             (Bruno)                                      │
│  - Menu interativo (match/case multi-nível)                              │
│  - Instância única de Colonia compartilhada entre menus                  │
│  - Integração entre os pacotes funcionais                                │
│  - Tratamento de entradas e validações                                   │
└──────┬─────────────────────┬──────────────────┬──────────────┬──────────┘
       │                     │                  │              │
┌──────▼──────────┐  ┌───────▼──────┐  ┌────────▼───────┐  ┌──▼──────────┐
│     MÓDULOS     │  │    REGRAS    │  │    PREVISÃO    │  │ DOCUMENTAÇÃO│
│    (Aelton)     │  │  (Michelly)  │  │    (Victor)    │  │   (Maria)   │
│                 │  │              │  │                │  │             │
│ • Classe Modulo │  │ • 7 Regras   │  │ • Dados        │  │ • README    │
│ • Hierarquia    │  │   de decisão │  │   históricos   │  │ • Diagramas │
│   Sistema/Solar/│  │ • ALERTAS,   │  │ • Regressão    │  │ • Guias de  │
│   Eolico/Reserva│  │   SUGESTÕES  │  │   linear       │  │   uso       │
│ • Classe Colonia│  │  e INFORMAÇÃO│  │ • Gráficos     │  │             │
│   (contexto)    │  │ • Prioridades│  │   matplotlib   │  │             │
│                 │  │   1, 2 e 3   │  │ • Análise de   │  │             │
│                 │  │              │  │   suficiência  │  │             │
└─────────────────┘  └──────────────┘  └────────────────┘  └─────────────┘
```

### Atribuições Explícitas

**AELTON** — Modelagem e Estruturas de Dados  
`src/modules/modulos.py` — Classes `Modulo`, `Sistema` e subclasses (`SistemaSolar`, `SistemaEolico`, `SistemaReserva`), além da classe `Colonia` com todos os métodos de consulta de estado.

**MICHELLY** — Motor de Regras  
`src/rules/regras.py` — Função `verificar_colonia()` com 7 regras independentes de avaliação do estado energético da colônia.

**VICTOR** — Previsão e Análise Energética  
`src/forecast/previsao.py` — Históricos, regressão linear, previsão pontual e geração de quatro tipos de gráfico.  
`src/forecast/analise_energetica.py` — Análise de suficiência eólica e solar em relação ao consumo atual.

**BRUNO** — Programa Principal  
`src/main.py` — Menu interativo multi-nível, integração entre os pacotes, instância única de `Colonia`, validações e tratamento de entradas.

**MARIA** — Documentação  
`README.md` — Documentação oficial do projeto, diagramas de arquitetura, guias de uso e cenários de teste.

---

## 4. 📁 Estrutura de Diretórios do Projeto

```text
intelligent-colony-system-main/
│
├── src/                              # Código-fonte principal
│   ├── main.py                       # Programa principal — menu interativo (Bruno)
│   │
│   ├── modules/                      # Camada de Modelagem (Aelton)
│   │   ├── __init__.py
│   │   └── modulos.py                # Classes Modulo, Sistema e Colonia
│   │
│   ├── rules/                        # Motor de Regras (Michelly)
│   │   ├── __init__.py
│   │   └── regras.py                 # Função verificar_colonia() — 7 regras
│   │
│   └── forecast/                     # Previsão Energética (Victor)
│       ├── __init__.py
│       ├── previsao.py               # Regressão linear e gráficos
│       └── analise_energetica.py     # Análise solar e eólica vs consumo
│
├── README.md                         # Documentação oficial (Maria)
└── .gitignore
```

---

## 5. 📦 Requisitos e Instalação

- **Ambiente Operacional:** Windows, macOS ou Linux
- **Interpretador:** Python 3.10 ou superior (obrigatório para `match/case`)
- **Dependências Externas:** `matplotlib` e `numpy`

### Passos para Configuração

**1. Clone o repositório do projeto:**

```bash
git clone https://github.com/DevLounge-FIAP/intelligent-colony-system.git
cd intelligent-colony-system-main
```

**2. Crie e ative o ambiente virtual (recomendado):**

```bash
# Windows:
python -m venv venv
.\venv\Scripts\Activate.ps1

# macOS/Linux:
python3 -m venv venv
source venv/bin/activate
```

**3. Instale as dependências:**

```bash
pip install -r requirements.txt
```

---

## 6. 💻 Guia de Uso e Exemplos de Execução

Para iniciar o sistema interativo principal:

```bash
cd src
python main.py
```

O terminal exibirá o menu principal:

```text
===============
Menu Principal
===============
[1] - Configuração (Módulos, Sistemas e Telemetria)
[2] - Regras
[3] - Previsão
[0] - Sair
```

### Fluxo Recomendado de Uso

**Passo 1 — Cadastrar a colônia via menu `[1]`:**

- `[1]` Cadastrar módulos (ID, tipo, função, criticidade 1–5, consumo/h)
- `[2]` Cadastrar sistemas de energia (Solar máx 30, Eólico máx 20, Reserva máx 50)
- `[3]` Informar velocidade do vento (0–30, inteiro) e radiação solar (0–100, inteiro)
- `[4]` Visualizar módulos cadastrados
- `[5]` Listar sistemas cadastrados

**Passo 2 — Analisar regras via menu `[2]`:**

> Pré-requisitos: pelo menos 2 módulos, 1 sistema e telemetria configurada.

- `[1]` Executa `verificar_colonia()` e imprime recomendações com tipo, prioridade e plano de módulos ativos e desligados por prioridade.

**Passo 3 — Obter previsões via menu `[3]`:**

> Pré-requisitos: pelo menos 2 módulos, 1 sistema e telemetria configurada.

- `[1]` Usa telemetria atual de vento → retorna kWh previstos, executa análise de suficiência energética eólica e abre gráfico.
- `[2]` Usa telemetria atual de radiação → retorna kWh previstos, executa análise de suficiência energética solar e abre gráfico.
- `[3]` Exibe gráfico histórico eólico completo.
- `[4]` Exibe gráfico histórico solar completo.

### Exemplos de Saída

**Análise de Regras — Vento zerado e radiação ativa:**

```text
----------------------------------------
| ANÁLISES                             |
----------------------------------------
| [3] SUGESTÃO: Energia eólica não ... |
|     está sendo produzida. Utilize    |
|     sistema de energia solar.        |
| [1] ALERTA: Consumo (90.00 kWh)      |
|     maior que energia disponível     |
|     (30.00 kWh).                     |
----------------------------------------
```

**Previsão Eólica — Vento de 15 m/s:**

```text
Velocidade do Vento Atual: 15 m/s
Previsão de geração eólica: 9.90 kWh
[Gráfico matplotlib exibido em janela separada]
```

**Previsão Solar — Radiação de 70%:**

```text
Radiação Solar Atual: 70%
Previsão de geração solar: 21.00 kWh
[Gráfico matplotlib exibido em janela separada]
```

---

## 7. 🧱 Estruturas de Dados e Complexidade

O sistema emprega quatro estruturas de dados com finalidades distintas:

**1. Objeto `Colonia` (Contexto Central)**  
Agrega em tempo de execução todas as listas de módulos e sistemas, além das variáveis ambientais de vento e radiação solar. É o único parâmetro de entrada das funções de análise e regras. Centraliza o estado da simulação em um único objeto, facilitando a passagem de contexto entre os pacotes.

**2. Lista de Módulos (`colonia.modulos`)**  
Armazena os objetos `Modulo` cadastrados pelo operador. Operações: `append()` em O(1) para inserção; iteração O(n) para calcular consumo total e filtrar módulos por status ou criticidade.

**3. Lista de Sistemas (`colonia.sistemas`)**  
Armazena os objetos de geração/armazenamento (Solar, Eólico, Reserva). Permite somar `geracao_atual` e `capacidade_max` em O(n).

**4. Lista de Recomendações (retorno de `verificar_colonia`)**  
Acumula dicionários com as chaves `tipo`, `mensagem`, `prioridade` e `origem`. Cresce dinamicamente conforme as regras são ativadas. Se permanecer vazia após a varredura, a Regra 7 insere a mensagem de sistema estável. A última entrada sempre contém o plano de módulos por prioridade (tipo `INFORMAÇÃO`, prioridade 2), com as chaves adicionais: `modulos_ativos`, `modulos_desligados` e `energia_restante_modulos`.

### Métodos de Consulta da Classe `Colonia`

```text
+---------------------------+----------+----------------------------------+
| Método                    | Retorno  | Descrição                        |
+---------------------------+----------+----------------------------------+
| energia_disponivel_total()| int      | Soma de geracao_atual de todos   |
|                           |          | os sistemas (inclui reserva)     |
| capacidade_total()        | int      | Soma de capacidade_max de todos  |
|                           |          | os sistemas cadastrados          |
| nivel_energia_percentual()| float    | (disponível / capacidade) × 100  |
| consumo_total()           | int      | Soma do consumo dos módulos com  |
|                           |          | status = True (ligados)          |
| modulos_ligados()         | list     | Módulos com status = True        |
| modulos_desligaveis()     | list     | Módulos ligados com criticidade  |
|                           |          | menor que 4                      |
| modulos_por_prioridade()  | tuple    | (ativos, desligados, energia     |
|                           |          | restante) — estratégia first-fit |
|                           |          | por criticidade decrescente      |
+---------------------------+----------+----------------------------------+
```

---

## 8. 🔧 Algoritmos e Modelos Implementados

### 1. Regressão Linear — Previsão de Geração de Energia

- **Funções:** `regressao_eolica()` e `regressao_solar()`
- **Biblioteca:** `numpy.polyfit` — ajuste por mínimos quadrados (grau 1)
- **Complexidade:** O(n) para ajuste; O(1) para previsão pontual

O ajuste determina os coeficientes `a` (inclinação) e `b` (intercepto) da equação `y = a·x + b` a partir das séries históricas fixas do sistema. Os coeficientes são reutilizados para prever a geração a partir de qualquer entrada de vento ou radiação informada.

**Dados históricos de treinamento — Eólico:**

```text
+---------------------+---------------------+
| Velocidade (m/s)    | Energia gerada (kWh)|
+---------------------+---------------------+
|        28           |        18,48        |
|        12           |         7,92        |
|         8           |         5,28        |
|        16           |        10,56        |
|        20           |        13,20        |
|        18           |        11,88        |
+---------------------+---------------------+
```

Modelo resultante: `y ≈ 0,66 · vento`

**Dados históricos de treinamento — Solar:**

```text
+---------------------+---------------------+
| Radiação (%)        | Energia gerada (kWh)|
+---------------------+---------------------+
|        90           |        27,00        |
|        70           |        21,00        |
|        50           |        15,00        |
|        80           |        24,00        |
|        30           |         9,00        |
|        60           |        18,00        |
+---------------------+---------------------+
```

Modelo resultante: `y = 0,30 · radiação`

### 2. Análise de Suficiência Energética

- **Funções:** `analise_energetica_eolica(estado)` e `analise_energetica_solar(estado)`
- **Complexidade:** O(1) — comparação direta entre dois valores

Compara a energia prevista pelo modelo (usando vento ou radiação atuais da colônia) com o consumo total em tempo real. Retorna `ALERTA` (prioridade 1) se a geração for inferior ao consumo, ou `SUGESTÃO` (prioridade 3) se for suficiente.

### 3. Plano de Módulos por Prioridade — First-fit Decrescente

- **Função:** `modulos_por_prioridade()` — classe `Colonia`
- **Complexidade:** O(n log n) para ordenação; O(n) para alocação

Ordena os módulos por criticidade decrescente e aloca energia disponível sequencialmente. O primeiro módulo que não couber encerra a alocação — todos os subsequentes são marcados como desligados, garantindo que módulos de maior criticidade tenham prioridade absoluta.

---

## 9. 📋 Motor de Regras de Decisão

A função `verificar_colonia(estado: Colonia)` avalia as condições abaixo em sequência. Todas são verificadas a cada chamada, e as recomendações ativadas são acumuladas em uma lista de dicionários retornada ao programa principal.

**Estrutura de cada recomendação retornada:**

| Campo | Valores possíveis |
|---|---|
| `tipo` | `"ALERTA"`, `"SUGESTÃO"` ou `"INFORMAÇÃO"` |
| `mensagem` | Texto descritivo para o operador |
| `prioridade` | `1` (crítica), `2` (importante) ou `3` (sugestão) |
| `origem` | Identificador do módulo que gerou a recomendação |

**Tabela de Regras:**

```text
+----+---------------------------------------------+----------+------------+
| #  | Condição de Ativação                        | Tipo     | Prioridade |
+----+---------------------------------------------+----------+------------+
|  1 | vento > 0 e radiação = 0                    | SUGESTÃO |     3      |
|    | → Usar energia eólica; solar indisponível   |          |            |
+----+---------------------------------------------+----------+------------+
|  1 | radiação > 0 e vento = 0 (elif)             | SUGESTÃO |     3      |
|    | → Usar energia solar; eólica indisponível   |          |            |
+----+---------------------------------------------+----------+------------+
|  1 | vento = 0 e radiação = 0 (elif)             | SUGESTÃO |     3      |
|    | → Operar apenas com reserva de baterias     |          |            |
+----+---------------------------------------------+----------+------------+
|  2 | energia > 50, consumo < 30, reserva < 49%   | SUGESTÃO |     3      |
|    | → Armazenar excedente na reserva            |          |            |
+----+---------------------------------------------+----------+------------+
|  3 | energia > 99 e reserva > 49%                | SUGESTÃO |     3      |
|    | → Parar produção solar e eólica             |          |            |
+----+---------------------------------------------+----------+------------+
|  4 | energia ≤ 30 e consumo ≥ 50% da disponível  | ALERTA   |     1      |
|    | → Risco de apagão                           |          |            |
+----+---------------------------------------------+----------+------------+
|  5 | radiação < 10%, vento < 10, energia% < 50%  | SUGESTÃO |     3      |
|    | → Atenção; desligar módulos de baixa crit.  |          |            |
+----+---------------------------------------------+----------+------------+
|  6 | energia > 50 e há módulos desligados        | SUGESTÃO |     3      |
|    | → Energia normalizada, verificar religação  |          |            |
+----+---------------------------------------------+----------+------------+
|  7 | Nenhuma regra anterior acionada             | SUGESTÃO |     3      |
|    | → Sistema dentro dos parâmetros normais     |          |            |
+----+---------------------------------------------+----------+------------+
| +1 | Sempre: plano de módulos por prioridade     |INFORMAÇÃO|     2      |
+----+---------------------------------------------+----------+------------+
```

> **Nota:** As três condições da Regra 1 são implementadas como `if/elif`, portanto apenas uma delas dispara por execução. As demais regras são `if` independentes e podem se acumular na mesma análise.

---

## 10. 🧩 Cenário de Teste Padrão

Para validação manual, cadastre o seguinte cenário via menu `[1]`:

**Módulos:**

```text
+--------+--------------+-------------+----------+
|   ID   |     Tipo     | Criticidade | Consumo/h|
+--------+--------------+-------------+----------+
| MED-01 | Médico       |      5      |    10    |
| HAB-02 | Habitação    |      1      |    20    |
| LAB-03 | Laboratório  |      3      |    30    |
| LOG-04 | Logístico    |      2      |    30    |
+--------+--------------+-------------+----------+
```

> Consumo total (todos ligados): **90 kWh/h**

**Sistemas:**

```text
+---------+-----------+------------------+---------------+
|  Nome   |   Tipo    | Capacidade Máx.  | Geração Atual |
+---------+-----------+------------------+---------------+
| Painel  | Solar     |     30 kWh       |    10 kWh     |
| Torre   | Eólico    |     20 kWh       |     0 kWh     |
| Bateria | Reserva   |     50 kWh       |    20 kWh     |
+---------+-----------+------------------+---------------+
```

> Energia disponível total: **30 kWh** | Capacidade total: **100 kWh**

**Parâmetros ambientais:**

- Velocidade do vento: `0 m/s` (sem geração eólica)
- Radiação solar: `40%` (escala de 0 a 100)

**Resultado esperado de `verificar_colonia()`:**

- Regra 1 (elif): vento = 0 com radiação ativa → `SUGESTÃO` (prioridade 3)
- Regra 4: consumo (90) ≥ 50% de energia disponível (30) → `ALERTA` (prioridade 1)
- +1: Plano de módulos por prioridade → `INFORMAÇÃO` (prioridade 2)

**Resultado esperado de `analise_energetica_eolica` (vento = 0 m/s):**

- Energia prevista: ~0 kWh < consumo 90 → `ALERTA` (prioridade 1)

**Resultado esperado de `analise_energetica_solar` (radiação = 40%):**

- Energia prevista: 12,00 kWh < consumo 90 → `ALERTA` (prioridade 1)

---

*Fim da Documentação Oficial — Equipe DevLounge-FIAP (2026)*