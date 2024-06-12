import random

######### FUNÇÕES #########

def sorteio():
    valSorteados = []
    for i in range(5):
        valor = random.randint(0, 100)
        valSorteados.append(valor)
    return valSorteados

def calcularMedia(valores):
    menor = min(valores)
    maior = max(valores)
    media = sum(valores) / len(valores)
    return menor, maior, media

def main():
    valSorteados = sorteio()
    print("Valores sorteados:", valSorteados)

    menor, maior, media = calcularMedia(valSorteados)
    print("Menor valor sorteado:", menor)
    print("Maior valor sorteado:", maior)
    print("Média dos valores sorteados:", media)

############# PROGRAMA PRINCIPAL ############

main()
