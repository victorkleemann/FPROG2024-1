import random

positivos = 0
negativos = 0

for _ in range(20):
    numero = random.randint(-10, 10)
    if numero > 0:
        print(numero, "- POSITIVO")
        positivos += 1
    elif numero < 0:
        print(numero, "- NEGATIVO")
        negativos += 1
    else:
        print(numero, "- NULO")

print("-"*20)
print("\nQuantidade de números positivos:", positivos)
print("Quantidade de números negativos:", negativos)
print("-"*20)
