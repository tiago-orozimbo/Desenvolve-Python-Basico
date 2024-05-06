ano = int(input('Digite um ano para verificar se o mesmo é ano bissexto: '))
ano_b = ano % 400
ano_nb = ano % 100
ano_b1 = ano % 4
if  (ano_b == 0 and ano_nb > 0) or ano_b1 == 0  :
    print('Bissexto.')
else :
    print('Não Bissexto.')
