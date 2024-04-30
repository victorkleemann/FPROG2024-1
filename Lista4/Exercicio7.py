############ FUNÇÕES ##############

def findName():
    nomes = []
    for i in range(1,6):
        nome = input(f"Digite o {i}º nome: ")
        nomes.append(nome)
    firstName = min(nomes)
    return firstName

def main():
    firstName = findName()
    print("O primeiro nome em ordem alfabética é:", firstName)

############ PROGRAMA PRINCIPAL ############

main()
