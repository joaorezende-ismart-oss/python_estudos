from time import sleep

cores = {
'limpa': '\033[m',
'verde': '\033[32m',
'vermelho': '\033[31m',
'amarelo': '\033[33m'
}

num_int_1 = int(input('Digite um numero inteiro: ')) # primeiro numero do usuario
num_int_2 = int(input('Digite um segundo numero inteiro: ')) # segundo numero do usuario

sleep(1)
print('Analisando os dados...')
sleep(2)

if num_int_1 > num_int_2:   # primeiro valor o maior
    print('{}O primeiro valor({}), é maior que o segundo({})!{}'.format(cores['verde'], num_int_1, num_int_2, cores['limpa']))

elif num_int_2 > num_int_1: # segundo valor o maior
    print('{}O segundo valor({}), é maior que o primeiro({})!{}'.format(cores['verde'], num_int_2, num_int_1, cores['limpa']))

else: # valores identicos
    print('{}O primeiro é o segundo valor são identicos, sendo ambos iguais a {}{}'.format(cores['amarelo'], num_int_1, cores['limpa']))
