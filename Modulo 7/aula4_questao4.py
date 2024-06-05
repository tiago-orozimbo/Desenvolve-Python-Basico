import random

def imprime_enforcado(erros):
    estagios = [
        """
         ------
         |    |
              |
              |
              |
              |
        --------
        """,
        """
         ------
         |    |
         O    |
              |
              |
              |
        --------
        """,
        """
         ------
         |    |
         O    |
         |    |
              |
              |
        --------
        """,
        """
         ------
         |    |
         O    |
        /|    |
              |
              |
        --------
        """,
        """
         ------
         |    |
         O    |
        /|\\   |
              |
              |
        --------
        """,
        """
         ------
         |    |
         O    |
        /|\\   |
        /     |
              |
        --------
        """,
        """
         ------
         |    |
         O    |
        /|\\   |
        / \\   |
              |
        --------
        """
    ]
    print(estagios[erros])

def jogar_forca():
    with open("gabarito_forca.txt", "r") as arquivo:
        palavras = arquivo.read().splitlines()
    
    palavra = random.choice(palavras).upper()
    palavra_oculta = ["_"] * len(palavra)
    tentativas = 6
    erros = 0
    letras_usadas = []

    while erros < tentativas and "_" in palavra_oculta:
        print(" ".join(palavra_oculta))
        letra = input("Digite uma letra: ").upper()

        if letra in letras_usadas:
            print("Você já tentou essa letra.")
            continue

        letras_usadas.append(letra)

        if letra in palavra:
            for i, char in enumerate(palavra):
                if char == letra:
                    palavra_oculta[i] = letra
        else:
            erros += 1
            imprime_enforcado(erros)

    if "_" not in palavra_oculta:
        print(f"Parabéns! Você acertou a palavra: {palavra}")
    else:
        print(f"Você perdeu! A palavra era: {palavra}")

jogar_forca()
