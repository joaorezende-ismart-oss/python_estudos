cores = {
'limpa': '\033[m',
'amarelo': '\033[33m',
'verde_fundo': '\033[42m',
}

r = float(input('{}Quanto reias você tem na sua carteira? R${}'.format(cores['amarelo'], cores['limpa'])))

us = r / 5.52 #contação no dia que fiz o programa
print('Com {} reais você pode comprar {}{:.2f}{} dolares'.format(r, cores['verde_fundo'], us, cores['limpa'])) # reais para dolares

e = r / 6.46
print('Além disso, com {} reais você pode comprar {}{:.2f}{} euros'.format(r, cores['verde_fundo'], e, cores['limpa'])) # reais para euros
