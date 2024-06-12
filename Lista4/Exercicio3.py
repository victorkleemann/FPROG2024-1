
while True:
    print("-"*40)
    num = int(input("Entre com um número (de 1 a 9): "))
    print("-"*40)
    
    if 1 <= num <= 9:
        print(f"Tabuada do {num}:")
        for i in range(1, 11):
            result = num * i
            print(f"{num} x {i} = {result}")
            print("-"*40)
    else:
        print("Número inválido. Por favor, entre com um número de 1 a 9.")
    
    opcao = input("Calcular outro número (s/n)? ")
    if opcao != 'S':
        break
