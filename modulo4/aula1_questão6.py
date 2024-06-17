n = int(input('Digite a quantidade de experimentos realizados: '))
cont = 0
soma_s, soma_r, soma_c = 0, 0, 0

while cont < n:
    quantia = int(input())
    tipo = input()

    if tipo == 'S':
        soma_s += quantia
    elif tipo == 'R':
        soma_r += quantia
    elif tipo == 'C':
        soma_c += quantia

    cont += 1

print('O total de cobaias é:',soma_s + soma_r + soma_c)
print('O total de sapos é:',soma_s)
print('O total de sapos é:',soma_r)
print('O total de coelhos é:',soma_c)