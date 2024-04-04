notaA = float(input('Digite a sua nota referente ao grau A: '))
notaB = float(input('Digite a sua nota referente ao grau B: '))
media = (notaA * (1/3)) + (notaB * (2/3))

if media >=6 and media <=10:
    print('Prabéns! Você está aprovado!')
elif media < 6:
    print('Que pena! Você está de recuperação.')
    recuperacao = True
if recuperacao == True:
     ans = input('Você gostaria de substituir qual grau? A ou B?: ')
     if ans == 'A':
         notaC = float(input('Digite sua nota para o grau C:'))
         media = (notaC * (1/3)) + (notaB * (2/3))
     elif ans == 'B':
         notaC = float(input('Digite sua nota para o grau C:'))
         media = (notaC * (1/3)) + (notaB * (2/3))
     if media >=6 and media <=10:
         print('Parabéns!Você foi aprovado!')
     elif media < 6:
         print('Você foi reprovado!')