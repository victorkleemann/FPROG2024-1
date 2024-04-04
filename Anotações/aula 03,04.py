cont = 0
senha = '789'
senhacorreta = False
root = ''

while (cont < 3 and senhacorreta == False):
    root = input('Digite a senha para o usuario "root":')
    cont = cont + 1
    if root == senha:
        senhacorreta == True
        print('Senha correta! Entrou no sistema!')
    else:
        print('Senha incorreta! Você ainda possui',3-cont,'tentativas')
    
