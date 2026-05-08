import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from modules.modulos import Colonia, Modulo, SistemaSolar, SistemaReserva, SistemaEolico
from regras_basicas import executar
from regras_compostas import verificar_colonia

# Monta cenário de exemplo: energia=40, consumo=70
col = Colonia()
col.modulos.append(Modulo("MED-01", "Medico", "Suporte à Vida", 5, 10)) #Adicinando modulo SUP-01
col.modulos.append(Modulo("HAB-02", "Habitacao", "Moradia", 1, 20))
col.modulos.append(Modulo("LAB-03", "Laboratorio", "Pesquisa", 3, 30)) #Adicinando modulo LAB-01
col.modulos.append(Modulo("LOG-04", "Logistico", "Logistíca de exploracao", 2, 30))
col.sistemas.append(SistemaSolar("Painel", capacidade_max=30, geracao_atual=10)) #Adicionando o sistema de paineis solares
col.sistemas.append(SistemaEolico("Torre", capacidade_max=20, geracao_atual=0))
col.sistemas.append(SistemaReserva("Bateria", capacidade_max=50, carga_atual=20)) #Adicionando o sistema de baterias
col.vento = 0
col.radiacao_solar = 40
acoes = executar(col)

for a in acoes:
    print(f"[{a['prioridade']}] {a['tipo']}: {a['mensagem']}")

recomendacoes = verificar_colonia(col)
for a in recomendacoes:
    print(f"[{a['prioridade']}] {a['tipo']}: {a['mensagem']}")
