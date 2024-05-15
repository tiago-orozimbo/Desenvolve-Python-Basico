import random
tam_f_m, tam_f_a, inicio_f_m, inicio_f_a = 0,0,0,0
l1 = [random.randint(-10,10) for i in range(20)]
for i in range (len(l1)):
    if l1[i] < 0:
        tam_f_a +=1
        if tam_f_a == 1:
            inicio_f_a = i
    else :
        if tam_f_a > tam_f_m:
            tam_f_m = tam_f_a
            inicio_f_m = inicio_f_a
        tam_f_a = 0
print(f'Lista original: {l1}')
del l1[inicio_f_m:inicio_f_m+tam_f_m]
print(f'Lista editada: {l1}')

