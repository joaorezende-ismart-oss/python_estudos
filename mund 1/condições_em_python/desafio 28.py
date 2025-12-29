from random import randint
print('===Tente adivinhar o numero escolhido entre 0 e 5===')
num = int(input('escolha um numero de 0 a 5: '))
num_sorteado = randint(0, 5)
if num == num_sorteado:
    print('Parabens você acertou o numero sorteado')
    print('Que tal ver se vocÊ acerta de novo?')
else:
    print('Você errou, o numero sorteado era {}'.format(num_sorteado))
    print('Que tal tantar mais uma vez?')
print('Bom jogo')
