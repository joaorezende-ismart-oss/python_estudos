velocidade = float(input('Velocidade do carro: km'))
muta = (velocidade - 80) * 7
if velocidade > 80:
    print('A velocidade do carro está acima de 80km')
    print('O carro devera ser mutado em: R${}'.format(muta))
else:
    print('A velocidade está de acordo com as permitidas nesta estrada')
