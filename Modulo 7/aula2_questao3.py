def eh_palindromo(frase):
    frase = ''.join(char.lower() for char in frase if char.isalnum())
    return frase == frase[::-1]

while True:
    entrada = input('Digite uma frase (digite "fim" para encerrar): ')
    if entrada.lower() == 'fim':
        break
    if eh_palindromo(entrada):
        print(f'"{entrada}" é palíndromo')
    else:
        print(f'"{entrada}" não é palíndromo')
