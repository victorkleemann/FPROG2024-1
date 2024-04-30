########### FUNÇÕES ###########
def calcMedia(notaA, notaB):
    media = (notaA + notaB) / 2
    return media

def verificarAprovacao(media):
    if media >= 6.0:
        return "APROVADO"
    else:
        return "REPROVADO"

def substituirNota(notaA, notaB, grauC, substituir):
    while substituir.upper() != 'A' and substituir.upper() != 'B':
        print("Opção inválida")
        substituir = input("Qual nota deseja substituir (A ou B)? ")

    if substituir.upper() == 'A':
        notaA = grauC
    elif substituir.upper() == 'B':
        notaB = grauC

    return notaA, notaB

def main():
    numAlunos = int(input("De quantos alunos será calculada a media? "))
    mediaTotal = 0

    for aluno in range(1, numAlunos + 1):
        print('')
        print(f"Aluno {aluno}:")
        notaA = float(input("Digite a nota para o grau A: "))
        notaB = float(input("Digite a nota para o grau B: "))
        media = calcMedia(notaA, notaB)
        aprovacao = verificarAprovacao(media)

        if aprovacao == "APROVADO":
            print("APROVADO")
        else:
            grauC = float(input("Digite a nota para o grau C: "))
            substituir = input("Qual nota deseja substituir (A ou B)? ")
            notaA, notaB= substituirNota(notaA, notaB, grauC, substituir)
            media = calcMedia(notaA, notaB)
            aprovacao = verificarAprovacao(media)
            print(aprovacao)
        
        mediaTotal += media

    mediaGeral = mediaTotal / numAlunos
    print(f"A média geral dos alunos é: {mediaGeral:.2f}")

########### PROGRAMA PRINCIPAL ###########
main()
