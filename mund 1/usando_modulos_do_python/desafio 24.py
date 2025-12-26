cidade = input('Nome da sua cidade: ')
cidade_lista = cidade.title().split()
print('O nome da sua cidade começa com Santo?')
print('Santo' in cidade_lista[0])
