import math
angulo = float(input('Qual a medida do ângulo: '))
radiano = math.radians(angulo)
print('A seno do ângulo de {}° é igual a: {:.3f}'.format(angulo, math.sin(radiano)))
print('O cosseno deste ângulo é igual a: {:.3f}'.format(math.cos(radiano)))
print('E a tangente deste ângulo é igual a {:.3f}'.format(math.tan(radiano)))