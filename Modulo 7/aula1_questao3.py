frase = input("Digite a frase: ")
coun_vazios = 0
for i in range(len(frase)):
    if frase[i] in " ":
        coun_vazios += 1
print(coun_vazios)
