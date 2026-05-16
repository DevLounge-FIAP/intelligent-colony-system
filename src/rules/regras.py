import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from modules.modulos import Colonia


ACAO_ALERTA = "ALERTA"
ACAO_SUGESTAO = "SUGESTÃO"

PRIORIDADE_CRITICA = 1
PRIORIDADE_SUGESTAO = 3

def verificar_colonia (estado: Colonia) -> list[dict]:
    '''
    Args:  
        estado: Objeto Colonia contem todos os módulos, sistemas e dados ambientais.

    Retorno (uma lista de dicionários de recomendação, cada um com as chaves):
        -tipo: "ALERTA", "SUGESTAO" ou "INFORMAÇÃO";
        -mensagem: string descritiva para o operador;
        -prioridade: 1(crítica), 2 (importante) ou 3(sugestão);
        -origem: "regras.py".
    '''

    recomendacoes = []

    #atribuindo dentro de variavéis os valores da base (obtidos em modulos.py)
    vento = estado.vento  
    radiacao_solar = estado.radiacao_solar       
    energia_disp = estado.energia_disponivel_total() 
    energia_perc = estado.nivel_energia_percentual() 
    consumo = estado.consumo_total()
    capacidade_total = estado.capacidade_total()
    modulos_desligaveis = estado.modulos_desligaveis()
    nomes_desligaveis = ", ".join(m.id_nome for m in modulos_desligaveis)
    modulos_desligados = [m for m in estado.modulos if not m.status]

    # --- Regra 1: verificações sobre os sistemas de energia ---

    # --- Sem produção de energia solar ---
    if vento > 0 and radiacao_solar == 0: 
        recomendacoes.append({
            "tipo": ACAO_SUGESTAO, 
            "mensagem": f"Energia solar não está sendo produzida. Utilize sistema de energia eólica.",
            "prioridade": PRIORIDADE_SUGESTAO,
            "origem": "regras"
        })

    # --- Sem produção de energia eólica ---
    elif radiacao_solar > 0 and vento == 0:
        recomendacoes.append({
            "tipo": ACAO_SUGESTAO, 
            "mensagem": f"Energia eólica não está sendo produzida. Utilize sistema de energia solar.",
            "prioridade": PRIORIDADE_SUGESTAO,
            "origem": "regras"
        })

    # --- Sem produção de nenhum tipo de energia ---
    elif vento == 0 and radiacao_solar == 0:
        capacidade_reserva = (energia_disp / capacidade_total * 100) if capacidade_total > 0 else 0.0
        recomendacoes.append({
            "tipo": ACAO_SUGESTAO, 
            "mensagem": f"Energia eólica e energia solar não estão sendo produzidas. Utilize reserva de energia: {capacidade_reserva:.1f}%.",
            "prioridade": PRIORIDADE_SUGESTAO,
            "origem": "regras"
        })
        
    # --- Regra 2: Excedente de produção de energia ---
    if energia_disp > 50 and consumo < 30 and capacidade_reserva < 49:
        recomendacoes.append({
            "tipo": ACAO_SUGESTAO,
            "mensagem": "Excedente de energia detectado. Armazenar na reserva.",
            "prioridade": PRIORIDADE_SUGESTAO,
            "origem": "regras"            
        })

    # --- Regra 3: Excedente de energia total---
    if energia_disp > 99 and capacidade_reserva > 49:
        recomendacoes.append({
            "tipo": ACAO_SUGESTAO,
            "mensagem": "Excedente de energia detectado. Parar produção de energias eólica e solar.",
            "prioridade": PRIORIDADE_SUGESTAO,
            "origem": "regras"            
        })
    # --- Regra 4: Alto consumo e pouca energia --- 
    if energia_disp <= 30 and consumo >= energia_disp *0.5:
        recomendacoes.append({
            "tipo": ACAO_ALERTA,
            "mensagem": f"Consumo ({consumo}%) maior que a energia disponível ({energia_disp}%). Risco de apagão. \n\tDesligue todos os módulos de baixa e média criticidade: {nomes_desligaveis}",
            "prioridade": PRIORIDADE_CRITICA,
            "origem": "regras"            
        })
    
    # --- Regra 5: Baixa produção de energia e baixa reserva de energia --- 
    if radiacao_solar < 10 and vento < 10 and energia_perc < 50:
        modulos_baixa_critic = [m for m in estado.modulos if m.status and m.criticidade <= 2] #identifica os módulos de baixa criticidade
        nomes_baixa_critic = ", ".join(m.id_nome for m in modulos_baixa_critic)
        recomendacoes.append({
            "tipo": ACAO_SUGESTAO,
            "mensagem": f"""A energia disponível está em atenção. 
                            Recomenda-se desligar os módulos de baixa criticidade: {nomes_baixa_critic}""",
            "prioridade": PRIORIDADE_SUGESTAO,
            "origem": "regras"            
        })
    
    # --- Regra 6: Ligar módulos ---
    if energia_disp > 50 and modulos_desligados: 
        recomendacoes.append({
            "tipo": ACAO_SUGESTAO,
            "mensagem": f"Níveis de energia normalizados. Recomenda-se ligar todos os módulos: {modulos_desligados}",
            "prioridade": PRIORIDADE_SUGESTAO,
            "origem": "regras"            
        })

    # --- Regra 7: Situação estavel ---
    if not recomendacoes:   # Aqui verifica se tem algo dentro de recomendacoes se não tiver faz isso
        recomendacoes.append({
            "tipo": ACAO_SUGESTAO,
            "mensagem": "SISTEMA ESTÁVEL: Energia e consumo dentro dos parâmetros normais.",
            "prioridade": PRIORIDADE_SUGESTAO,
            "origem": "regras"
        })

    return recomendacoes



    
        

