old = int(input('Digite a idade do jogador para definir a categoria: '))

if old == 5 or old == 6 or old == 7:
    print('A categoria do jogador será Infantil A')
elif old == 8 or old == 9 or old == 10:
    print('A categoria do jogador será Infantil B')
elif old == 11 or old == 12 or old == 13:
    print('A categoria do jogador será Juvenil A')
elif old >= 14 and old <= 17:
    print('A categoria do jogador será Juvenil B')
elif old >= 18:
    print('A categoria do jogador será Sênior ')
else:
    print('Opção inválida!')