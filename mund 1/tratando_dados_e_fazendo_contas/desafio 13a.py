preço = float(input('Qual o preço do produto: '))
preço_a_vista = preço - preço * 10/100
print('Preço do produto a vista: {}'.format(preço_a_vista))
preço_parcelado12x = preço + preço * 8/100
print('Preço parcelado em até 12 vezes: {}'.format(preço_parcelado12x))
preço_parcelado_mais_12x = preço + preço * 12/100
print('Preço parcelado em mais de 12 vezes: {}'.format(preço_parcelado_mais_12x))
