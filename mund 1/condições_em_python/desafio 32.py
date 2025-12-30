print('Vamos vamos ver se tal ano é bisssexto')
ano = int(input('Digite um ano qualquer: '))
ano_bissesto = ano % 4 
if ano_bissesto == 0:
    print('O ano de {} é um ano bissexto, ou seja contem 366 dias'.format(ano))
else:
    print('O ano de {} não é bissexto'.format(ano))
