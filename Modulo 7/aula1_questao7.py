import random
def encrypt(lista):
    n = random.randint(1, 10)
    def criptografia(c):
        n_l = ord(c)
        novo_val = n_l + n
        if novo_val > 126:
            novo_val = 33 + (novo_val - 127)
        return chr(novo_val)
    lista_criptografada = []
    for string in lista:
        string_criptografada = ''.join(criptografia(c) for c in string)
        lista_criptografada.append(string_criptografada)
    return lista_criptografada, n
ele_lista = int(input("Digite a quantidade de elementos da sua lista: "))
lista_strings = []
for i in range(ele_lista):
    nomes = input("Digite o nome que deseja criptografar: ")
    lista_strings.append(nomes)
nomes_criptografados, chave = encrypt(lista_strings)
print(f'Nomes: {lista_strings}')
print(f'Nomes criptografados: {nomes_criptografados}')
print(f'Chave de criptografia: {chave}')
