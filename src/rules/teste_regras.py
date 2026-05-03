#Michelly usa esse arquivo para se guiar aqui tu vai entender a estrutura das regras básicas e como fazer para adicionar modulos, etc...


import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from modules.modulos import Colonia, Modulo, SistemaSolar, SistemaReserva
from regras_basicas import executar

# Monta cenário de exemplo: energia=40, consumo=70
col = Colonia()
col.modulos.append(Modulo("SUP-01", "Medico", "Suporte à Vida", 5, 30)) #Adicinando modulo SUP-01
col.modulos.append(Modulo("LAB-01", "Laboratorio", "Pesquisa", 3, 40)) #Adicinando modulo LAB-01
col.sistemas.append(SistemaSolar("Painel", capacidade_max=50, geracao_atual=30)) #Adicionando o sistema de paineis solares
col.sistemas.append(SistemaReserva("Bateria", capacidade_max=50, carga_atual=10)) #Adicionando o sistema de baterias

acoes = executar(col)
for a in acoes:
    print(f"[{a['prioridade']}] {a['tipo']}: {a['mensagem']}")