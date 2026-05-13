from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

import matplotlib.pyplot as plt
import numpy as np

from modules.modulos import Colonia

def historico_dados_eolica(): #Criação da função que irá armazenar os dados históricos de criação de energia eólica.
 
 """
 30 = velocidade máxima do vento para geração de energia eólica
 20.00 = capacidade máxima de energia eólica armazenada
 0.66 = a cada 1 m/s de vento, a energia gerada é de 0.66 (20/30) da velocidade do vento, ou seja, 0.66 * velocidade_vento = energia_gerada.
 """
 
 nome = "Eólica"
 dia_de_teste = [1, 2, 3, 4, 5, 6]
 velocidade_vento = [28, 12, 8, 16, 20, 18] #<- velocidade máxima 30 m/s
 energia_gerada = [18.48, 7.92, 5.28, 10.56, 13.2, 11.88] # <- a cada 1 m/s de vento, a energia gerada é de 0.66 (20/30) da velocidade do vento, ou seja, 0.66 * velocidade_vento = energia_gerada.

 """
 Coloquei os valores de energia_gerada como float, pois a energia nunca é exata, e sim uma aproximação, e o tipo float é mais adequado para representar esse tipo de dado. 
 Mas ainda é coerente com as regras do Aelton, visto que ele apenas limita o máximo do armazenamento em 20 (int), e não ultrapassa esse limite.
 """
 return  nome, velocidade_vento, energia_gerada



def historico_dados_solar(): #Criação da função que irá armazenar os dados históricos de criação de energia solar.
 
 """
    100 = radiação solar máxima 
    30.00 = capacidade máxima de energia solar armazenada
    0.3 = a cada 1% de radiação solar, a energia gerada é de 0.3 (30/100) da radiação solar, ou seja, 0.3 * radiacao_solar = energia_gerada.
 """

 nome = "Solar"
 dia_de_teste = [1, 2, 3, 4, 5, 6]
 radiacao_solar = [90, 70, 50, 80, 100, 60] # <- radiação solar máxima 100 
 energia_gerada = [27.00, 21.00, 15.00, 24.00, 30.00, 18.00] # <- a cada 1% de radiação solar, a energia gerada é de 0.3 (30/100) da radiação solar, ou seja, 0.3 * radiacao_solar = energia_gerada.

 return  nome, radiacao_solar, energia_gerada


def regressao_eolica():

 nome,velocidade_vento, energia_gerada = historico_dados_eolica() # <- Chama a função historico_dados_eolica para obter os dados históricos de criação de energia eólica.

 coeficientes = np.polyfit(velocidade_vento, energia_gerada, 1) # <- chama a função np.polyfit para calcular os coeficientes a (inclinação da reta) e b (ponto de partida da reta) a partir de X (causa) e Y (efeito) 
 

 return coeficientes[0], coeficientes[1] # <- retorna os coeficientes a e b

def regressao_solar():
 
 nome, radiacao_solar, energia_gerada = historico_dados_solar() 

 coeficientes = np.polyfit(radiacao_solar, energia_gerada, 1)

 return coeficientes[0], coeficientes[1]