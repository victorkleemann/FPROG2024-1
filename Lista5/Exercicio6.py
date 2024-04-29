import random

###################### FUNÇÕES ######################

def openBox():
    item = random.choices(['Comum', 'Raro', 'Lendário'], weights=[0.8, 0.19, 0.01])[0]
    inventario[item] += 1
    print("-"*20)
    print(f"Você coletou 1 item {item}!")

def consultItens():
    print("Itens coletados:")
    for tipo, quantidade in inventario.items():
        print(f"Itens {tipo}: {quantidade}")

def menu():
    while True:
        print("-"*20)
        print("1 – Abrir uma caixa")
        print("2 – Consultar itens")
        print("0 - Sair")
        print("-"*20)
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            openBox()
        elif opcao == '2':
            consultItens()
        elif opcao == '0':
            print("Saindo...")
            pass
        else:
            print("Opção inválida!")

###################### PROGRAMA PRINCIPAL ###################### 

inventario = {
    'Comum': 0,
    'Raro': 0,
    'Lendário': 0}
menu()
