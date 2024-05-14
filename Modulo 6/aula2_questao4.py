l1 = []
l2 = []
n_l1 = int(input("Digite a quantidade de elementos da lista 1: "))
for i in range(n_l1):
    n1 = int(input("Digite os elementos da lista 1: %d: "%i))
    l1.append(n1)
n_l2 = int(input("Digite a quantidade de elementos da lista 2: "))
for i in range(n_l2):
    n2 = int(input("Digite os elementos da lista 2: %d: "%i))
    l2.append(n2)
l3 = l2 + l1
print (l1)
print (l2)
print (sorted(l3))
