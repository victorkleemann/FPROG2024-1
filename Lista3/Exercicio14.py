#################### FUNÇÕES ####################
def ValorPlano(conv, dep):
     baseValue = 300
     depValue = 0
    
     for old in dep:
        if old < 10:
            depValue += 100
        elif 10 <= old <= 30:
            depValue += 220
        elif 31 <= old <= 60:
            depValue += 395
        elif old > 60:
            depValue += 480
     return baseValue + depValue

#################### PROGRAMA PRINCIPAL ####################

oldConv = int(input("Digite a idade do conveniado: "))
numDep = int(input("Digite o número de dependentes: "))

oldDep = []
for i in range(numDep):
    old = int(input(f"Digite a idade do dependente {i + 1}: "))
    oldDep.append(old)

total = ValorPlano(oldConv, oldDep)
print(f"O valor total a ser pago é: R${total}")
    