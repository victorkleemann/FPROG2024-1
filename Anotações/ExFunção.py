#Area com a implementação das funções que o codigo vai usar
def minhaFuncao():
    # Comandos que serão executados quando a função "minhaFuncao" for chamada
    print('Olá funções!')

def funcaoComParametros(p1,p2,p3):
    print('Olá função com parametros')
    print('Parametro 1: ',p1)
    print('Parametro 2: ',p2)
    print('Parametro 3: ',p3)

######## PROGRAMA PRINCIPAL ########
print('Olá')

minhaFuncao()

funcaoComParametros(1, 2, 3)
funcaoComParametros(1, 2.2,"c")
a = 'namibia'
b = input('Digite um bagulho:')
funcaoComParametros(a, b, True)