nota = int(input('Como você avalia o filme (notas de 1 a 5): '))
if nota == 1:
    print('Ruim')
if nota == 2:
    print('Regular')
if nota == 3:
    print('Bom!')
if nota == 4:
    print('Muito Bom!')
if nota == 5:
    print('Excelente!')
if nota > 5 or nota <1 :
    print('Nota invalida!')