import random
n_a = (random.randint (0,10))
while True :
    n = int(input('Adivinhe o número entre 1 e 10: '))
    if n == n_a :
        print(f'Correto! O número é {n}.')
        break
    elif n > n_a :
        print('Muito alto, tente novamente!')
    else :
        print('Muito baixo, tente novamente!')
