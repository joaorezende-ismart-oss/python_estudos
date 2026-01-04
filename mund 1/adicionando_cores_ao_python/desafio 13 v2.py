cores = {
'limpa': '\033[m',
'amarelo': '\033[33m',
'verde_fundo': '\033[42m', 
'vermelho_fundo/sublinhado': '\033[4;41m',
'azul_fundo/sublinhado': '\033[4;44m'
}

preço = float(input('{}Valor do produto: R${}'.format(cores['amarelo'], cores['limpa'])))

print('Um produto de {}{}{} reais com {}5% de desconto{} terá como seu preço final igual a: {}{:.2f} reais{}'.format(
cores['azul_fundo/sublinhado'], preço, cores['limpa'],
cores['vermelho_fundo/sublinhado'], cores['limpa'],
cores['verde_fundo'], preço - (preço * 1/20), cores['limpa']
))
