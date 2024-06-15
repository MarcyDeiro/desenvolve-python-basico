classe = input('Escolhe a classe (guerreiro, mago ou arqueiro):')
forca = int(input('Digite os pontos de força do personagem: '))
magia = int(input('Digite os pontos de magia do personagem: '))

apto_guerreiro = (forca >= 15) and (magia <= 10)
apto_mago = (forca <=10) and (magia >= 15)
apto_arqueiro = (5 < forca <= 15) and (5 < magia <= 15)

apto = (classe == "guerreiro" and apto_guerreiro) or \
       (classe == "mago" and apto_mago) or \
       (classe == "arqueiro" and apto_arqueiro)

print("Pontos de atributo consistentes com a classe escolhida:", apto)