nL = input('digite um "numero": ') 
nl = input('digite um segundo "numero": ')
print('Você sabia que estes "numeros" são considerados letras para o python? ')
print('olha só: ')
print(type(nL))
print(type(nl))
print('Mas dessas vez serão numeros, quer ver? ')
n1 = int(input('Esolha um numero: '))
n2 = int(input('Escolha outro numero '))
print(type(n1))
print(type(n2))
print('Tudo isso por conta de um unico "tipo primitivo" o grande INT ')
print('E agora da pra fazer muita coisa com esses numeros, olha só: ')
s = n1 + n2
z = n1 - n2
m = n1 * n2
d = n1 / n2 
print('A soma entre {} e {} é igual a: {}'.format(n1, n2, s))
print('A subtração entre {} e {} é igual a: {}'.format(n1, n2, z))
print('A multiplicação entre {} e {} tem como resultado: {}'.format(n1, n2, m))
print('A divisão entre {} e {} é igual a: {}'.format(n1, n2, d))
