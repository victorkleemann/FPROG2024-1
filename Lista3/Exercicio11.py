############## FUNÇÕES ##############
def calc(value):
    ceds = (100,50,20,10,5,1)
    result = {}
    for ced in ceds:
        if value >= ced:
            result[ced] = value // ced
            value %= ced
    return result

############## PROGRAMA PRINCIPAL ##############
value = int(input('Digite o valor desejado:'))

result = calc(value)

for ced,qnt in result.items():
    print(f"{qnt} notas de R${ced}")
