class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._ativo = False     # O 'underline' serve como um privatizador de atributos
        Restaurante.restaurantes.append(self)
    
    def __str__(self):      
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(15)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(15)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

restaurante_praca = Restaurante('praça', 'gourmet')
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante('pizza express', 'italiana')

Restaurante.listar_restaurantes()