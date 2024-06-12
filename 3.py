############### FUNÇÕES ###############

def prepararPoção():
    opcao = ''
    while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5:
        print('-------------------------------------------------------------')
        print('      Poção                            Ingredientes      ')
        print('')
        print('1) Poção de cura                 Pó de Fenix(30g) Essencia celestial(20g)')
        print('                              Flores secas(20g) Lágrimas de Unicornio(10ml)')
        print('')
        print('2) Poção força da floresta       Orvalho Lunar(20ml) Flores secas(30g) Raiz de Dragão(30g)')
        print('')
        print('3) Poção Sabedoria da Riqueza    Essencia celestial(30ml) Pó de Fenix(50g)')
        print('4) Poção sorte no amor           Orvalho Lunar(10ml) Flores secas(50g) Lágrima de unicornio(5ml)')
        print('5) Poção malvada                 Elixir Amargo(10ml) Raiz de Dragão(15g)')
        print('')
        print('-------------------------------------------------------------')
        opcao = input('Digite a opção correspondente a poção desejada:')
        if opcao == "1":
            pocaoDeCura()
        elif opcao == 2:
            pocaoForcaDaFloresta
        elif opcao == 3:
            pocaoSabedoriaDaRiqueza()
        elif opcao == 4:
            pocaoSorteNoAmor()
        elif opcao == 5:
            pocaoMalvada
        else:
            print('Opção Inválida!')
    

def consultarIngredDisponiveis():
    print('---------------------------------------------')
    print(f'Pó de Fenix = {poDeFenix}')
    print(f'Essencia Celestial = {essenciaCelestial}')
    print(f'Raiz de Dragão = {raizDeDragao}')
    print(f'Orvalho Lunar = {orvalhoLunar}')
    print(f'Flores Secas = {floresSecas}')
    print(f'Elixir amargo = {elixirAmargo}')
    print(f'Lagrimas de Unicornio = {lagrimasDeUnicornio}')
    print('---------------------------------------------')

def pocaoDeCura():
    if poDeFenix < 30:
        print('Pó de fenix insuficiente')
    if essenciaCelestial < 20:
        print('Essencia celestial insuficiente')
    if floresSecas < 20:
        print('Flores secas insuficientes')
    if lagrimasDeUnicornio < 10:
        print('Lagrimas de unicornio insuficientes')
    if poDeFenix > 30  and essenciaCelestial > 20 and floresSecas > 20 and lagrimasDeUnicornio > 10:
        poDeFenix = poDeFenix - 30
        essenciaCelestial = essenciaCelestial - 20
        floresSecas = floresSecas - 20
        lagrimasDeUnicornio = lagrimasDeUnicornio - 10
        print('Você fez uma Poção de Cura!')

def pocaoForcaDaFloresta():
    if orvalhoLunar < 20:
        print('Orvalho Lunar insuficiente')
    if floresSecas < 30:
        print('Flores Secas insuficientes')
    if raizDeDragao < 30:
        print('Raiz de Dragão insuficiente')
    if orvalhoLunar > 30  and floresSecas > 20 and raizDeDragao > 20:
        orvalhoLunar = orvalhoLunar - 30
        raizDeDragao = raizDeDragao - 20
        floresSecas = floresSecas - 20
        print('Você fez uma Poção Força da Floresta!')

def pocaoSabedoriaDaRiqueza():
    if poDeFenix < 30:
        print('Pó de fenix insuficiente')
    if essenciaCelestial < 50:
        print('Essencia celestial insuficiente')
    if poDeFenix > 50  and essenciaCelestial > 20:
        poDeFenix = poDeFenix - 50
        essenciaCelestial = essenciaCelestial - 20
        print('Você fez uma Poção Sabedoria da riqueza!')

def pocaoSorteNoAmor():
    if floresSecas < 10:
        print('Flores secas insuficientes')
    if lagrimasDeUnicornio < 5:
        print('Lagrimas de unicornio insuficientes')
    if orvalhoLunar < 10:
        print('Orvalho Lunar Insuficiente!')
    if orvalhoLunar > 10  and floresSecas > 50 and lagrimasDeUnicornio > 5:
        orvalhoLunar = orvalhoLunar - 10
        floresSecas = floresSecas - 50
        lagrimasDeUnicornio = lagrimasDeUnicornio - 50
        print('Você fez uma Poção Sorte no Amor!')

def pocaoMalvada():
    if elixirAmargo < 10:
        print('Elixir Amargo insuficiente')
    if raizDeDragao < 15:
        print('Raiz de Dragão insuficiente')
    if elixirAmargo > 10  and essenciaCelestial > 15: 
        elixirAmargo = elixirAmargo - 10
        raizDeDragao = raizDeDragao  - 15
        print('Você fez uma Poção Malvada!')




############### PROGRAMA PRINCIPAL ###############
escolha = ""
poDeFenix = 100
essenciaCelestial = 50
raizDeDragao = 45
orvalhoLunar = 30
floresSecas = 200
elixirAmargo = 20
lagrimasDeUnicornio = 15

while escolha != '0':
    print('Olá Sr Alquimista!\nSelecione uma opção para continuar:\n(1) Preparar poção\n(2) Consultar ingredientes disponiveis\n(0) Sair')
    escolha = input('Digite a opção desejada: ')
    if escolha == '1':
        prepararPoção()
    elif escolha == '2':
        consultarIngredDisponiveis()
    elif escolha == '0':
        print('Saindo...')
    else:
        print('Opção inválida')

