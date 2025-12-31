cores = {
'limpa':'\033[m',
'verde':'\033[32m',
'azul':'\033[34m',
'vermelho':'\033[31m'
}

nome = input('qual seu nome? ')
print('boas vindas, {}{}{}'.format(cores['verde'], nome, cores['limpa']))
print('========')
nome1 = input('Oi! Qual é seu nome? ')
print('boas vindas {}{}{} prazer em te conhecer!'.format(cores['azul'], nome1, cores['limpa']))
