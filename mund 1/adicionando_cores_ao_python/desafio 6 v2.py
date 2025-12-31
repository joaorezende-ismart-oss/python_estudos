n1 = int(input('Escolha um numero: '))

s = n1 + 1
su = n1 - 1

print('Você sabia que o sucessor do \033[31m{}\033[m é o \033[32m{}\033[m e o antecessor é o \033[32m{}\033[m'.format(n1, s, su))
print('=' * 20)

n2 = int(input('Escolha outro numero: '))

print('Seu antecessor é \033[32m{}\033[m e seu sucessor é \033[32m{}\033[m'.format(n2 - 1, n2 + 1))
