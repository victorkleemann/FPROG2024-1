import csv

arquivoCSV = open('ex.csv')
leitor = csv.reader(arquivoCSV,delimiter=';')
data = list(leitor)
arquivoCSV.close()

print(data)

playlist = [] # variavel que ai armazenar nossos dados tratados

# percorrer linha a linha, coluna por coluna, nossa matriz(tabela)
for i in range(1,len(data)): # percorrendo as linhas ignorando o cabeçalho
    linha = []
    for j in range (len(data[0])):# percorrendo as colunas
        if j == 3: # quarta coluna
            linha.append(int(data[i][j]))
        else:
            linha.append(data[i][j])
        print(data[i][j], end='\t')
    print()#quebra de linha

print(playlist)

# imprimir apenas o nome
for i in range(len(playlist)):
    print(playlist[i][0])
