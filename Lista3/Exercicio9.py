# Não entendi 100% o enunciado...Fiz do jeito que achei correto. Seja o que Deus quiser :)

cotDol = float(input('Digite a cotação do dolar: '))
cotEur = float(input('Digite a cotação do euro: '))

print('1) Converter de Real para Euro \n2) Converter de Real para Dólar \n3) Converter de Euro para Dólar \n4) Converter de Euro para Real \n5) Converter de Dólar para Euro \n6) Converter de Dólar para Real')

opc = input('Digite o numero referente a sua escolha entre uma das opções acima: ')

if opc == '1':
    valorReal = float(input("Digite o valor em Real: "))
    valorRealEur = valorReal / cotEur
    print(valorRealEur)
elif opc == '2':
    valorReal = float(input("Digite o valor em Real: "))
    valorRealDol = valorReal / cotDol
    print(valorRealDol)
elif opc == '3':
    valorEuro = float(input("Digite o valor em Euro: "))
    valorEurDol = valorEuro / 0,93
    print(valorEurDol)
elif opc == '4':
    valorEuro = float(input("Digite o valor em Euro: "))
    valorEurReal = valorEuro * cotEur
    print(valorEurReal)
elif opc == '5':
    valorDol = float(input("Digite o valor em Dólar: "))
    valorDolEur = valorDol * 1.08
    print(valorDolEur)
elif opc == '6':
    valorDol = float(input("Digite o valor em Dólar: "))
    valorDolReal = valorDol * cotDol
    print(valorDolReal)
else:
    print('Opção inválida')

# certo: 1,2,4,6
    


