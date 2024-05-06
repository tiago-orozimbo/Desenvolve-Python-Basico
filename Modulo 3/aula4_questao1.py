n_1 = int(input('Digite um número: '))
n_2 = int(input('Digite outro número: '))
n_3 = (n_1 + n_2) % 2
if n_3 == 0:
    print('O número é par.')
else :
    print('O número é ímpar.')