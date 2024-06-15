idade = int(input('Digite a sua idade: '))
jogos = bool(input('Já jogou pelo menos 3 jogos de tabuleiro?: '))
venci = int(input('Quantos jogos já venceu?: '))

jogos = jogos == "sim"

apto = (16 <= idade <= 18) and jogos and venci > 0

print("Apto para ingressar no clube de jogos de tabuleiro:",apto)