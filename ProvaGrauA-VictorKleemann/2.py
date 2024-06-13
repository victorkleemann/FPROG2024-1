############### FUNÇÕES ###############
def divisivelPorN(num1,num2):
    divisivel = ''
    if num1 % num2 == 0:
        divisivel = True
        print(f'{divisivel}')
    elif num2 == 0:
        print('Opcão inválida! Não é possível dividir por 0!')
    else:
        divisivel = False
        print(f'{divisivel}')


############### PROGRAMA PRINCIPAL ###############
num1 = int(input('Digite o divisor:'))
num2 = int(input('Digite o dividendo:'))

divisivelPorN(num1,num2)

