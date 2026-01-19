from time import sleep
from emoji import emojize

cores = {
'limpa': '\033[m',
'negrito_verde': '\033[1;32m',
'negrito_vermelho': '\033[1;31m',
'azul': '\033[34m',
'vermeho': '\033[31m',
'amarelo': '\033[33m'
}

num_int = int(input('Digite um numero inteiro: ')) # numero inteiro do usuario

print('{}Agora digite:{}'.format(cores['amarelo'], cores['limpa']))
print('{}1 para converção em binario \n2 para converção octal \n3 para coverção hexadecimal{}'.format(cores['negrito_verde'], cores['limpa']))
base_de_converção = int(input('Qual será a forma de converção: ')) #forma de converção

if base_de_converção == 1:
    bin_num = bin(num_int) # numero convertido em binario(Ob)
    print('Convertendo...')
    sleep(2)
    print('O numero {} convertido em binario é igual a: {}{}{}'.format(num_int, cores['azul'], bin_num[2:], cores['limpa']))

elif base_de_converção == 2:
    oct_num = oct(num_int) # numero convertido em octal(0o)
    print('Convertendo...')
    sleep(2)
    print('O numero {} convertido em octal é igual a: {}{}{}'.format(num_int, cores['azul'], oct_num[2:], cores['limpa']))

elif base_de_converção == 3: 
    hex_num = hex(num_int) # numero convertido em hexadecimal(0x)
    print('Convertendo...')
    sleep(2)
    print('O numero {} convertido em hexadecimal é igual a: {}{}{}'.format(num_int, cores['azul'], hex_num[2:], cores['limpa']))

else:
    print('{}ERRO{}'.format(cores['negrito_vermelho'], cores['limpa']))
    print('{}Você provavelmente digitou um numero que não condiz com as opções de converção'.format(cores['vermeho']))
    print('Por favor, tente novamente{}'.format(cores['limpa']))

sleep(0.5)
print(emojize('Agradecemos a utilização :beaming_face_with_smiling_eyes:'))
