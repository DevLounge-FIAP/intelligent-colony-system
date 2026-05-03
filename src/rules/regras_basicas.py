import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from modules.modulos import Colonia


ACAO_ALERTA = "ALERTA"
ACAO_SUGESTAO = "SUGESTÃO"

PRIORIDADE_CRITICA = 1
PRIORIDADE_IMPORTANTE = 2
PRIORIDADE_SUGESTAO = 3

def executar (estado: Colonia) -> list[dict]:
    '''
    Aplica regras de decisão simples sobre o estado da colônia.

    Args:
        estado: Objeto Colonia contem todos os módulos, sistemas e dados ambientais.

    Retornos:
    Retorna uma lista de dicionários de ação, cada um com as chaves:
        -tipo: "ALERTA" ou "SUGESTAO";
        -mensagem: string descritiva para o operador;
        -prioridade: 1(crítica), 2 (importante) ou 3(sugestão);
        -origem: "regras_basicas.py".
    '''
    acoes = []

    energia_disp = estado.energia_disponivel_total() #só atribuindo dentro de uma variavel o valor da energia disponivel
    energia_perc = estado.nivel_energia_percentual() #só atribuindo dentro de uma variavel o valor da energia percentual
    consumo = estado.consumo_total()

    # --- Regra 1: Energia abaixo de 50% ---
    if energia_perc < 50:
        acoes.append({
            "tipo": ACAO_ALERTA, #note que estou pegando lá de cima a variavel ACAO_ALERTA que tem armazenado "ALERTA"
            "mensagem": f"ALERTA: Nível de energia em {energia_perc:.1f}% (abaixo de 50%). Reduzir consumo.",
            "prioridade": PRIORIDADE_IMPORTANTE,
            "origem": "regras_basicas"
        })


    # --- Regra 2: Consumo maior que a energia disponível ---
    # Exemplo: geração = 40, consumo = 70 -> ALERTA
    if consumo > energia_disp:
        acoes.append({
            "tipo": ACAO_ALERTA,
            "mensagem": f"ALERTA: Consumo ({consumo}) maior que a energia disponível ({energia_disp}). Risco de apagão.",
            "prioridade": PRIORIDADE_CRITICA,
            "origem": "regras_basicas"
        })

    # --- Regra 3: Excedente de energia ---
    # Exemplo: geração = 80, consumo = 30 -> SUGESTÃO armazenar
    if energia_disp > 80 and consumo < 40:
        acoes.append({
            "tipo": ACAO_SUGESTAO,
            "mensagem": "SUGESTÃO: Excedente de energia detectado. Armazenar na reserva.",
            "prioridade": PRIORIDADE_SUGESTAO,
            "origem": "regras_basicas"            
        })

    # --- Regra 4: Situação estavel ---
    if not acoes:   # Aqui verifica se tem algo dentro de acoes se não tiver faz isso
        acoes.append({
            "tipo": ACAO_SUGESTAO,
            "mensagem": "SISTEMA ESTÁVEL: Energia e consumo dentro dos parâmetros normais.",
            "prioridade": PRIORIDADE_SUGESTAO,
            "origem": "regra_basica"
        })
    return acoes