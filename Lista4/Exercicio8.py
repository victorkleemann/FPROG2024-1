########### FUNÇÕES ###############

def calcFatorial(num):
    fatorial = 1
    for i in range(1, num + 1):
        fatorial *= i
    return fatorial

def main():
    continuar = True
    while continuar == True:
        numero = int(input("Entre com um número: "))
        resultado = calcFatorial(numero)
        print(f"O fatorial de {numero} é {resultado}")
        opcao = input("Calcular outro número (s/n)? ")
        if opcao != 's':
            continuar = False

######### PROGRAMA PRINCIPAL ##########

main()
