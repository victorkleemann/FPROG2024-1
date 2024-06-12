import random

################# FUNÇÕES ################# 

def sorteio(inicio, fim):
    return random.randint(inicio, fim)

################# PROGRAMA PRINCIPAL ################# 

inicio = 1
fim = 10
numSorteado = sorteio(inicio, fim)
print(f"Número sorteado:{numSorteado}")
