import random 

numeroSorteado = random.randint(1,3)

#####################

numeroLido = int(input('Digite um numero de 1 a 3: '))
if numeroLido == numeroSorteado:
    print('você acertou!!!')
else:
    print('errou!! O numero sorteado era',numeroSorteado)