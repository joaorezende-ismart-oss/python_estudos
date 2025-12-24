'''from math import pow, sqrt
num1 = float(input('Qual a medida do cateto oposto do triangulo: '))
num2 = float(input('Qual a medida do cateto adjacente: '))
hipotenusa = sqrt(pow(num1, 2) + pow(num2, 2))
print('Tendo a medida do cateto oposto igual a {} e a medida do cateto adjacente igual a {}'.format(num1, num2))
print('A hipotenusa deste triangulo é igual a {}'.format(hipotenusa))'''
from math import hypot
cateto_oposto = float(input('Medida do cateto oposto: '))
cateto_adjacente = float(input('Medida do cateto adjacente: '))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print('A hipotenusa dessa triangulo mede {:.2f}'.format(hipotenusa))