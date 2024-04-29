################# FUNÇÕES #################
def tabuada(n):
    for i in range(1,11):
        res = n * i
        print(n,'x', i, '=', res)


################# PROGRAMA PRINCIPAL #################

for i in range(1,11):
    tabuada(i)
    print('------------------')
