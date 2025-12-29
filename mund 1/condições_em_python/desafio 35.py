r1 = float(input('Valor da reta: ')) #a
r2 = float(input('Valor da segunda reta: ')) #b
r3 = float(input('Vlor da terceira reta: ')) #c
d = r2 - r3
if d < 0:
    d * -1
triangulo = d < r1 < r2 + r3
if triangulo == True:
    print('De acordo com as medias da reta...')
    print('É possivel criar um triangulo')
else:
    print('Não é possivel criar um triangulo com essas medidas')
