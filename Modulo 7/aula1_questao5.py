frase = input("Digite a frase: ")
coun_vogais = 0
indices = []
for i in range(len(frase)):
    if frase[i] in "aeiouAEIOU":
        coun_vogais += 1
        indices.append(i)
print(coun_vogais)
print(indices)