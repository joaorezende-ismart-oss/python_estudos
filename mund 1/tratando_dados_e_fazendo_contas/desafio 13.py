preço = float(input('Me fala o valor de um produto: R$'))
print('Um produto de {} reais com 5% de desconto terá como seu preço final igual a: {:.2f} reais'.format(preço, preço - (preço * 1/20)))
