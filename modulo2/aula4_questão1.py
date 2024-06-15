comprimento = int(input('Imprima o valor do comprimento: '))
largura = int(input('Imprima o valor da largura: '))
preco_m2 = float(input('Imprima o valor dos metros quadrados: '))

area_m2 = comprimento * largura
preco_t = preco_m2 * area_m2

print(f'O terreno possui {area_m2}m2 e custa R${preco_t:,.2f}')