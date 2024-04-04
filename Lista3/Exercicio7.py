a = float(input('Digite o valor do seu salário para calcular o desconto: '))
desconto = a * 0.11

if desconto <= 318.20:
    print('O valor do desconto equivale a R$',desconto)
else:
     print('O valor do desconto equivale a R$318,20')