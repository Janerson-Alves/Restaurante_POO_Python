#pegando as informações do restaurante.py e colocando aqui neste script, usando import
from restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.receber_avaliacao('GUI', 10) #como esta entre 1 e 5, esta nota não entra na média das notas do restaurante
restaurante_praca.receber_avaliacao('LAIS', 5)
restaurante_praca.receber_avaliacao('Emy', 2)
restaurante_praca.alternar_estado()

restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_mexicano.receber_avaliacao('CARLOS', 5)
restaurante_mexicano.receber_avaliacao('JOAO', 4)
restaurante_mexicano.receber_avaliacao('JOANA', 7)
restaurante_mexicano.alternar_estado()
restaurante_japones = Restaurante('Japa', 'Japonesa')
restaurante_japones.receber_avaliacao('CARLOS', 5)
restaurante_japones.receber_avaliacao('ELIAS', 5)
restaurante_japones.receber_avaliacao('GARRINCHA', 5)
def main():
    Restaurante.listar_restaurantes()
if __name__ == '__main__':
    main()