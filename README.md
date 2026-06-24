# 🛰️ SIGIC — Sistema de Gerenciamento da Infraestrutura da Colônia

**Projeto Acadêmico — FIAP**  
Documentação Oficial do Sistema de Navegação e Análise de Grafos para Colônias em Ambiente Extremo  
**Versão:** 1.0 | **Data:** Junho de 2026 | **Status:** Funcional

---

## 👥 Equipe

| Integrante | Responsabilidade |
|---|---|
| 🔵 **Victor** | Algoritmos de Grafo (BFS, DFS, Dijkstra, Conexões Críticas), Menu Principal e Integração |
| 🔴 **Michelly** | Estruturas de Dados, Modelagem da Colônia (classes `Modulo` e `Colonia`), Matriz de Adjacências |
| 🟢 **Bruno** | Modelagem Matemática, Documentação, Sustentabilidade & Governança, README |

> Repositório: [github.com/ChellySantos/Fase-4---FIAP](https://github.com/ChellySantos/Fase-4---FIAP.git)  
> Arquivo principal de execução: `codigo_fonte.py`

---

## 📋 Sumário

1. [Visão Geral](#1-visão-geral)
2. [Características do Sistema](#2-características-do-sistema)
3. [Arquitetura Modular e Equipe](#3-arquitetura-modular-e-equipe)
4. [Estrutura de Diretórios do Projeto](#4-estrutura-de-diretórios-do-projeto)
5. [Requisitos e Instalação](#5-requisitos-e-instalação)
6. [Guia de Uso e Exemplos de Execução](#6-guia-de-uso-e-exemplos-de-execução)
7. [Estruturas de Dados e Complexidade](#7-estruturas-de-dados-e-complexidade)
8. [Algoritmos Implementados](#8-algoritmos-implementados)
9. [Modelagem Matemática](#9-modelagem-matemática)
10. [Módulos da Colônia](#10-módulos-da-colônia)
11. [Sustentabilidade e Governança](#11-sustentabilidade-e-governança)
12. [Testes Automatizados](#12-testes-automatizados)

---

## 1. 🎯 Visão Geral

O SIGIC (Sistema de Gerenciamento da Infraestrutura da Colônia) é um sistema interativo de análise e navegação em grafos para uma colônia instalada em ambiente hostil (Marte).

O sistema representa a infraestrutura da colônia como um grafo não-direcionado, onde os nós são os módulos físicos da base (habitação, laboratório, centro de controle, etc.) e as arestas representam as conexões operacionais entre eles. A partir dessa modelagem, o sistema oferece ferramentas para explorar a rede, encontrar rotas eficientes, simular falhas e identificar pontos críticos de vulnerabilidade.

O objeto central é a classe `Colonia`, desenvolvida pela **Michelly**, que agrega todos os módulos e seus atributos, servindo como entrada única para todas as funções de algoritmos e visualização implementadas por **Victor**.

---

## 2. ⭐ Características do Sistema

- **Menu Interativo com 9 Opções** *(Victor):* Navegação direta por todas as funcionalidades — visualização, consulta de módulos, execução de algoritmos, simulação de falhas e análise de eficiência — implementada com `match/case` (Python 3.10+).

- **Representação por Grafo** *(Michelly):* A colônia é modelada como uma matriz de adjacências 8×8, com pesos calculados dinamicamente a partir da distância euclidiana entre os módulos, tempo de comunicação e custo energético da transmissão.

- **Três Algoritmos de Grafo** *(Victor):* BFS (Busca em Largura), DFS (Busca em Profundidade) e Dijkstra (Caminho Mínimo) — cada um com finalidade distinta e complexidade documentada.

- **Identificação de Conexões Críticas** *(Victor):* Algoritmo de Tarjan baseado em DFS com timestamps que detecta automaticamente todas as arestas cuja remoção tornaria a rede desconexa (pontes do grafo).

- **Simulação de Falhas na Rede** *(Victor):* Testa o impacto da remoção de uma conexão específica ou da desativação de múltiplos módulos simultaneamente, executando BFS para verificar conectividade e restaurando a rede ao estado original ao final.

- **Análise Comparativa de Eficiência** *(Victor):* Exibe lado a lado os resultados de BFS, DFS e Dijkstra para o mesmo par de módulos.

- **Visualização do Mapa** *(Michelly):* Gera um gráfico `matplotlib` com todos os módulos posicionados por coordenadas no espaço 10×10 da colônia, exportando como `Mapa_Colonia.png`.

- **Modelagem Matemática e Documentação** *(Bruno):* Fórmula de peso das arestas, justificativa das estruturas de dados, reflexão sobre sustentabilidade e governança, e documentação oficial do projeto.

---

## 3. 🏗️ Arquitetura Modular e Equipe

```text
┌──────────────────────────────────────────────────────────────────────────┐
│                          PROGRAMA PRINCIPAL                              │
│                            (codigo_fonte.py)                             │
│                          🔵 Victor                                       │
│  - Menu interativo (match/case com 9 opções)                             │
│  - Instância única de Colonia compartilhada entre funções                │
│  - Integração entre os pacotes funcionais                                │
│  - Tratamento de entradas e validações                                   │
└──────┬─────────────────────┬──────────────────────────┬──────────────────┘
       │                     │                          │
┌──────▼──────────┐  ┌───────▼──────────────┐  ┌───────▼──────────────────┐
│  MODELAGEM      │  │  ALGORITMOS DE GRAFO │  │  DOCUMENTAÇÃO            │
│  🔴 Michelly    │  │  🔵 Victor           │  │  🟢 Bruno                │
│                 │  │                      │  │                          │
│ • Classe Modulo │  │ • BFS                │  │ • README.md              │
│ • Classe Colonia│  │ • DFS                │  │ • Modelagem matemática   │
│ • Métodos de    │  │ • Dijkstra           │  │ • Justificativa das      │
│   consulta por  │  │ • Conexões Críticas  │  │   estruturas de dados    │
│   status e      │  │   (Tarjan)           │  │ • Sustentabilidade e     │
│   prioridade    │  │ • sistema.py         │  │   governança             │
│ • Mapa visual   │  │ • testes.py          │  │ • rede_colonia.pdf       │
│   (matplotlib)  │  │                      │  │ • documentacao_          │
│ • Matriz 8×8    │  │                      │  │   complementar.pdf       │
│ • Cálculo de    │  │                      │  │                          │
│   pesos         │  │                      │  │                          │
└─────────────────┘  └──────────────────────┘  └──────────────────────────┘
```

### Atribuições Detalhadas

**🔵 VICTOR — Algoritmos, Sistema & Main**  
`src/codigo_fonte.py` — Menu interativo multi-opções, função `selecionar_modulo()` reutilizável, integração entre os pacotes, validações e tratamento de entradas.  
`src/sistema.py` — Inicialização da colônia com os 8 módulos predefinidos.  
`src/testes.py` — Bateria de 8 testes automatizados com `assert`.  
`src/algorithms/algoritmos.py` — Funções `bfs()`, `dfs()`, `dijkstra()` e `conexoes_criticas()`.

**🔴 MICHELLY — Estrutura de Dados & Modelagem da Colônia**  
`src/modules/modulos.py` — Classes `Modulo` e `Colonia` com todos os atributos e métodos de consulta por status e prioridade.  
`src/modules/mapa.py` — Matriz de adjacências 8×8, visualização `matplotlib`, cálculo de distância euclidiana e peso das arestas.  
`src/optimization/modelagem.py` — Estrutura auxiliar de modelagem.

**🟢 BRUNO — Modelagem Matemática, ESG & Documentação**  
`README.md` — Documentação oficial completa do projeto.  
`documentacao_complementar.pdf` — Relatório técnico com modelagem matemática, análise das estruturas de dados, reflexão sobre sustentabilidade e governança.  
`rede_colonia.pdf` — Diagrama visual da rede da colônia.

---

## 4. 📁 Estrutura de Diretórios do Projeto

```text
Fase-4---FIAP/
│
├── src/                              # Código-fonte principal
│   ├── codigo_fonte.py               # Programa principal — menu interativo (Victor)
│   ├── sistema.py                    # Inicialização da Colonia com os 8 módulos (Victor)
│   ├── testes.py                     # Bateria de testes automatizados (Victor)
│   │
│   ├── modules/                      # Camada de Modelagem (Michelly)
│   │   ├── __init__.py
│   │   ├── modulos.py                # Classes Modulo e Colonia
│   │   └── mapa.py                   # Matriz de adjacências, visualização e pesos
│   │
│   ├── algorithms/                   # Algoritmos de Grafo (Victor)
│   │   ├── __init__.py
│   │   └── algoritmos.py             # BFS, DFS, Dijkstra e Conexões Críticas
│   │
│   └── optimization/                 # Modelagem Auxiliar (Michelly)
│       ├── __init__.py
│       └── modelagem.py
│
├── Mapa_Colonia.png                  # Mapa visual gerado pelo sistema
└── README.md                         # Documentação oficial (Bruno)
```

---

## 5. 📦 Requisitos e Instalação

- **Ambiente Operacional:** Windows, macOS ou Linux
- **Interpretador:** Python 3.10 ou superior (obrigatório para `match/case`)
- **Dependência Externa:** `matplotlib`

### Passos para Configuração

**1. Clone o repositório:**

```bash
git clone https://github.com/ChellySantos/Fase-4---FIAP.git
cd Fase-4---FIAP
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
pip install matplotlib
```

---

## 6. 💻 Guia de Uso e Exemplos de Execução

Para iniciar o sistema interativo principal:

```bash
cd src
python codigo_fonte.py
```

O terminal exibirá o menu principal:

```text
╔══════════════════════════════════════════╗
║     SIGIC — Sistema de Gerenciamento     ║
║        da Infraestrutura da Colônia      ║
╠══════════════════════════════════════════╣
║  1. Visualizar rede da colônia           ║
║  2. Consultar módulos                    ║
║  3. Executar BFS                         ║
║  4. Executar DFS                         ║
║  5. Executar Dijkstra                    ║
║  6. Simular falha na rede                ║
║  7. Análise de eficiência                ║
║  8. Identificar conexões críticas        ║
║  9. Sair                                 ║
╚══════════════════════════════════════════╝
```

### Fluxo Recomendado de Uso

**Passo 1 — Explorar a rede via `[1]` e `[2]`:**
- `[1]` Gera o mapa visual com todos os módulos e conexões, salvando em `Mapa_Colonia.png`.
- `[2]` Lista os 8 módulos com ID, tipo, status e prioridade.

**Passo 2 — Executar algoritmos via `[3]`, `[4]` e `[5]`:**
- `[3]` Executa BFS — percorre a rede nível a nível a partir de uma origem.
- `[4]` Executa DFS — percorre a rede por profundidade (ramo por ramo).
- `[5]` Executa Dijkstra — encontra o caminho mais eficiente entre dois módulos.

**Passo 3 — Analisar resiliência via `[6]`, `[7]` e `[8]`:**
- `[6]` Simula remoção de conexão ou desativação de módulos e verifica impacto.
- `[7]` Compara BFS, DFS e Dijkstra lado a lado para o mesmo par de módulos.
- `[8]` Detecta automaticamente todas as conexões críticas (pontes) da rede.

### Exemplos de Saída

**BFS a partir de HAB-01:**
```text
📡 BFS a partir de HAB-01:
HAB-01 → CTR-01 → AGR-01 → MED-01 → ENE-01 → LAB-01 → COM-01 → OXI-01
```

**Dijkstra de HAB-01 até LAB-01:**
```text
🛰️ Dijkstra — Caminho mais eficiente de HAB-01 até LAB-01:
HAB-01 → CTR-01 → LAB-01
Custo total: 47.83
```

**Simulação de falha:**
```text
🔌 Conexão CTR-01 ↔ ENE-01 removida temporariamente.
✅ Rede ainda conectada — todos os módulos permanecem acessíveis.
   A conexão CTR-01 ↔ ENE-01 NÃO é crítica.
🔁 Caminho alternativo: CTR-01 → AGR-01 → ENE-01
🔧 Conexão CTR-01 ↔ ENE-01 restaurada.
```

---

## 7. 🧱 Estruturas de Dados e Complexidade

*(Estruturas definidas por **Michelly** — justificativa redigida por **Bruno**)*

**1. Objeto `Colonia` (Contexto Central)**  
Agrega em tempo de execução a lista de módulos e o dicionário de acesso rápido por ID. É o único parâmetro de entrada das funções de algoritmos e visualização. Centraliza o estado da simulação em um único objeto.

**2. Lista de Módulos (`colonia.modulos`)**  
Armazena os objetos `Modulo` em ordem de inserção. Inserção em O(1); iteração O(n) para consultas filtradas por status ou prioridade.

**3. Dicionário de Módulos (`colonia.dict_modulos`)**  
Mapeamento `id_nome → Modulo` para acesso direto em O(1). Usado pelos algoritmos para traduzir nome de módulo em índice da matriz sem iteração.

**4. Matriz de Adjacências (`matriz_conexoes`) — 8×8**  
Lista de listas em Python representando as conexões entre módulos. Valor `1` indica conexão direta; `0` indica ausência. Simétrica (grafo não-direcionado). Acesso em O(1); iteração completa em O(V²).

**5. Fila (`collections.deque`)**  
Empregada no BFS para garantir a ordem FIFO (First-In, First-Out) de exploração nível a nível. Inserção e remoção em O(1).

**6. Pilha (`list` com `pop()`)**  
Utilizada no DFS para implementar a ordem LIFO (Last-In, First-Out), aprofundando a busca em um ramo antes de retroceder.

**7. Tupla (`tuple`)**  
Armazena as coordenadas cartesianas `(x, y)` de cada módulo no mapa. Escolha coerente pois as posições dos módulos são imutáveis durante toda a execução.

### Métodos de Consulta da Classe `Colonia`

```text
+----------------------------+----------+--------------------------------------+
| Método                     | Retorno  | Descrição                            |
+----------------------------+----------+--------------------------------------+
| adicionar_modulo(modulo)   | None     | Insere módulo na lista e no dict     |
| mapa_modulos()             | dict     | Retorna dict_modulos completo        |
| modulos_ativo()            | list     | Módulos com status = "ativo"         |
| modulos_manutencao()       | list     | Módulos com status = "manutencao"    |
| modulos_alerta()           | list     | Módulos com status = "alerta"        |
| modulos_inativo()          | list     | Módulos com status = "inativo"       |
| modulos_alta_prioridade()  | list     | Módulos com prioridade ≤ 2           |
| modulos_baixa_prioridade() | list     | Módulos com prioridade > 2           |
| modulos_coordenadas()      | list     | Lista de tuplas (x, y) de cada módulo|
+----------------------------+----------+--------------------------------------+
```

---

## 8. 🔧 Algoritmos Implementados

*(Implementados por **Victor**)*

### 1. BFS — Busca em Largura

- **Função:** `bfs(colonia, id_origem)`
- **Estrutura auxiliar:** `collections.deque` (fila FIFO)
- **Complexidade:** O(V + E)

Percorre os módulos da colônia nível a nível a partir da origem — visita todos os vizinhos diretos antes de avançar para os próximos níveis. Aplicação: verificar conectividade da rede e identificar módulos isolados após falhas.

### 2. DFS — Busca em Profundidade

- **Função:** `dfs(colonia, id_origem)`
- **Estrutura auxiliar:** `list` usada como pilha (LIFO)
- **Complexidade:** O(V + E)

Percorre a rede indo o mais fundo possível em cada ramo antes de retroceder. Base para o algoritmo de identificação de conexões críticas. Aplicação: exploração completa da rede.

### 3. Dijkstra — Caminho Mínimo

- **Função:** `dijkstra(colonia, id_origem, id_destino)`
- **Estrutura auxiliar:** vetor de custos + vetor de anteriores
- **Complexidade:** O(V²)

Calcula o caminho de menor custo entre dois módulos usando os pesos reais das arestas (distância, tempo e consumo de comunicação). Aplicação: roteamento eficiente de energia e dados entre módulos.

### 4. Conexões Críticas — Algoritmo de Tarjan

- **Função:** `conexoes_criticas(colonia)`
- **Estrutura auxiliar:** vetores `descoberta[]` e `baixo[]` com timestamps
- **Complexidade:** O(V + E)

Identifica todas as pontes do grafo — conexões cuja remoção aumenta o número de componentes conexos. Uma aresta (v, w) é crítica quando `baixo[w] > descoberta[v]`, indicando que não existe caminho alternativo de w para alcançar v. Aplicação: planejamento de redundância e resiliência da rede.

---

## 9. 📐 Modelagem Matemática

*(Desenvolvida por **Bruno**)*

O peso de cada aresta no grafo do Dijkstra é calculado pela função `calcular_peso()` em `mapa.py`, combinando três componentes derivados da distância euclidiana entre as coordenadas dos módulos:

```text
+----------------------+-----------------------------------+------------------------------------------+
| Componente           | Fórmula                           | Descrição                                |
+----------------------+-----------------------------------+------------------------------------------+
| Distância Euclidiana | d = √((x2-x1)² + (y2-y1)²)       | Distância no mapa entre dois módulos     |
| Distância Real       | d_m = d × 500                     | Conversão para metros (1 unidade = 500m) |
| Tempo de Comunicação | t = d × 0.5                       | Tempo de transmissão em segundos         |
| Consumo Energético   | e = t × 5                         | Consumo em Watts da transmissão          |
| Peso Total           | w = d_m + t + e                   | Custo total da aresta no grafo           |
+----------------------+-----------------------------------+------------------------------------------+
```

**Análise qualitativa:** O peso composto penaliza simultaneamente módulos distantes (alto `d_m`), rotas de alta latência (alto `t`) e conexões energeticamente custosas (alto `e`). Isso garante que o Dijkstra selecione rotas que minimizam o impacto operacional total da comunicação, e não apenas a distância física — fundamental em um ambiente marciano onde energia é um recurso crítico.

**Justificativa da estrutura da rede:** A rede foi projetada com CTR-01 como nó central (hub) conectado a todos os demais módulos, garantindo conectividade máxima da base. As conexões periféricas criam caminhos alternativos redundantes, eliminando a existência de pontes — verificado automaticamente pela função `conexoes_criticas()`, que retorna lista vazia para a rede padrão da colônia.

---

## 10. 🧩 Módulos da Colônia

*(Definidos por **Michelly** em `sistema.py`)*

A colônia é inicializada com 8 módulos predefinidos, cada um com coordenadas fixas no espaço 10×10 do mapa:

```text
+--------+------------------------+----------+---------+----------+--------+
|   ID   |          Tipo          |Prioridade|Consumo/h|Cap. Arm. |Coord.  |
+--------+------------------------+----------+---------+----------+--------+
| HAB-01 | Habitação              |    1     |  120 W  |  40 kW   | (9, 5) |
| CTR-01 | Centro de Controle     |    2     |  100 W  | 100 kW   | (5, 6) |
| ENE-01 | Armazenamento Energia  |    3     |   50 W  | 500 kW   | (2, 8) |
| AGR-01 | Agricultura            |    5     |  130 W  |  20 kW   | (8, 8) |
| LAB-01 | Laboratório Científico |    4     |  100 W  |  25 kW   | (2, 2) |
| COM-01 | Comunicação            |    3     |   60 W  |  20 kW   | (5, 3) |
| MED-01 | Suporte Médico         |    4     |   60 W  |  50 kW   | (8, 2) |
| OXI-01 | Produção de Oxigênio   |    2     |  180 W  |  50 kW   | (1, 5) |
+--------+------------------------+----------+---------+----------+--------+
```

> Prioridade: **1 = mais crítico** (HAB-01, OXI-01) → **5 = menos crítico** (AGR-01)

**Matriz de conexões (grafo não-direcionado):**

```text
        HAB CTR ENE AGR LAB COM MED OXI
  HAB [  0,  1,  0,  1,  0,  0,  1,  0 ]
  CTR [  1,  0,  1,  1,  1,  1,  1,  1 ]
  ENE [  0,  1,  0,  1,  0,  0,  0,  1 ]
  AGR [  1,  1,  1,  0,  0,  0,  0,  0 ]
  LAB [  0,  1,  0,  0,  0,  1,  0,  1 ]
  COM [  0,  1,  0,  0,  1,  0,  1,  0 ]
  MED [  1,  1,  0,  0,  0,  1,  0,  0 ]
  OXI [  0,  1,  1,  0,  1,  0,  0,  0 ]
```

> **CTR-01** é o nó central da rede — único módulo conectado a todos os demais.

---

## 11. 🌱 Sustentabilidade e Governança

*(Reflexão desenvolvida por **Bruno**)*

O SIGIC foi projetado com princípios de sustentabilidade e governança desde sua concepção:

1. **Eficiência energética:** O Dijkstra minimiza o consumo energético ao selecionar rotas de menor custo composto — distância, latência e consumo de transmissão — reduzindo o desperdício de recursos em um ambiente onde energia é escassa.

2. **Manutenção preventiva:** A identificação de conexões críticas permite priorizar reforço e redundância nos pontos mais vulneráveis da rede antes que falhas ocorram, evitando interrupções catastróficas na infraestrutura da colônia.

3. **Planejamento de contingências:** A simulação de falhas possibilita testar cenários adversos sem risco à operação real da colônia, permitindo decisões operacionais mais seguras e embasadas.

4. **Governança tecnológica:** O SIGIC centraliza as decisões operacionais no CTR-01 (Centro de Controle), mas mantém rotas alternativas para todos os módulos através da rede redundante. Isso garante resiliência mesmo em cenários adversos — fundamental para a sobrevivência em ambiente marciano, onde não há suporte externo imediato.

---

## 12. ✅ Testes Automatizados

*(Desenvolvidos por **Victor**)*

O arquivo `testes.py` contém 8 testes independentes que validam o comportamento correto de cada algoritmo sem passar pelo menu interativo:

```bash
cd src
python testes.py
```

**Saída esperada:**

```text
Executando bateria de testes do SIGIC...

✅ teste_bfs passou
✅ teste_bfs_origem_invalida passou
✅ teste_dfs passou
✅ teste_dijkstra_caminho_direto passou (custo=28.75)
✅ teste_dijkstra_mesmo_modulo passou
✅ teste_conexoes_criticas_rede_real passou
✅ teste_conexoes_criticas_rede_em_linha passou
✅ teste_matriz_simetrica passou

🎉 Todos os testes passaram!
```

**Cobertura dos testes:**

```text
+----------------------------------------+--------------------------------------------+
| Teste                                  | O que valida                               |
+----------------------------------------+--------------------------------------------+
| teste_bfs                              | BFS visita todos os 8 módulos e começa     |
|                                        | pela origem correta                        |
| teste_bfs_origem_invalida              | Módulo inexistente retorna None sem crash  |
| teste_dfs                              | DFS visita todos os 8 módulos              |
| teste_dijkstra_caminho_direto          | Caminho direto tem 2 módulos e custo > 0  |
| teste_dijkstra_mesmo_modulo            | Origem = destino resulta em custo = 0     |
| teste_conexoes_criticas_rede_real      | Rede da colônia não tem pontes            |
| teste_conexoes_criticas_rede_em_linha  | Rede A-B-C artificial tem 2 pontes        |
| teste_matriz_simetrica                 | Matriz de adjacências é simétrica         |
+----------------------------------------+--------------------------------------------+
```

---

*Documentação Oficial — Equipe SIGIC | FIAP 2026*  
*Bruno · Victor · Michelly*
