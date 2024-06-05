import os
import re

def processar_frase():
    # Definir caminhos dos arquivos
    caminho_atual = os.getcwd()
    caminho_frase = os.path.join(caminho_atual, "frase.txt")
    caminho_palavras = os.path.join(caminho_atual, "palavras.txt")
    
    # Ler o conteúdo do arquivo "frase.txt"
    with open(caminho_frase, "r") as arquivo:
        conteudo = arquivo.read()
    
    # Encontrar todas as palavras (removendo espaços e caracteres não alfabéticos)
    palavras = re.findall(r'\b\w+\b', conteudo)
    
    # Escrever as palavras no arquivo "palavras.txt", uma em cada linha
    with open(caminho_palavras, "w") as arquivo:
        for palavra in palavras:
            arquivo.write(palavra + "\n")
    
    # Ler e imprimir o conteúdo do arquivo "palavras.txt"
    with open(caminho_palavras, "r") as arquivo:
        print(arquivo.read())

processar_frase()
