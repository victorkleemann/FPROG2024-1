import random
import os
#adicionar o comando do os depois

posHamster1 = 0
posHamster2 = 0

#0 - nignuem venceu ainda
#1 - hamster 1 venceu
#2 - hamster 2 venceu
#3 - empate

vencedor = 0 

while vencedor == 0: #continua a corrida
    #limpando a tela do console
    os.system('cls' if os.name == 'nt' else 'clear')
    #fazendo a movimentação do ham1
    nroSorteado = random.randint(1,5) #sorteia um num entre 1 e 5
    # aplicar as regras da tabela na posicao do ham1
    if nroSorteado == 1:
        posHamster1 = posHamster1 + 1
    elif nroSorteado == 2:
        posHamster1 = posHamster1 + 2
    elif nroSorteado == 3:
        #nao se mexe
        pass
    elif nroSorteado == 4:
        posHamster1 = posHamster1 - 1
    else:
        posHamster1 = posHamster1 - 2
    #garantir que não existe posição negativa
    if posHamster1 < 0:
        posHamster1 = 0
    elif posHamster1 > 12:
        posHamster1 = 12

    #fazendo a movimentação do ham2
    nroSorteado = random.randint(1,5) #sorteia um num entre 1 e 5
    # aplicar as regras da tabela na posicao do ham1
    if nroSorteado == 1:
        posHamster2 = posHamster2 + 1
    elif nroSorteado == 2:
        posHamster2 = posHamster2 + 2
    elif nroSorteado == 3:
        #nao se mexe
        pass
    elif nroSorteado == 4:
        posHamster2 = posHamster2 - 1
    else:
        posHamster2 = posHamster2 - 2
    #garantir que não existe posição negativa
    if posHamster2 < 0:
        posHamster2 = 0
    elif posHamster2 > 12:
        posHamster2 = 12
    
    #Testa quem venceu
    if posHamster1 == 12:
        vencedor = 1 # hamster 1 venceu
    if posHamster2 == 12 and vencedor == 0:
        if vencedor == 0:
            vencedor = 2 # hamster 2 venceu
        else:
            vencedor = 3 #empate
    
    #imprime na tela o status da corrida
    print('Hamster 1:',end= '')
    for n in range(posHamster1):
        print('*',end = '')
    print() # quebra de linha

    print('Hamster 2:',end = '')
    for n in range(posHamster2):
        print('*',end ='')
    print() # quebra de linha
    print('------------------------------')

#imprime quem ganhou
if vencedor == 1:
    print('Hamster 1 venceu')
elif vencedor == 2:
    print('Hamster 2 venceu')
else:
    print('Houve um impate')


    
        

    
