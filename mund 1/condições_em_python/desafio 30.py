num = int(input('Esoclha um numero: '))
num_par = num % 2
if num_par == 0:
    print('Seu numero é par pois o resta da divisão por 2 é igual a zero')
else:
    print('Seu numero é impar')
    print('Ou seja o resto é diferente de zero por isso este numero é impar')
