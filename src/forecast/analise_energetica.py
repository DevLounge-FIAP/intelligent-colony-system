from ..forecast.previsao import previsao_energia_eolica, previsao_energia_solar
from ..modules.modulos import Colonia

"""
Análise de suficiência energética.
Compara a energia prevista pelo modelo de regressão linear com o consumo
total atual da colônia e retorna recomendações de ALERTA ou SUGESTÃO.
"""

ACAO_ALERTA = "ALERTA"  
ACAO_SUGESTAO = "SUGESTÃO"
PRIORIDADE_CRITICA = 1
PRIORIDADE_SUGESTAO = 3


def analise_energetica_eolica(estado: Colonia):
    """
    Verifica se a energia eólica prevista é suficiente para atender
    o consumo total da colônia e retorna a recomendação correspondente.
    """

    vento_atual = estado.vento
    consumo_total = estado.consumo_total()
    energia_gerada = previsao_energia_eolica(vento_atual)
    
    recomendacoes = []

    if energia_gerada < consumo_total:
        recomendacoes.append({
            "tipo": ACAO_ALERTA,
            "mensagem": f"A energia eólica gerada ({energia_gerada:.2f}) é insuficiente para atender o consumo total ({consumo_total:.2f}). Considere reduzir o consumo ou aumentar a geração de energia.",
            "prioridade": PRIORIDADE_CRITICA,
            "origem": "analise_energetica"
        })
    else: 
        recomendacoes.append({
            "tipo": ACAO_SUGESTAO,
            "mensagem": f"A energia eólica gerada ({energia_gerada:.2f}) é suficiente para atender o consumo total ({consumo_total:.2f}).",
            "prioridade": PRIORIDADE_SUGESTAO,
            "origem": "analise_energetica"
        })

    return recomendacoes


def analise_energetica_solar(estado: Colonia):
    """
    Verifica se a energia solar prevista é suficiente para atender
    o consumo total da colônia e retorna a recomendação correspondente.
    """

    radiacao_atual = estado.radiacao_solar
    consumo_total = estado.consumo_total()
    energia_gerada = previsao_energia_solar(radiacao_atual)

    recomendacoes = []

    if energia_gerada < consumo_total:
        recomendacoes.append({
            "tipo": ACAO_ALERTA,
            "mensagem": f"A energia solar gerada ({energia_gerada:.2f}) é insuficiente para atender o consumo total ({consumo_total:.2f}). Considere reduzir o consumo ou aumentar a geração de energia.",
            "prioridade": PRIORIDADE_CRITICA,
            "origem": "analise_energetica"
        })
    else:
        recomendacoes.append({
            "tipo": ACAO_SUGESTAO,
            "mensagem": f"A energia solar gerada ({energia_gerada:.2f}) é suficiente para atender o consumo total ({consumo_total:.2f}).",
            "prioridade": PRIORIDADE_SUGESTAO,
            "origem": "analise_energetica"
        })

    return recomendacoes