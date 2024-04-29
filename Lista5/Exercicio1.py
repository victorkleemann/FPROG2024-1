################# FUNÇÕES #################

def cumprimentar(nome):
    print('Olá!',nome,)


################# PROGRAMA PRINCIPAL #################

#nome1 = input('Usuario 1, digite seu nome: ')
#cumprimentar(nome1)

#nome2 = input('Usuario 2, digite seu nome: ') 
#cumprimentar(nome2)

for i in range(5):
    print('Usuário',i+1, end = "")
    nome2 = input(', digite seu nome: ') 
    cumprimentar(nome2)