idade = int(input('Qual é sua idade? '))
q_jogo = input('Você já jogou pelo menos 3 jogos de tabuleiro? ')
venceu = int(input('Quantas vezes venceu um jogo? '))
a = idade >= 16 and idade <=18
b = q_jogo == 'sim'
c = venceu >=1
participar = a and b and c
print(participar)
