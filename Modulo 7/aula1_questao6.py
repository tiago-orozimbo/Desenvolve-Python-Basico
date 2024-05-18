frase = "Meu amor mora em Roma e me deu um ramo de flores"
palavra_objetivo = sorted("amor")
palavras_sep = frase.lower().split()
print(palavras_sep)
for palavras in palavras_sep:
    if sorted(palavras) == palavra_objetivo:
        print(palavras)
