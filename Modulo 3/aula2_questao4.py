personagem = input('Qual é a classe de personagem escolhido (guerreiro, mago ou arqueiro): ')
forca = int(input('Quais são os pontos de força do seu personagem: '))
magia = int(input('Quais são os pontos de magia do seu personagem: '))
guerreiro = personagem == 'guerreiro' and forca >=15 and magia <= 10
mago = personagem == 'mago' and forca <=10 and magia >= 15
arqueiro = personagem == 'arqueiro' and (forca >=5 and forca <=15) and (magia >= 5 and magia <= 15)
verdade = guerreiro or mago or arqueiro
print(verdade)