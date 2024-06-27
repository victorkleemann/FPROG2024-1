import random

################ FUNÇÕES ###################
def shuffle(matriz):
    n = len(matriz)
    for i in range(n):
        x, y = random.sample(range(n), 2) #Sorteia dois índices
        matriz[x], matriz[y] = matriz[y], matriz[x] #Embaralha os elementos


###################### PROGRAMA PRINCIPAL ########################
array = ['a', 'b', 'c', 'd', 'e']
print("Array original:", array)

shuffle(array)
print("Array embaralhada:", array)
