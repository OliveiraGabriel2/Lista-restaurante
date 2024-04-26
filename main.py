from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Gabriel', 4)
restaurante_praca.receber_avaliacao('Lais', 5)
restaurante_praca.receber_avaliacao('Jordan', 3)

restaurante_italian = Restaurante('italian', 'Pizzeria')
restaurante_italian.receber_avaliacao('Gabriel', 4)
restaurante_italian.receber_avaliacao('Lais', 5)
restaurante_italian.receber_avaliacao('Jordan', 3)

restaurante_vettor = Restaurante('vettor', 'Francêsa')
restaurante_vettor.receber_avaliacao('Jordan', 3)
restaurante_vettor.receber_avaliacao('Jordan', 5)
restaurante_vettor.receber_avaliacao('Jordan', 4)


def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()