import os

def salvar_frase():
    frase = input("Digite uma frase: ")
    caminho_arquivo = os.path.join(os.getcwd(), "frase.txt")
    
    with open("frase.txt", "w") as arquivo:
        arquivo.write(frase)
    
    print(f"Frase salva em {caminho_arquivo}")

salvar_frase()
