cores = {
'limpa':'\033[m',
'verde':'\033[32m',
'ciano':'\033[36m',
'amarelo':'\033[33m',
'vermelho':'\033[31m'
}

dia = input('{}qual é o dia do seu nascimento?{} '.format(cores['amarelo'], cores['limpa']))
mês = input('{}qual é o mês do seu nascimento?{} '.format(cores['amarelo'], cores['limpa']))
ano = input('{}qual é o ano do seu nascimento?{} '.format(cores['amarelo'], cores['limpa']))

print('você nasceu no dia {}{}{} de {}{}{} em {}{}{}.'.format(
cores['vermelho'], dia, cores['limpa'],
cores['verde'], mês, cores['limpa'],
cores['ciano'], ano, cores['limpa']
))
