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
            capacidade_max (int): Capacidade maxima de geração do sistema do sistema.
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
        self.vento = 0.0 #Velocidade do Vento
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
        capacidade = self.capacidade_total()
        if capacidade == 0:
            return 0.0
        return (self.energia_disponivel_total() / capacidade) * 100

    def consumo_total(self) -> int:
        '''Soma o consumo apenas dos módulos que estão ligados.'''
        return sum(m.consumo for m in self.modulos if m.status)
    
    def modulos_ligados(self) -> list:
        '''Lista de módulos ativos no momento.'''
        return [m for m in self.modulos if m.status]
    
    def modulos_desligaveis(self) -> list:
        '''Lista de módulos ativos com criticidade < 4 (podem ser desligados em emergência).'''
        return [m for m in self.modulos if m.status and m.criticidade < 4]

    def modulos_por_prioridade(self) -> tuple[list, list, float]:
        '''
        Planeja quais módulos permanecem ativos com base na energia disponível.
        Ordena os módulos por criticidade decrescente e aplica estratégia first-fit:
        o primeiro módulo que não couber na energia restante encerra a alocação,
        e todos os subsequentes (mesmo que individualmente coubessem) são marcados
        como desligados. Isso garante que módulos de maior criticidade sempre
        tenham prioridade absoluta sobre os de menor criticidade.

        Retorna:
            modulos_ativos: lista de módulos que permanecem ligados no plano
            modulos_desligados: lista de módulos a serem desligados
            energia_restante: energia disponível após alocar os módulos ativos
        '''
        energia_disponivel = self.energia_disponivel_total()
        modulos_ordenados = sorted(
            enumerate(self.modulos),
            key=lambda item: (-item[1].criticidade, item[0])
        )

        modulos_ativos = []
        modulos_desligados = []
        energia_restante = energia_disponivel
        bloqueado = False

        for _, modulo in modulos_ordenados:
            if not bloqueado and modulo.consumo <= energia_restante:
                modulos_ativos.append(modulo)
                energia_restante -= modulo.consumo
            else:
                bloqueado = True
                modulos_desligados.append(modulo)

        return modulos_ativos, modulos_desligados, energia_restante