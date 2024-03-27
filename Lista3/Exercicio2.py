A = int(input('Digite o primeiro valor da soma: '))
B = int(input('Digite o segundo valor da soma: '))
C = int(input('Digite o terceiro valor da soma: '))

answer = A + B + C

if A + B < A + C:
    print('A soma de A + B é menor que A + C')
else:
    print('A soma de A + B é maior que A + C')
