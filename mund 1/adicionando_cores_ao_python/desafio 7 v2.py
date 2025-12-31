cores = {
'limpa':'\033[m',
'negrito_verde':'\033[1;42m',
'negrito_azul':'\033[1;44m',
'negrito_magenta':'\033[1;45m',
'negrito_amarelo':'\033[1;43m'
}

n = float(input('Escolha um numero: ')) # numero que o usuario escolheu

print('O dobro de {}{:.2f}{} é igual à: {}{:.2f}{} \n O triplo deste é: {}{:.2f}{} \n e sua raiz quadrada igual à: {}{:.2f}{}'.format(
cores['negrito_magenta'], n, cores['limpa'], # numero
cores['negrito_amarelo'], n * 2, cores['limpa'],
cores['negrito_verde'], n * 3, cores['limpa'],
cores['negrito_azul'], n ** (1 / 2), cores['limpa']  # raiz quadrada
))
