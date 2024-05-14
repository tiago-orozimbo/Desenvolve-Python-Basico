import random
n_a = []
for i in range (20):
    n = random.randint(-100, 100)
    n_a.append(n)
print(sorted(n_a))
print (n_a)
print("O maior valor está no indice: ", n_a.index(max(n_a)))
print("O menor valor está no indice: ", n_a.index(min(n_a)))

