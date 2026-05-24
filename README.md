```markdown
# 🏗️ SICE - SISTEMA INTELIGENTE DE CONTROLE ENERGÉTICO DE COLÔNIAS
**Projeto Acadêmico - FIAP**
Documentação Oficial do Sistema de Gestão Energética para Ambientes Extremos
**Versão:** 1.0 | **Data:** Maio de 2026
**Status:** Funcional

---

## 📋 SUMÁRIO
1. Visão Geral
2. Características do Sistema
3. Arquitetura Modular e Equipe
4. Estrutura de Diretórios do Projeto
5. Requisitos e Instalação
6. Guia de Uso e Exemplos de Execução
7. Estruturas de Dados e Complexidade
8. Algoritmos e Modelos Implementados
9. Motor de Regras de Decisão
10. Cenário de Teste Padrão
11. Scripts de Teste Manual

---

## 1. 🎯 VISÃO GERAL
O SICE (Sistema Inteligente de Controle Energético de Colônias) é um sistema interativo de simulação e tomada de decisão energética para uma colônia instalada em ambiente hostil.

O sistema monitora em tempo real o equilíbrio entre geração de energia (solar e eólica), armazenamento em banco de baterias e consumo dos módulos ativos — aplicando um motor de regras para emitir alertas e sugestões operacionais, além de prever a geração futura a partir de modelos de regressão linear treinados com dados históricos.

O objeto central é a classe `Colonia`, que agrega todos os módulos, sistemas de energia e parâmetros ambientais, servindo como entrada única para todas as funções de análise e decisão.

## 2. ⭐ CARACTERÍSTICAS DO SISTEMA
* **Menu Interativo Multi-Nível:** Navegação por três áreas funcionais — Módulos, Regras e Previsão — implementada com `match/case` (Python 3.10+).
* **Gestão de Módulos Dinâmica:** O operador cadastra módulos e sistemas de energia em tempo de execução; o estado da colônia é mantido em memória ao longo de toda a sessão através de uma instância única de `Colonia`.
* **Motor de 7 Regras Independentes:** Cada ciclo de análise avalia todas as condições em sequência e acumula as recomendações pertinentes, sem interromper a avaliação ao encontrar a primeira ocorrência.
* **Previsão por Regressão Linear:** Modelos ajustados com `numpy.polyfit` sobre séries históricas fornecem previsão pontual de geração eólica (entrada: m/s) e solar (entrada: % de radiação).
* **Visualização Integrada:** Gráficos `matplotlib` exibem histórico de dados, reta de regressão ajustada e ponto de previsão anotado. O menu de módulos exibe gráficos compostos de criticidade (barras) e status ligado/desligado (pizza) lado a lado.
* **Análise de Suficiência:** Compara automaticamente a energia prevista pelo modelo com o consumo atual da colônia e classifica o resultado como ALERTA (insuficiente) ou SUGESTÃO (suficiente).

## 3. 🏗️ ARQUITETURA MODULAR E EQUIPE
O projeto separa responsabilidades em três pacotes independentes coordenados pelo programa principal:

```text
┌──────────────────────────────────────────────────────────────────┐
│                      PROGRAMA PRINCIPAL                          │
│                         (main.py)                                │
│  - Menu interativo (match/case multi-nível)                      │
│  - Instância única de Colonia compartilhada entre menus          │
│  - Integração entre os três pacotes funcionais                   │
└──────────────┬────────────────────┬───────────────┬─────────────┘
               │                    │               │
    ┌──────────▼──────────┐  ┌──────▼──────┐  ┌────▼────────────┐
    │      MÓDULOS        │  │    REGRAS   │  │    PREVISÃO     │
    │     (Aelton)        │  │  (Michelly) │  │    (Bruno)      │
    │                     │  │             │  │                 │
    │ • Classe Modulo     │  │ • 7 Regras  │  │ • Dados         │
    │ • Hierarquia        │  │   de decisão│  │   históricos    │
    │   Sistema/Solar/    │  │ • ALERTAS e │  │ • Regressão     │
    │   Eolico/Reserva    │  │   SUGESTÕES │  │   linear        │
    │ • Classe Colonia    │  │ • Prioridade│  │ • Gráficos      │
    │   (contexto)        │  │   1 e 3     │  │   matplotlib    │
    └─────────────────────┘  └─────────────┘  └─────────────────┘

```

**ATRIBUIÇÕES EXPLÍCITAS:**

* **AELTON (Modelagem e Estruturas de Dados):**
* `src/modules/modulos.py`: Classes `Modulo`, `Sistema` e suas subclasses, além da classe `Colonia` com todos os métodos de consulta de estado.


* **MICHELLY (Motor de Regras):**
* `src/rules/regras.py`: Função `verificar_colonia()` com 7 regras independentes de avaliação do estado energético da colônia.
* `src/rules/teste_regras.py`: Cenário de validação manual das regras.


* **BRUNO (Previsão e Análise Energética):**
* `src/forecast/previsao.py`: Históricos, regressão linear, previsão pontual e geração de quatro tipos de gráfico.
* `src/forecast/analise_energetica.py`: Análise de suficiência eólica e solar em relação ao consumo atual.
* `src/forecast/teste_previsao.py`: Cenário de validação manual.



## 4. 📁 ESTRUTURA DE DIRETÓRIOS DO PROJETO

```text
intelligent-colony-system-main/
│
├── src/                              # Código-fonte principal
│   ├── main.py                       # Programa principal — menu interativo
│   │
│   ├── modules/                      # Camada de Modelagem (Aelton)
│   │   ├── __init__.py
│   │   └── modulos.py                # Classes Modulo, Sistema e Colonia
│   │
│   ├── rules/                        # Motor de Regras (Michelly)
│   │   ├── __init__.py
│   │   ├── regras.py                 # Função verificar_colonia() — 7 regras
│   │   └── teste_regras.py           # Cenário de teste manual das regras
│   │
│   └── forecast/                     # Previsão Energética (Bruno)
│       ├── __init__.py
│       ├── previsao.py               # Regressão linear e gráficos
│       ├── analise_energetica.py     # Análise solar e eólica vs consumo
│       └── teste_previsao.py         # Cenário de teste manual da previsão
│
└── .gitignore

```

## 5. 📦 REQUISITOS E INSTALAÇÃO

* **Ambiente Operacional:** Windows, macOS ou Linux.
* **Interpretador:** Python 3.10 ou superior (obrigatório para `match/case`).
* **Dependências Externas:** `matplotlib` e `numpy`.

**Passos para Configuração:**

1. Clone o repositório do projeto:

```bash
git clone [https://github.com/DevLounge-FIAP/intelligent-colony-system.git](https://github.com/DevLounge-FIAP/intelligent-colony-system.git)
cd intelligent-colony-system-main

```

2. Crie e ative o ambiente virtual (recomendado):

```bash
# Windows:
python -m venv venv
.\venv\Scripts\Activate.ps1

# macOS/Linux:
python3 -m venv venv
source venv/bin/activate

```

3. Instale as dependências:

```bash
pip install matplotlib numpy

```

## 6. 💻 GUIA DE USO E EXEMPLOS DE EXECUÇÃO

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
[1] - Modulos
[2] - Regras
[3] - Previsão
[0] - Sair

```

**Fluxo Recomendado de Uso:**

* **Passo 1 — Cadastrar a colônia via menu [1]:**
* Opção [1]: Cadastrar módulos (ID, tipo, função, criticidade, consumo)
* Opção [2]: Cadastrar sistemas de energia (Solar, Eólico ou Reserva)
* Opção [3]: Informar velocidade do vento (km/h) e radiação solar (W/m²)
* Opção [4]: Visualizar módulos com gráficos de criticidade e status
* Opção [5]: Listar sistemas cadastrados


* **Passo 2 — Analisar regras via menu [2]:**
* Opção [1]: Executa `verificar_colonia()` e imprime todas as recomendações geradas, com tipo e prioridade de cada uma.


* **Passo 3 — Obter previsões via menu [3]:**
* Opção [1]: Informa velocidade do vento → retorna kWh previstos e abre gráfico da reta de regressão eólica com ponto marcado.
* Opção [2]: Informa nível de radiação → retorna kWh previstos e abre gráfico da reta de regressão solar com ponto marcado.
* Opção [3]: Exibe gráfico histórico eólico completo.
* Opção [4]: Exibe gráfico histórico solar completo.



**Exemplo — Análise de Regras com Vento Zerado e Radiação Ativa:**

```text
[Saída de verificar_colonia()]

----------------------------------------
| ANÁLISES                             |
----------------------------------------
| [3] SUGESTÃO: Energia eólica não ... |
|     está sendo produzida. Utilize    |
|     sistema de energia solar.        |
| [1] ALERTA: Consumo (60) maior que   |
|     energia disponível (30). Risco   |
|     de apagão. Desligue: HAB-02,     |
|     LAB-03, LOG-04                   |
----------------------------------------

```

**Exemplo — Previsão Eólica para Vento de 15 m/s:**

```text
Velocidade do vento (0 a 30 m/s): 15
Previsão de energia eólica: 9.90 kWh
[Gráfico matplotlib exibido em janela separada]

```

**Exemplo — Previsão Solar para Radiação de 70%:**

```text
Radiação solar (0 a 100%): 70
Previsão de energia solar: 21.00 kWh
[Gráfico matplotlib exibido em janela separada]

```

## 7. 🧱 ESTRUTURAS DE DADOS E COMPLEXIDADE

O sistema emprega quatro estruturas de dados com finalidades distintas:

1. **Objeto `Colonia` (Contexto Central):**
* **Uso:** Agrega em tempo de execução todas as listas de módulos e sistemas, além das variáveis ambientais de vento e radiação solar. É o único parâmetro de entrada das funções de análise e regras.
* **Vantagem:** Centraliza o estado da simulação em um único objeto, facilitando a passagem de contexto entre os três pacotes.


2. **Lista de Módulos (`colonia.modulos`):**
* **Uso:** Armazena os objetos `Modulo` cadastrados pelo operador.
* **Operações:** `append()` em O(1) para inserção; iteração linear O(n) para calcular consumo total e filtrar módulos por status ou criticidade.


3. **Lista de Sistemas (`colonia.sistemas`):**
* **Uso:** Armazena os objetos de geração/armazenamento (Solar, Eólico, Reserva). Permite somar `geracao_atual` e `capacidade_max` em O(n).


4. **Lista de Recomendações (retorno de `verificar_colonia`):**
* **Uso:** Acumula dicionários com as chaves `tipo`, `mensagem`, `prioridade` e `origem`. Cresce dinamicamente conforme as regras são ativadas; se permanecer vazia após a varredura, a Regra 7 insere a mensagem de sistema estável.



**Métodos de Consulta da Classe Colonia:**

| Método | Retorno | Descrição |
| --- | --- | --- |
| `energia_disponivel_total()` | int | Soma de `geracao_atual` de todos os sistemas (inclui reserva) |
| `capacidade_total()` | int | Soma de `capacidade_max` de todos os sistemas cadastrados |
| `nivel_energia_percentual()` | float | (disponível / capacidade) × 100 |
| `consumo_total()` | int | Soma do consumo dos módulos com status = True (ligados) |
| `modulos_ligados()` | list | Módulos com status = True |
| `modulos_desligaveis()` | list | Módulos ligados com criticidade menor que 4 |

## 8. 🔧 ALGORITMOS E MODELOS IMPLEMENTADOS

**1. Regressão Linear (Previsão de Geração de Energia):**

* **Funções:** `regressao_eolica()` e `regressao_solar()`
* **Biblioteca:** `numpy.polyfit` — ajuste por mínimos quadrados (grau 1)
* **Complexidade:** O(n) para ajuste; O(1) para previsão pontual

O ajuste determina os coeficientes `a` (inclinação) e `b` (intercepto) da equação `y = a·x + b` a partir das séries históricas fixas do sistema. Os coeficientes são reutilizados para prever a geração a partir de qualquer entrada de vento ou radiação informada.

**Dados históricos de treinamento — Eólico:** (Modelo resultante: `y ≈ 0,66 · vento`)

| Velocidade (m/s) | Energia gerada (kWh) |
| --- | --- |
| 28 | 18,48 |
| 12 | 7,92 |
| 8 | 5,28 |
| 16 | 10,56 |
| 20 | 13,20 |
| 18 | 11,88 |

**Dados históricos de treinamento — Solar:** (Modelo resultante: `y = 0,30 · radiação`)

| Radiação (%) | Energia gerada (kWh) |
| --- | --- |
| 90 | 27,00 |
| 70 | 21,00 |
| 50 | 15,00 |
| 80 | 24,00 |
| 30 | 9,00 |
| 60 | 18,00 |

**2. Análise de Suficiência Energética:**

* **Funções:** `analise_energetica_eolica(estado)` e `analise_energetica_solar(estado)`
* **Complexidade:** O(1) — comparação direta entre dois valores

Compara a energia prevista pelo modelo (usando vento ou radiação atuais da colônia) com o consumo total em tempo real. Retorna ALERTA (prioridade 1) se a geração for inferior ao consumo, ou SUGESTÃO (prioridade 3) se for suficiente.

## 9. 📋 MOTOR DE REGRAS DE DECISÃO

A função `verificar_colonia(estado: Colonia)` avalia 7 condições independentes sobre o estado atual da colônia. Todas as regras são verificadas a cada chamada, e as recomendações ativadas são acumuladas em uma lista de dicionários retornada ao programa principal.

**Estrutura de cada recomendação retornada:**

* **tipo:** "ALERTA" ou "SUGESTÃO"
* **mensagem:** Texto descritivo para o operador
* **prioridade:** 1 (crítica) ou 3 (sugestão)
* **origem:** Identificador do módulo que gerou a recomendação

**Tabela de Regras:**

| # | Condição de Ativação | Tipo | Prioridade |
| --- | --- | --- | --- |
| 1 | vento > 0 e radiação_solar = 0 <br>

<br> → Usar energia eólica; solar indisponível | SUGESTÃO | 3 |
| 2 | radiação_solar > 0 e vento = 0 <br>

<br> → Usar energia solar; eólica indisponível | SUGESTÃO | 3 |
| 3 | vento = 0 e radiação_solar = 0 <br>

<br> → Operar apenas com reserva de baterias | SUGESTÃO | 3 |
| 4 | energia_disp > 50 e consumo < 30 e reserva < 49% <br>

<br> → Armazenar excedente | SUGESTÃO | 3 |
| 5 | energia_disp > 99 e reserva > 49% <br>

<br> → Parar produção solar e eólica | SUGESTÃO | 3 |
| 6 | energia_disp ≤ 30 e consumo ≥ 50% da disp. <br>

<br> → Risco de apagão; desligar módulos < crit. | ALERTA | 1 |
| 7 | radiação < 10%, vento < 10 e reserva < 50% <br>

<br> → Atenção; desligar módulos criticidade ≤ 2 | SUGESTÃO | 3 |
| 7 | Nenhuma regra acionada <br>

<br> → Sistema dentro dos parâmetros normais | SUGESTÃO | 3 |

## 10. 🧩 CENÁRIO DE TESTE PADRÃO

Os scripts de teste manual (`teste_regras.py` e `teste_previsao.py`) montam o seguinte cenário fixo para validação das camadas de regras e previsão de forma independente:

**Módulos cadastrados no cenário:**

| ID | Tipo | Criticidade | Consumo/h |
| --- | --- | --- | --- |
| MED-01 | Médico | 5 | 10 |
| HAB-02 | Habitação | 1 | 20 |
| LAB-03 | Laboratório | 3 | 30 |
| LOG-04 | Logístico | 2 | 30 |

**Sistemas de energia no cenário:**

| Nome | Tipo | Capacidade Máx. | Geração Atual |
| --- | --- | --- | --- |
| Painel | Solar | 30 kWh | 10 kWh |
| Torre | Eólico | 20 kWh | 0 kWh |
| Bateria | Reserva | 50 kWh | 20 kWh |

**Parâmetros ambientais do cenário:**

* **Velocidade do vento:** 0 km/h (sem geração eólica)
* **Radiação solar:** 40 W/m²

**Resultado esperado de `verificar_colonia()` neste cenário:**

* Regra 2 ativada: vento zero com radiação ativa → SUGESTÃO (prioridade 3)
* Regra 6 ativada: consumo (60) superior à disponível (30) → ALERTA (prioridade 1)

**Resultado esperado de `teste_previsao.py`:**

* Previsão eólica (vento=15 m/s): 9,90 kWh
* Previsão solar (radiação=70%): 21,00 kWh
* Análise eólica → SUGESTÃO (geração suficiente para consumo de 60)
* Análise solar → SUGESTÃO (21,00 kWh suficientes para consumo de 60)

## 11. 🧪 SCRIPTS DE TESTE MANUAL

O projeto conta com dois scripts de validação manual que exercitam cada camada de forma isolada, sem depender da interface interativa:

### `teste_regras.py` (`src/rules/`)

Monta o cenário padrão descrito na seção 10 e chama `verificar_colonia()` diretamente, exibindo todas as recomendações geradas no terminal em formato de tabela.

**Para executar:**

```bash
cd src/rules
python teste_regras.py

```

**Saída esperada:**

```text
----------------------------------------
| ANÁLISES                             |
----------------------------------------
| [3] SUGESTÃO: Energia eólica não ... |
| [1] ALERTA: Consumo (60) maior qu... |
----------------------------------------

```

### `teste_previsao.py` (`src/forecast/`)

Monta o cenário padrão com vento = 15 m/s e radiação = 70%, executa previsão pontual eólica e solar, roda a análise de suficiência para ambas as fontes e abre os quatro gráficos matplotlib em sequência: histórico eólico, histórico solar, previsão eólica e previsão solar.

**Para executar:**

```bash
cd src/forecast
python teste_previsao.py

```

**Saída esperada no terminal:**

```text
Previsão eólica (vento=15): 9.90 kWh
Previsão solar (radiação=70): 21.00 kWh
[3] SUGESTÃO: A energia eólica gerada (9.90) é suficiente...
[3] SUGESTÃO: A energia solar gerada (21.00) é suficiente...
[Quatro janelas de gráfico abertas em sequência]

```

```

```
