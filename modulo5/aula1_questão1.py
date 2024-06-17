numero1 = float(input("Digite o primeiro número decimal: "))
numero2 = float(input("Digite o segundo número decimal: "))

diferenca_absoluta = abs(numero1 - numero2)

diferenca_arredondada = round(diferenca_absoluta, 2)

print("A diferença absoluta entre os números é:", diferenca_arredondada)