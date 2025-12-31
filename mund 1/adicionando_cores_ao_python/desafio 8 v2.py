from time import sleep

print('\033[1;33m===media dos alunos===\033[m') # titulo

n1 = float(input('Quanto você tirou na sua ultima prova de matematica? ')) # nota 1 do usuario
n2 = float(input('E na sua penultima? ')) #nota 2 do usuario
n3 = float(input('E na antipenultima? ')) #nota 3 do usuario

print('\033[1;31mVOCÊ DEVE ESTAR CHUTANDO QUALQUER NUMERO NÉ???\033[m')

n4 = float(input('Então chuta mais um ai: ')) # nota 4 do usuario

print('A media das suas notas...')
sleep(2)
print('\033[34m(concerteza são numeros de notas não numeros que você chuto)\033[m')
sleep(2)
print('é de \033[32m{:.1f}\033[m'.format((n1 + n2 + n3 + n4) / 4))