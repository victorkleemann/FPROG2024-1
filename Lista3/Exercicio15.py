valor =  float(input('Digite o valor do produto: '))
opcPag = input('Digite o método de pagamento("C" para crédito,"De para débito ou "Di" para dinheiro"): ')
desc15 = valor * 0.15
desc10 = valor * 0.10


if opcPag == 'C' or opcPag == 'Di':
    parc = input('Você deseja parcelar?("S" para sim e "N" para não)')
    if parc == 'S':
        qtParc = int(input('Em quantas vezes?'))
if opcPag == 'Di':
    print('Em dinheiro, sua compra recebe 15 por cento de desconto. O novo valor da sua compra será',desc15)
elif opcPag == 'C' and parc == 'N':
    print('No cartão a vista, sua compra recebe 10 por cento de desconto. O novo valor da sua compra será',desc10)
elif opcPag == 'C' and parc == 'S' and qtParc == '2':
    parcTrue = valor / qtParc
    print('O valor da sua compra de',valor,'foi dividida em 2 parcelas. Cada parcela será de',parcTrue) 
elif opcPag == 'C' and parc == 'S' and qtParc == '3':
    valParcPag = valor * 0,10 * qtParc
