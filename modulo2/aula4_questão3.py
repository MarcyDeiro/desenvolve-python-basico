
nome1 = input('O nome do produto 1 é: ')
preco1 = float(input('Digite o preço unitário do produto 1: '))
quant1 = int(input('Digite a quantidade do produto 1: '))
total1 = preco1 * quant1

nome2 = input('O nome do produto 2 é: ')
preco2 = float(input('Digite o preço unitário do produto 2: '))
quant2 = int(input('Digite a quantidade do produto 2: '))
total2 = preco2 * quant2

nome3 = input('O nome do produto 3 é: ')
preco3 = float(input('Digite o preço unitário do produto 3: '))
quant3 = int(input('Digite a quantidade do produto 3: '))
total3 = preco3 * quant3

total = total1 + total2 + total3

print(f'O preço total da compra é: R$ {total:,.2f}')
