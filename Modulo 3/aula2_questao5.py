genero = input('Qual é seu genero? ')
idade = int(input('Qual é sua idade? '))
t_contr = int(input('Qual é o tempo de contribuição? '))
a = genero == ('m' and idade >= 65) or (genero == 'f' and idade >= 60)
b = t_contr >= 30 and idade > t_contr
c = idade >=60 and t_contr >= 25
aposentar = a or b or c
print(aposentar)