import random

############# FUNÇÕES #############
def sorteio(inicio,fim):
    random.randint(inicio,fim)


############# PROGRAMA PRINCIPAL #############
inicio = int(input('Digite um valor para o inicio:'))
fim = int(input('Digite um valor para o fim:'))

sorteio(inicio,fim)
