from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'gourmet')
restaurante_praca.receber_avaliacao('Gabriel', 5)
restaurante_praca.receber_avaliacao('Felipe', 3.5)
restaurante_praca.receber_avaliacao('Julia', 2.5)

restaurante_mexicano = Restaurante('mexican food', 'mexicana')
restaurante_mexicano.receber_avaliacao('Maria', 3)
restaurante_mexicano.receber_avaliacao('André', 4)
restaurante_mexicano.receber_avaliacao('Camila', 4.5)
restaurante_mexicano.alternar_estado()

restaurante_japones = Restaurante('japa', 'japonesa')

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()