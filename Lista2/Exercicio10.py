# O lojista gostou tanto do seu programa anterior que encomendou outro. Dessa vez ele quer que 
# você calcule quanto cada cliente gastou na loja apenas informando o número de camisetas, calças 
# e cintos comprados. As camisetas custam R$ 25,00, as calças cem reais e os cintos 40 reais. Some o 
# valor da compra e ao final dê um desconto de 10 por cento sobre o total. Exiba na tela o valor do 
# desconto e o valor da compra.

valorCamisas = int(input('Quantas camisas você comrpou? '))
valorCalca = int(input('Quantas calças você comrpou? '))
valorCinto = int(input('Quantos cintos você comrpou? '))

camisas = 25
calca = 100
cinto = 40
desconto = 10

totalCamisas = valorCamisas * camisas
totalCalcas = valorCalca * calca
totalCintos = valorCinto * cinto

total = totalCalcas + totalCamisas + totalCintos 
totalDescontado = total - (total * desconto / 100)

print('O valor total de sua compra foi de',total,'reais, porém você tem direito a um desconto de',desconto,'%. Ou seja, o valor final da sua compra foi de',totalDescontado,'reais')




