import matplotlib.pyplot as plt
import numpy as np

"""
Módulo de previsão energética.
Contém os dados históricos, regressão linear e geração dos quatro
gráficos de visualização (histórico eólico, histórico solar,
previsão eólica e previsão solar).
"""


def historico_dados_eolica():
    """
    Armazena os dados históricos de geração de energia eólica.

    Regra de geração: 0.66 kWh por m/s de vento (20 kWh / 30 m/s máx).
    Velocidade máxima considerada: 30 m/s.
    """
    nome = "Eólica"
    velocidade_vento = [28,    12,   8,     16,    20,    18]
    energia_gerada   = [18.48, 7.92, 5.28, 10.56, 13.20, 11.88]
    return nome, velocidade_vento, energia_gerada


def historico_dados_solar():
    """
    Armazena os dados históricos de geração de energia solar.

    Regra de geração: 0.30 kWh por % de radiação (30 kWh / 100% máx).
    Radiação máxima considerada: 100%.
    """
    nome = "Solar"
    radiacao_solar = [90,    70,    50,    80,    30,   60]
    energia_gerada = [27.00, 21.00, 15.00, 24.00, 9.00, 18.00]
    return nome, radiacao_solar, energia_gerada


def regressao_eolica():
    """
    Calcula os coeficientes a (inclinação) e b (intercepto) da reta de
    regressão linear para os dados históricos eólicos via numpy.polyfit.
    """
    nome, velocidade_vento, energia_gerada = historico_dados_eolica()
    coeficientes = np.polyfit(velocidade_vento, energia_gerada, 1)
    return coeficientes[0], coeficientes[1]


def regressao_solar():
    """
    Mesma lógica da regressão eólica, aplicada aos dados solares.
    """
    nome, radiacao_solar, energia_gerada = historico_dados_solar()
    coeficientes = np.polyfit(radiacao_solar, energia_gerada, 1)
    return coeficientes[0], coeficientes[1]


def previsao_energia_eolica(velocidade_vento):
    """
    Prevê a energia eólica gerada (kWh) para uma dada velocidade de vento (m/s)
    usando o modelo de regressão linear: energia = a * vento + b.
    """
    a, b = regressao_eolica()
    return a * velocidade_vento + b


def previsao_energia_solar(radiacao_solar):
    """
    Prevê a energia solar gerada (kWh) para uma dada radiação (%)
    usando o modelo de regressão linear: energia = a * radiacao + b.
    """
    a, b = regressao_solar()
    return a * radiacao_solar + b


def plotar_grafico_historico_eolica():
    """
    Exibe o gráfico histórico eólico: pontos dos dados de treinamento
    e reta de regressão ajustada.
    """
    nome, velocidade_vento, energia_gerada = historico_dados_eolica()
    a, b = regressao_eolica()

    plt.figure()  # garante figura nova a cada chamada
    x_reta = np.linspace(0, 30, 100)
    y_reta = a * x_reta + b

    plt.scatter(velocidade_vento, energia_gerada, zorder=3)
    plt.plot(x_reta, y_reta, zorder=2)
    for x, y in zip(velocidade_vento, energia_gerada):
        plt.annotate(f"{y:.2f} kWh", (x, y), textcoords="offset points",
                     fontsize=6, xytext=(0, 10), ha='center')
    plt.xlabel("Velocidade do Vento (m/s)")
    plt.ylabel("Energia Gerada (kWh)")
    plt.title(f"Energia {nome} Gerada vs Velocidade do Vento")
    plt.grid()
    plt.show()


def plotar_grafico_historico_solar():
    """
    Exibe o gráfico histórico solar: pontos dos dados de treinamento
    e reta de regressão ajustada.
    """
    nome, radiacao_solar, energia_gerada = historico_dados_solar()
    a, b = regressao_solar()

    plt.figure()  # garante figura nova a cada chamada
    x_reta = np.linspace(0, 100, 100)
    y_reta = a * x_reta + b

    plt.scatter(radiacao_solar, energia_gerada, zorder=3)
    plt.plot(x_reta, y_reta, zorder=2)
    for x, y in zip(radiacao_solar, energia_gerada):
        plt.annotate(f"{y:.2f} kWh", (x, y), textcoords="offset points",
                     fontsize=6, xytext=(0, 10), ha='center')
    plt.xlabel("Radiação Solar (%)")
    plt.ylabel("Energia Gerada (kWh)")
    plt.title(f"Energia {nome} Gerada vs Radiação Solar")
    plt.grid()
    plt.xticks(range(0, 101, 5))
    plt.show()


def plotar_grafico_previsao_eolica(vento_atual):
    """
    Exibe a reta de regressão eólica com o ponto de previsão
    para a velocidade de vento atual anotado no gráfico.
    """
    energia_prevista = previsao_energia_eolica(vento_atual)
    a, b = regressao_eolica()

    plt.figure()  # garante figura nova a cada chamada
    x_reta = np.linspace(0, 30, 100)
    y_reta = a * x_reta + b

    plt.plot(x_reta, y_reta, zorder=2)
    plt.scatter(vento_atual, energia_prevista, color='blue', zorder=3)
    plt.annotate(f"Previsão: {energia_prevista:.2f} kWh", (vento_atual, energia_prevista),
                 textcoords="offset points", fontsize=6, xytext=(0, 10), ha='center')
    plt.xlabel("Velocidade do Vento (m/s)")
    plt.ylabel("Energia Gerada (kWh)")
    plt.title("Previsão de Energia Eólica Gerada vs Velocidade do Vento")
    plt.grid()
    plt.show()


def plotar_grafico_previsao_solar(radiacao_atual):
    """
    Exibe a reta de regressão solar com o ponto de previsão
    para a radiação atual anotado no gráfico.
    """
    energia_prevista = previsao_energia_solar(radiacao_atual)
    a, b = regressao_solar()

    plt.figure()  # garante figura nova a cada chamada
    x_reta = np.linspace(0, 100, 100)
    y_reta = a * x_reta + b

    plt.plot(x_reta, y_reta, zorder=2)
    plt.scatter(radiacao_atual, energia_prevista, color='orange', zorder=3)
    plt.annotate(f"Previsão: {energia_prevista:.2f} kWh", (radiacao_atual, energia_prevista),
                 textcoords="offset points", fontsize=6, xytext=(0, 10), ha='center')
    plt.xlabel("Radiação Solar (%)")
    plt.ylabel("Energia Gerada (kWh)")
    plt.title("Previsão de Energia Solar Gerada vs Radiação Solar")
    plt.grid()
    plt.xticks(range(0, 101, 5))
    plt.show()