import random

############## FUNÇÕES ##################
def gerarToupeiras(): #Função para gerar as toupeiras em posições aleatórias
    array = [['-' for i in range(4)] for i in range(4)] # Matriz cheia de posições vazias
    for o in range(4):
        while True:
            x = random.randint(0,3) # seleciona uma linha aleatória
            y = random.randint(0,3) # seleciona uma coluna aleatoria
            if array [x][y] == '-':  
                array[x][y] = 'T'
                break
    return array #Retorna a array com as toupeiras posicionadas

############## PROGRAMA PRINCIPAL ################
for h in range(1,4): #Loop que vai formar as 3 gerações
    print(f"Geração {h}: ")
    toupeiras = gerarToupeiras()
    for u in toupeiras:
        print('  '.join(u))
    print()