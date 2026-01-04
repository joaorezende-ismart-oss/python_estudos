cores = {
'limpa': '\033[m',
'magenta': '\033[35m'
}

n = int(input('\033[033mDigite um numero para ver sua tabuada:\033[m '))

print('\033[32m-=-\033[m' * 7)
print('{} * {}{:2}{} = {:3}'.format(n, cores['magenta'], 1, cores['limpa'], n)) # n vezes 1
print('{} * {}{:2}{} = {:3}'.format(n, cores['magenta'], 2, cores['limpa'], n*2)) # n vezes 2
print('{} * {}{:2}{} = {:3}'.format(n, cores['magenta'], 3, cores['limpa'], n*3)) # n vezes 3
print('{} * {}{:2}{} = {:3}'.format(n, cores['magenta'], 4, cores['limpa'], n*4)) # n vezes 4
print('{} * {}{:2}{} = {:3}'.format(n, cores['magenta'], 5, cores['limpa'], n*5)) # n vezes 5
print('{} * {}{:2}{} = {:3}'.format(n, cores['magenta'], 6, cores['limpa'], n*6)) # n vezes 6
print('{} * {}{:2}{} = {:3}'.format(n, cores['magenta'], 7, cores['limpa'], n*7)) # n vezes 7
print('{} * {}{:2}{} = {:3}'.format(n, cores['magenta'], 8, cores['limpa'], n*8)) # n vezes 8
print('{} * {}{:2}{} = {:3}'.format(n, cores['magenta'], 9, cores['limpa'], n*9)) # n vezes 9
print('{} * {}{:2}{} = {:3}'.format(n, cores['magenta'], 10, cores['limpa'], n*10)) # n * 10
print('{} * {}{:2}{} = {:3}'.format(n, cores['magenta'], 11, cores['limpa'], n*11)) # n * 11
print('\033[32m-=-\033[m' * 7)
