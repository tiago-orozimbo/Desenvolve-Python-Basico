import random
def embaralhar_palavras(frase):
    palavras = frase.split()
    resultado = []
    for palavra in palavras:
        if len(palavra) <= 3:
            resultado.append(palavra)
        else:
            letras_intermediarias = list(palavra[1:-1])
            random.shuffle(letras_intermediarias)
            palavra_embaralhada = palavra[0] + ''.join(letras_intermediarias) + palavra[-1]
            resultado.append(palavra_embaralhada)
    return ' '.join(resultado)

frase = input('Digite uma frase: ')
resultado = embaralhar_palavras(frase)
print(resultado)
