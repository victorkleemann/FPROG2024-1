
def cifrarMensagem(msg):
    msgCifrada = ''
    for i in range (len(msg)):
        code = ord(msg[i]) - 1 
        msgCifrada = msgCifrada + chr(code)
    return msgCifrada

def decifrarMsg(msgCifrada):
    msgDecifrada = ''
    for i in range(len(msgDecifrada)):
        code = ord(msgCifrada[i]) + 1
        msgDecifrada += chr(code)
    return msgDecifrada

###############################
msg = input('Digite sua mensagem: ')
msgCifrada = cifrarMensagem(msg)
print(msgCifrada)

# Salvar a mensagem cifrada em um arquivo

nomeArquivo = input('Digite o nome do arquivo que deseja salvar: ')
inputFile = open(nomeArquivo, 'w')
inputFile.write(msgCifrada)
inputFile.close()
#textStr = inputFile.read()

# Ler o arquivo com a msg cirada e decifrar a mensagem
nomeArquivo = input('Digite o nome do arquivo que deseja salvar: ')
arqEntrada = open(nomeArquivo, 'r')
mensagemCifrada = arqEntrada.read() # Armazena todo o conteudo do arquivo em uma string
arqEntrada.close()
mensagemDecifrada = decifrarMsg(mensagemCifrada)
print(mensagemDecifrada)
