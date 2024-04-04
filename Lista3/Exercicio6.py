a = input('Esscolha entre par ou impar: ')
b = int(input('Agora escolha um número entre 0 e 5:'))

import random 

numSorteado = random.randint(0,5)

b = numSorteado + b

if a == 'par' and b % 2 or a == 'impar' and b == 3:
    print('Parabéns!! Você venceu.')
else:
    print('O programa venceu!!')
