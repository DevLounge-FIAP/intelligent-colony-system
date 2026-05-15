from pathlib import Path
import sys # <- permissão para importar ou exportar os módulos do código todo
sys.path.insert(0, str(Path(__file__).parent.parent)) # <- Aquilo de criar pastas a cima do arquivo, para o python saber onde procurar os arquivos e não dar erro

from forecast.previsao import previsao_energia_eolica, previsao_energia_solar

from modules.modulos import Colonia # <- importa a classe Colonia do arquivo modulos.py da página modules
"""
Importações necessárias para a análise energética, incluindo a função de previsão de energia eólica e solar, e a classe Colonia que representa o estado atual da colônia.
"""

ACAO_ALERTA = "ALERTA"  
ACAO_SUGESTAO = "SUGESTÃO"
PRIORIDADE_CRITICA = 1
PRIORIDADE_SUGESTAO = 3

"""
Declaração das variáveis de ação e prioridade para as recomendações geradas pela análise energética. Essas variáveis são usadas para categorizar as recomendações como alertas ou sugestões, e para definir a prioridade de cada recomendação.
"""

def analise_energetica_eolica(estado:Colonia):
    """Função que verifica se a energica eólica gerada é o suficiente para atender o consumo total da colônia, e gera recomendações de acordo com essa análise."""

    vento_atual = estado.vento # <- Puxa o estado do vento atual da colônia.
    consumo_total = estado.consumo_total() # <- Puxa o consumo total de energia da colônia.

    energia_gerada = previsao_energia_eolica(vento_atual) # <- Faz o cálculo criado em previsao_energia_eolica com base no vento atual da colônia para obter a energia eólica gerada.
    
    recomendacoes = [] # <- inicia uma lista vazia para permitir utilizar o append depois, igual a Michelly fez :)

    if energia_gerada < consumo_total: # <- Condição que verifica se energia gerada é menor que consumo total 
        recomendacoes.append({ # <- utilização da lista recomendacoes para adicionar um dicionário com as informações do alerta, caso a condição if seja verdadeira
            "tipo": ACAO_ALERTA,
            "mensagem": f"A energia eólica gerada ({energia_gerada:.2f}) é insuficiente para atender o consumo total ({consumo_total:.2f}). Considere reduzir o consumo ou aumentar a geração de energia.",
            "prioridade": PRIORIDADE_CRITICA,
            "origem": "analise_energetica"
        })
    else: 
        recomendacoes.append({ # <- utilização da lista recomendacoes para adicionar um dicionário com as informações da sugestão, caso a condição if seja falsa
            "tipo": ACAO_SUGESTAO,
            "mensagem": f"A energia eólica gerada ({energia_gerada:.2f}) é suficiente para atender o consumo total ({consumo_total:.2f}).",
            "prioridade": PRIORIDADE_SUGESTAO,
            "origem": "analise_energetica"
        })

    return recomendacoes



def analise_energetica_solar(estado:Colonia):
    """Mesma coisa da analise eólica."""

    radiacao_atual = estado.radiacao_solar # <- Obtém a radiação solar atual do estado da colônia, que é um dos fatores que influenciam a geração de energia solar.
    consumo_total = estado.consumo_total() # <- Obtém o consumo total de energia da colônia, que é a quantidade de energia necessária para atender as necessidades da colônia.

    energia_gerada = previsao_energia_solar(radiacao_atual) # <- Faz o cálculo criado em previsao_energia_solar com base na radiação solar atual da colônia.

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

