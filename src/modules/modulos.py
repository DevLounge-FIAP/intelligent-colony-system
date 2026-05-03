'''
Módulo de Regras Basicas - Classe Modulo
Responsável por: Aelton

Parte estrutural para definição dos módulos da base Marciana.
Define a estrutura da base em solo e comportamente de cada módulo.
'''


class Modulo:
    """
    Representa um módulo físico da base.
    """
    def __init__(self, id_nome: str, tipo: str, funcao: str, criticidade: int, consumo: int):
        '''
        Args:
            id_nome: Identificador único (ex: 'SUP-01')
            tipo: Categoria do módulo ('Medico', 'Logistica', 'Engenharia', 'Laboratorio')
            funcao: Descrição da função ('Suporte à Vida', 'Pesquisa', 'Controle de Energia')
            criticidade: 1 (pouco essencial) a 5 (insubstituível)
            consumo: Energia consumida por hora (valor absoluto)
        '''
        self.id_nome = id_nome
        self.tipo = tipo
        self.funcao = funcao
        self.criticidade = criticidade
        self.consumo = consumo
        self.status = True  # True = Ligado, False = Desligado

    def __repr__(self):
        estado = "Ligado" if self.status else "Desligado"
        return f"Módulo: {self.id_nome} ({self.funcao}) [{estado}] Criticidade:{self.criticidade}"
    
class Sistema:
    '''Classe que representa um sistema de energia (geração ou armazenamento)'''
    def __init__(self, nome: str, capacidade_max: int, geracao_atual: int = 0):
        '''
        Args:
            nome: Nome do Sistema.
            capacidade_max (int): Capacidade maxima do sistema.
            geracao_atual (int): Geração atual do sistema.
        '''
        self.nome = nome
        self.capacidade_max = capacidade_max
        self.geracao_atual = geracao_atual


class SistemaSolar(Sistema):
    '''Painéis Solares.'''
    def __init__(self, nome: str, capacidade_max: int, geracao_atual: int = 0):
        super().__init__(nome, capacidade_max, geracao_atual)
        self.tipo = "Solar"

class SistemaEolico(Sistema):
    '''Turbinas Eólicas'''
    def __init__(self, nome: str, capacidade_max: int, geracao_atual: int = 0):
        super().__init__(nome, capacidade_max, geracao_atual)
        self.tipo = "Eolica"

class SistemaReserva(Sistema):
    '''Banco de baterias (armazenamento).'''
    def __init__(self, nome, capacidade_max, carga_atual = 0):
        super().__init__(nome, capacidade_max, carga_atual)
        self.tipo = "Reserva"

class Colonia:
    '''
    Contexto central da colônia. Agrega todos os módulos e sistemas.
    É o objeto de entrada para todas as funções de decisão.
    '''
    def __init__(self):
        self.modulos = [] #Lista de objetos Módulo
        self.sistemas = [] #Lista de sistemas (Solar, Eolico e Reserva)
        self.vento = 0 #Velocidade do Vento
        self.radiacao_solar = 0 #Irradiância Solar

#--------------------- Métodos de consulta ------------------

    def energia_disponivel_total(self) -> int:
        '''Soma a geração atual de todos os sistemas (inclui a reserva).'''
        return sum(s.geracao_atual for s in self.sistemas)
    
    def capacidade_total(self) -> int:
        '''Soma a capacidade total de todos os sistemas'''
        return sum(s.capacidade_max for s in self.sistemas)
    
    def nivel_energia_percentual(self) -> float:
        '''
        Basicamente retorna a capacidade total em porcentagem.
        Exemplo: Se total disponivel = 40 e capacidade total = 100, retorna 40.0 (que é 40 em %)
        '''
        capacidade = self.capacidade_total() #Aqui é só dizendo que a variavel capacidade é igual a capacidade, fica mais fácil de escrever.
        '''Poderia ter feito assim:
        if self.capacidade_total() == 0:
            return 0.0
        return (self.energia_disponivel_total() / self.capacidade_total()) * 100
        Entendeu?? então segue o baile.
        '''
        if capacidade == 0:
            return 0.0
        return (self.energia_diponivel_total() / capacidade) * 100
    def consumo_total(self) -> int:
        '''Soma o consumo apenas dos módulos que estão ligadis.'''
        return sum(m.consumo for m in self.modulos if m.status) #Aqui é legal pois ele retorna o consumo somente se o status tiver ligado.
    
    def modulos_ligados(self) -> list:
        '''Lista de módulos ativos no momento.'''
        return [m for m in self.modulos if m.status] #Bom como já diz retorna em uma lista só modulos ligados
    
    def modulos_desligaveis(self) -> list:
        '''Lista de módulos ativos com criticidade < 4 (podem ser delisgados em emergência).'''
        return [m for m in self.modulos if m.status and m.criticidade < 4]