d = float(input('Digite a distância da entrega em quilômetros: '))
p = float(input('Digite o peso do pacote em quilogramas: '))
if d <= 100 :
    frete = d* p * 1
if d > 100 and d <= 300 : 
    frete = d * p * 1.50
if d > 300 :
    frete = d * p * 2
if p > 10 :
    frete = frete + 10
print (f'O valor do frete é: R${frete}') 
