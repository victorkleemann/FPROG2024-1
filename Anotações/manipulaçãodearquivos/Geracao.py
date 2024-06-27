#cria um arquivo vazio se não existir ou APAGA o conteudo de um arquivo existente para escrita
nomeArquivo = 'arquivo.txt'
texto = 'atstwwfwd'
numero = 15

a = open('arquivo.txt', 'w')

# cria um arquivo vazio se não existir ou MANTEM o conteudo de um arquivo
#a = open('arquivo.txt', 'a')

# cria um arquivo se não existir,e se exitir imprime um imagem de erro
#a = open('arquivo.txt', 'x')



# Escreve um texto em um arquivo
a.write('arquivo')

# fecha um arquivo
a.close()

# Escreve o conteudo de uma variavel de texto em um arquivo:
a.write(texto)

# Escreve o conteudo de uma variavel que não seja de texto em um arquivo
a.write(str(texto))

