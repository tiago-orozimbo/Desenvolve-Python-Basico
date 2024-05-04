comprimento_terreno = int(input('Qual é o comprimento do terreno ? '))
largura_terreno = int(input('Qual é o largura do terreno ? '))
area_m2 = comprimento_terreno * largura_terreno
preco_m2 = float(input('Qual é o preço do metro quadrado da região ? '))
preco_total = preco_m2 * area_m2
print(f"O terreno possui {area_m2}m^2 e custa {preco_total} reais")
