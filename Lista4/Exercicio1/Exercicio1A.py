##### LETRA A #####
i = 0
while i <= 99:
    i = i + 1
    print(i)

##### LETRA B #####
i = 0
for i in range(20,52,2):
    print(i)

##### LETRA C #####
i = 0
for i in range(70,25,-2):
    print(i)

##### LETRA D #####
i = 0
for i in range(95,24,-1):
    if i % 2 != 0:
        print(i)

##### LETRA E #####

soma = 0
for i in range(1, 16):
    numero = float(input(f"Digite o {i}º número: "))
    soma += numero

media = soma / 15

print("A soma dos números é:", soma)
print("A média dos números é:", media)

##### LETRA F #####
pares = 0
impares = 0

for _ in range(10):
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Quantidade de números pares:", pares)
print("Quantidade de números ímpares:", impares)
