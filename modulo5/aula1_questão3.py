import random

numero_aleatorio = random.randint(1, 10)

while True:
    palpite = int(input("Adivinhe o número entre 1 e 10: "))
    
    if palpite < numero_aleatorio:
        print("Muito baixo! Tente novamente.")
    elif palpite > numero_aleatorio:
        print("Muito alto! Tente novamente.")
    else:
        print("Correto! Você adivinhou o número.")