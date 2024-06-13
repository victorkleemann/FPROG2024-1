#cria um arquivo vazio se não existir ou APAGA o conteudo de um arquivo existente para escrita
nomeArquivo = 'arquivo.txt'

a = open('arquivo.txt', 'w')

# criaa um arquivo vazio se não existir ou MANTEM o conteudo de um arquivo
#a = open('arquivo.txt', 'a')

# cria um arquivo se não existir,e se exitir imprime um imagem de erro
#a = open('arquivo.txt', 'x')



# Escreve um texto em um arquivo
a.write('arquivo')

# fecha um arquivo
a.close()
#
#a.write()


