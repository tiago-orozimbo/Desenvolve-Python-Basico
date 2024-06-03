data = input("Digite uma data de nascimento neste formato (dd/mm/aaaa): ")
dia = data[0:2]
ano = data[6:10]
mes_n = data[3:-5]
mes_n = int(mes_n)
mes_n -= 1
mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
mes = mes[mes_n]
print(f'Você nasceu em  {dia} de {mes} de {ano}')

