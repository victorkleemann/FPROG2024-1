a = float(input('Digite o valor do produto: '))

x = a * 0.45
y = a * 0.35
z = a * 0.25

valorA = a + x
valorB = a + y
valorC = a + z

if a <= 20:
    print('O valor da sua venda será de R$',valorA)
elif a <= 50:
    print('O valor da sua venda será de R$',valorB)
elif a > 50:
    print('O valor da sua venda será de R$',valorC)