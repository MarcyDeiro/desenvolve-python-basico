import random
import math

n = int(input("Digite o valor de n: "))

soma = 0

for _ in range(n):
    valor = random.randint(0, 100)
    soma += valor

raiz_quadrada = math.sqrt(soma)

print(f"A soma dos {n} valores aleatórios é: {soma}")
print(f"A raiz quadrada da soma é: {raiz_quadrada:.2f}")