l1 = []
ln_p = []
ln_i = []
n_l1 = int(input("Digite a quantidade de elementos da lista 1: "))
for i in range(n_l1):
    n1 = int(input("Digite os elementos da lista 1: %d: "%i))
    l1.append(n1)
    if n1 % 2 == 0:
        ln_p.append(n1)
    else :
        ln_i.append(n1)
print (f'A lista é : {l1}')
print(f'Os 3 primeiros elementos da lista são: {l1[:3]}')
print(f'Os 2 últimos elementos da lista são: {l1[:3:-1]}')
print(f'Lista invertida: {l1[::-1]}')
print(f'Os números pares da lista: {ln_p}')
print(f'Os números ímpares da lista: {ln_i}')