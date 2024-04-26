from modelos.avaliacao import Avaliacao

class Restaurante:
    """Representa um restaurante e suas características."""
    restaurantes = []
    # Inicialização do construtor
    def __init__(self, nome, categoria):

        """
        Inicializa uma instância de Restaurante.

        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante.
        """
        self._nome = nome.title() # Title = Todos os nomes começam com a letra maiscula
        self._categoria = categoria
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    
    def __str__(self):
        """Retorna uma representação em string do restaurante."""
        return f'{self._nome} | {self._categoria}'
    
    # Para cada restaurante dentro da lista restaurantes, me traga essas informações
    @ classmethod
    def listar_restaurantes(cls):
        """Exibe uma lista formatada de todos os restaurantes."""
        print(f'{'Nome do restaurante' .ljust(25)} | {'Categoria' .ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    def alternar_estado(self):
        """Alterna o estado de atividade do restaurante."""
        self._ativo = not self._ativo

    @property
    def ativo(self):
        """Retorna um símbolo indicando o estado de atividade do restaurante."""
        return '✔️' if self._ativo else '❌'
    

    def receber_avaliacao(self, cliente, nota):
        """
        Registra uma avaliação para o restaurante.

        Parâmetros:
        - cliente (str): O nome do cliente que fez a avaliação.
        - nota (float): A nota atribuída ao restaurante (entre 1 e 5).
        """
        if (0 < nota <= 5):
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        """Calcula e retorna a média das avaliações do restaurante."""
        if (not self._avaliacao):
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao) # para cada avaliação dentro da nossa lista de avaliacao, pega apenas a nota e soma
        quantidade_de_avaliacoes = len(self._avaliacao) # leia a quantidade de avaliacões que tem no array
        media = round(soma_das_notas / quantidade_de_avaliacoes, 1) # faça a média de avaliações
        return media # retorna a media