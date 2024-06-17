n = int(input('Digite a quantidade de respondentes: '))

soma = 0
cont = 0

while cont < n:
    idade = int(input())
    soma += idade

    cont += 1

print(f"A média das idades é {soma/n:.0f} anos")