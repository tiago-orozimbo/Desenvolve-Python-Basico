exp = int(input('Digite a quantidade de experimentos realizados: '))
q_r = 0
q_s = 0
q_c = 0
while exp > 0 :
    r = int(input('Digite a quantidade de ratos utilizados: '))
    S = int(input('Digite a quantidade de sapos utilizados: '))
    c = int(input('Digite a quantidade de coelhos utilizados: '))
    q_r += r
    q_s += S
    q_c += c
    exp -= 1
t = q_c + q_r + q_s
print(f'Total de cobais: {t}')
print(f'Total de Coelhos: {q_c}')
print(f'Total de Sapos: {q_s}')
print(f'Total de Ratos: {q_r}')
print(f'Percentual de Coelhos: {(q_c/t)*100:,.2f}%')
print(f'Percentual de Sapos: {(q_s/t)*100:,.2f}%')
print(f'Percentual de Ratos: {(q_r/t)*100:,.2f}%')
