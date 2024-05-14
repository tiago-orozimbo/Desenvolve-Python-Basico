import random
lista1 = []
lista2 = []
for i in range (20):
    n = random.randint(0, 50)
    lista1.append(n)
for i in range (20):
    n = random.randint(0, 50)
    lista2.append(n)
interseccao  = []
for n in lista1:
    if n in lista2 and n not in interseccao:
        interseccao.append(n)
for i in interseccao:
    print (f"{i} : ({lista1.count(i)}, {lista2.count(i)})")
print(sorted(lista1))
print(sorted(lista2))
print(sorted(interseccao))


