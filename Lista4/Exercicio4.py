def numDiv(divisor, inicio_intervalo, final_intervalo):
    numeros_divisiveis = []
    for numero in range(inicio_intervalo, final_intervalo + 1):
        if numero % divisor == 0:
            numeros_divisiveis.append(numero)
    return numeros_divisiveis

def main():
    divisor = int(input("Entre com o valor do divisor: "))
    inicio_intervalo = int(input("Início do intervalo: "))
    final_intervalo = int(input("Final do intervalo: "))

    divisives = numDiv(divisor, inicio_intervalo, final_intervalo)
    
    print(f"Números divisíveis por {divisor} no intervalo de {inicio_intervalo} a {final_intervalo}:")
    print(divisives)

if __name__ == "__main__":
    main()
