distancia = float(input('Digite o valor da distância de entrega em km:'))
pacote = float(input('Digite o peso do pacote em kg:'))

if pacote > 10:
    taxa = 10
else:
    taxa = 0

if distancia <= 100:
    frete = 1 * pacote + taxa
    print('O frete é de: R$',pacote)
elif distancia > 100 and distancia <= 300:
    frete = 1.5 * pacote + taxa
    print('O frete é de: R$',pacote)
else:
    frete = 2 * pacote + taxa
    print('O frete é de: R$',pacote)