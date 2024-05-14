import random
num_elementos = random.randint(5,20)
n_a = []
for i in range(num_elementos):
    n = random.randint(1,10)
    n_a.append(n)
print(n_a)
print(sum(n_a))
print(sum(n_a)/len(n_a))


