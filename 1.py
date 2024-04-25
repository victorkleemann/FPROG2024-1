############### FUNÇÕES ###############
def divisivelPor2(numInt):
    if numInt % 2 == 0:
        numInt = True
        print(f'{numInt} = True')
    else:
        numInt = False
        print(f'{numInt} = False')

############### PROGRAMA PRINCIPAL ###############
num = int(input('Digite o valor desejado:'))
divisivelPor2(num)
