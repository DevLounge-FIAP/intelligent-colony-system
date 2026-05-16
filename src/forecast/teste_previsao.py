from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

# Importações dos módulos do projeto
from modules.modulos import Colonia, Modulo, SistemaSolar, SistemaEolico, SistemaReserva
from forecast.previsao import previsao_energia_eolica, previsao_energia_solar, plotar_grafico_historico_eolica, plotar_grafico_historico_solar, plotar_grafico_previsao_eolica, plotar_grafico_previsao_solar
from forecast.analise_energetica import analise_energetica_eolica, analise_energetica_solar

# Monta cenário de teste com valores fixos
col = Colonia()
col.modulos.append(Modulo("MED-01", "Medico", "Suporte à Vida", 5, 10)) # <- Módulo médico, criticidade 5, consumo 10
col.modulos.append(Modulo("HAB-02", "Habitacao", "Moradia", 1, 20)) # <- Módulo de habitação, criticidade 1, consumo 20
col.modulos.append(Modulo("LAB-03", "Laboratorio", "Pesquisa", 3, 30)) # <- Módulo de laboratório, criticidade 3, consumo 30
col.sistemas.append(SistemaSolar("Painel", capacidade_max=30, geracao_atual=10)) # <- Sistema solar com capacidade máxima de 30 kWh
col.sistemas.append(SistemaEolico("Torre", capacidade_max=20, geracao_atual=0)) # <- Sistema eólico com capacidade máxima de 20 kWh
col.sistemas.append(SistemaReserva("Bateria", capacidade_max=50, carga_atual=20)) # <- Sistema de reserva com capacidade máxima de 50 kWh
col.vento = 15 # <- Velocidade do vento atual em m/s
col.radiacao_solar = 70 # <- Radiação solar atual em %

# Testa previsão de energia
print(f"Previsão eólica (vento={col.vento}): {previsao_energia_eolica(col.vento):.2f} kWh")
print(f"Previsão solar (radiação={col.radiacao_solar}): {previsao_energia_solar(col.radiacao_solar):.2f} kWh")

# Testa análise energética eólica
for r in analise_energetica_eolica(col):
    print(f"[{r['prioridade']}] {r['tipo']}: {r['mensagem']}")# <- puxa a list append de recomendações

# Testa análise energética solar
for r in analise_energetica_solar(col):
    print(f"[{r['prioridade']}] {r['tipo']}: {r['mensagem']}")# <- puxa a list append de recomendações

# Plota gráficos históricos
plotar_grafico_historico_eolica()
plotar_grafico_historico_solar()

# Plota gráficos de previsão atual
plotar_grafico_previsao_eolica(col.vento)
plotar_grafico_previsao_solar(col.radiacao_solar)