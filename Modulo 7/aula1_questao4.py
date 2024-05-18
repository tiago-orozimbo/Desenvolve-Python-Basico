numero = input("Digite o número: ")
if len(numero) == 8:
    numero_completo = "9" + numero
    numero_completo = numero_completo[:5] + "-" + numero_completo[5:]
    print(f"Número completo: {numero_completo}")
elif len(numero) == 9 and numero[0] == "9":
    print("Número completo")
    numero = numero[:5] + "-" + numero[5:]
    print(numero)
else:
    print("Número invalido")
