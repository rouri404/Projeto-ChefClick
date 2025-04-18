from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'gourmet')
restaurante_praca.receber_avaliacao('Gabriel', 10)
restaurante_praca.receber_avaliacao('Felipe', 7)
restaurante_praca.receber_avaliacao('Julia', 5)

# restaurante_mexicano = Restaurante('mexican food', 'mexicana')
# restaurante_japones = Restaurante('japa', 'japonesa')

#restaurante_mexicano.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()