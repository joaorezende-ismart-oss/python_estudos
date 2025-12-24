import math
alt = float(input('Qual a altura da sua parede? '))
larg = float(input('Qual a largura da sua parede? '))
area = larg * alt
print('De acordo com a largura igual a {} e a altura igual a {} a area da parede é igual a: {:.2f}m^2'.format(larg, alt, area))
baldes = area / 2
print('Para pintar essa parede com baldes de 1 litro de tinta que pintam 2 metros cubicos cada um')
print('Você precisara de {:.2f} baldes'.format(baldes))
baldes_arredondados = math.ceil(area / 2)
print('Caso seu valor seja um valor quebrado(arredondando para cima) você precisara de {} baldes'.format(baldes_arredondados))
