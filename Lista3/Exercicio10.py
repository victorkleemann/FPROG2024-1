ans = int(input(' As faces disponíveis são: 4, 6, 8, 10, 12 ou 16. Digite o numero de faces que deseja:'))

import random

if ans == 4:
    dice = random.randint(1,4)
    print(dice)
elif ans == 6:
    dice = random.randint(1,6)
    print(dice)
elif ans == 8:
    dice = random.randint(1,8)
    print(dice)
elif ans == 10:
    dice = random.randint(1,10)
    print(dice)
elif ans == 12:
    dice = random.randint(1,12)
    print(dice)
elif ans == 16:
    dice = random.randint(1,16)
    print(dice)
else:
    print('Opção Inválida!')
