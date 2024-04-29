
n = int(input("Digite a quantidade de números a serem lidos: "))
soma = 0
for _ in range(n):
    numero = float(input("Digite um número: "))
    soma += numero

print("A soma dos números lidos é:", soma)

