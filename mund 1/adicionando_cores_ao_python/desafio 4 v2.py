cores = {
'limpa': '\033[m',
'vermelho': '\033[41m',
'verde': '\033[42m',
}

n1 = int(input('Escolha um numero: '))
n2 = int(input('Escolha um outro numero'))

print('A soma deles é igual a {}{}{}'.format(cores['verde'], n1 + n2, cores['limpa']))
print('Ou melhor dizendo: a soma de {}{}{} mais {}{}{} é igual a: {}{}{}'.format(
cores['vermelho'], n1, cores['limpa'],
cores['vermelho'], n2, cores['limpa'],
cores['verde'], n1 + n2, cores['limpa']
))
