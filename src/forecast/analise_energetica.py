from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from forecast.previsao import previsao_energia_eolica, previsao_energia_solar

from modules.modulos import Colonia
"""
Importações necessárias para a análise energética, incluindo a função de previsão de energia eólica e solar, e a classe Colonia que representa o estado atual da colônia.
"""

ACAO_ALERTA = "ALERTA"
ACAO_SUGESTAO = "SUGESTÃO"
PRIORIDADE_CRITICA = 1
PRIORIDADE_SUGESTAO = 3

def analise_energetica_eolica(estado:Colonia):
    
    vento_atual = estado.vento
    consumo_total = estado.consumo_total()

    energia_gerada = previsao_energia_eolica(vento_atual)
    
    recomendacoes = []

    if energia_gerada < consumo_total :
        recomendacoes.append({
            "tipo": ACAO_ALERTA,
            "mensagem": f"ALERTA: A energia eólica gerada ({energia_gerada:.2f}) é insuficiente para atender o consumo total ({consumo_total:.2f}). Considere reduzir o consumo ou aumentar a geração de energia.",
            "prioridade": PRIORIDADE_CRITICA,
            "origem": "analise_energetica"
        })
    else:
        recomendacoes.append({
            "tipo": ACAO_SUGESTAO,
            "mensagem": f"SUGESTÃO: A energia eólica gerada ({energia_gerada:.2f}) é suficiente para atender o consumo total ({consumo_total:.2f}).",
            "prioridade": PRIORIDADE_SUGESTAO,
            "origem": "analise_energetica"
        })

    return recomendacoes

def analise_energetica_solar(estado:Colonia):

    radiacao_atual = estado.radiacao_solar
    consumo_total = estado.consumo_total()

    energia_gerada = previsao_energia_solar(radiacao_atual)

    recomendacoes = []

    if energia_gerada < consumo_total:
        recomendacoes.append({
            "tipo": ACAO_ALERTA,
            "mensagem": f"ALERTA: A energia solar gerada ({energia_gerada:.2f}) é insuficiente para atender o consumo total ({consumo_total:.2f}). Considere reduzir o consumo ou aumentar a geração de energia.",
            "prioridade": PRIORIDADE_CRITICA,
            "origem": "analise_energetica"
        })
    else:
        recomendacoes.append({
            "tipo": ACAO_SUGESTAO,
            "mensagem": f"SUGESTÃO: A energia solar gerada ({energia_gerada:.2f}) é suficiente para atender o consumo total ({consumo_total:.2f}).",
            "prioridade": PRIORIDADE_SUGESTAO,
            "origem": "analise_energetica"
        })

    return recomendacoes