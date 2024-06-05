import re

def analisar_roteiro():
    with open("estomago.txt", "r", encoding="latin-1") as arquivo:
        linhas = arquivo.readlines()
    
    primeiras_25_linhas = linhas[:25]
    numero_de_linhas = len(linhas)
    linha_mais_longa = max(linhas, key=len)
    
    nonato_mencoes = sum(1 for linha in linhas if re.search(r'\bnonato\b', linha, re.IGNORECASE))
    iria_mencoes = sum(1 for linha in linhas if re.search(r'\bíria\b', linha, re.IGNORECASE))
    
    print("Primeiras 25 linhas:")
    for linha in primeiras_25_linhas:
        print(linha.strip())
    
    print(f"\nNúmero de linhas: {numero_de_linhas}")
    print(f"Linha com maior número de caracteres: {linha_mais_longa.strip()}")
    print(f"Número de menções a 'Nonato': {nonato_mencoes}")
    print(f"Número de menções a 'Íria': {iria_mencoes}")

analisar_roteiro()
