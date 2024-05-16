frase = input("Escreva uma frase: ")
vogais = 'aeiouAEIOU'
lista_vogais = sorted([i for i in frase if i in vogais])
lista_consoantes = sorted ([i for i in frase if i.isalpha() and i not in vogais])
print("Lista de vogais ordenada alfabeticamente:", lista_vogais)
print("Lista de consoantes:", lista_consoantes)
