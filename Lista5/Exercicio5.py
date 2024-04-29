################# FUNÇÕES ################# 
def somar(num1,num2):
    num1 = int(input('Digite o primeiro valor que deseja somar:'))
    num2 = int(input('Digite o segundo valor que deseja somar:'))
    result = num1 + num2
    return result

def subtrair(num1,num2):
    num1 = int(input('Digite o primeiro valor que deseja subtrair:'))
    num2 = int(input('Digite o segundo valor que deseja subtrair:'))
    result = num1 - num2
    return result

def multiplicar(num1,num2):
    num1 = int(input('Digite o primeiro valor que deseja multiplicar:'))
    num2 = int(input('Digite o segundo valor que deseja multiplicar:'))
    result = num1 * num2
    return result

def dividir(num1,num2):
    while True:
        num1 = int(input('Digite o divisor:'))
        num2 = int(input('Digite o dividendo:'))
        if num1 != 0 and num2 != 0:
            result = num1 / num2
            False
            return result
        else:
            print("Zero não pode ser dividido!")

def menu(opc):
    print("-"*20)
    print("")
    print("CALCULADORA")
    print("")
    print("-"*20)
    print("Digite a opção relacionada a operação que deseja fazer:\n(1) Somar \n(2) Subtrair \n(3) Multiplicar \n(4) Dividir \n(0) Sair")
    print("-"*20)


################# PROGRAMA PRINCIPAL ################# 
num1 = ''
num2 = ''
opc = ''
while opc != 0:
    menu(opc)
    opc = int(input('Digite a opção relacionada a operação que deseja fazer:'))
    if opc == 1:
        result = somar(num1,num2)
        print("-"*20)
        print(f"Resultado da soma: {result}")
        print("-"*20)
    elif opc == 2:
        result = subtrair(num1,num2)
        print("-"*20)
        print(f"Resultado da subtração: {result}")
        print("-"*20)
    elif opc == 3:
        result = multiplicar(num1,num2)
        print("-"*20)
        print(f"Resultado da multiplicação: {result}")
        print("-"*20)
    elif opc == 4:
        result = dividir(num1,num2)
        print("-"*20)
        print(f"Resultado da divisão: {result}")
        print("-"*20)
    elif opc == 0:
        print("Saindo...")
    else:
        print("Opção Inválida!")
