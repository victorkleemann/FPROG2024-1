############### FUNÇÕES ############### 
def mediaUnisinos(grauA,grauB):
    media = (grauA + 2*grauB) / 3.0
    media2 = (grauA * (1/3) + grauB * (1/2))
    return media   

############### PROGRAMA PRINCIPAL ###############

grauA = float(input('Digite a sua média do grau A:')) 
grauB = float(input('Digite a sua média do grau B:'))
grauFinal = mediaUnisinos(grauA, grauB)
print('A sua média é',grauFinal)