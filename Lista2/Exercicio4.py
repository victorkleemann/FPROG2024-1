A = float(input('Digite sua nota para o grau A:'))
B = float(input('Digite sua nota para o grau B:'))

mediaFinal = (A * (1/3)) + (B * (2/3))
mediaFinal_limited = round(mediaFinal, 2)

print('A sua média final foi: ',mediaFinal_limited)
