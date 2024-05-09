q_respostas = int(input('Digite a quantidade de respondentes: '))
quant = q_respostas
media_idade = 0
while q_respostas > 0:
    idade = int(input('Digite a idade do respondente: '))
    media_idade += idade
    q_respostas -= 1
media_idade = media_idade / quant
print(f'A media das idades é {media_idade}')