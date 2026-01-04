from math import ceil

cores = {
'limpa': '\033[m',
'amarelo_sublinhado': '\033[4;33m',
'vermelho_fundo': '\033[41m',
'verde_fundo': '\033[42m',
'azul': '\033[34m'
}

alt = float(input('{}Qual a altura da sua parede? '.format(cores['amarelo_sublinhado'])))
larg = float(input('Qual a largura da sua parede? {}'.format(cores['limpa'])))

area = larg * alt

print('De acordo com a largura igual a {}{}{} e a altura igual a {}{}{} a area da parede é igual a: {}{:.2f}m^2{}'.format(
cores['vermelho_fundo'], larg, cores['limpa'], 
cores['vermelho_fundo'], alt, cores['limpa'],
cores['verde_fundo'], area, cores['limpa']
))

baldes_arredondados = ceil(area / 2)

print('{}Para pintar essa parede com baldes de 1 litro de tinta que pintam 2 metros cubicos cada{}'.format(cores['azul'], cores['limpa']))
print('Você precisara de {}{}{} baldes'.format(cores['verde_fundo'], baldes_arredondados, cores['limpa']))
