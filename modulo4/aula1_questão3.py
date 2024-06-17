n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))

m = (n1 + n2 + n3)/3

if m >= 60:
    print('Aprovado')
elif m >= 40:
    print('Recuperação')
else:
    print('Reprovado')
print('Fim')