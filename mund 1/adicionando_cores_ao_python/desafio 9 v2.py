cores = {
'limpa': '\033[m',
'amarelo': '\033[33m',
'verde': '\033[32m'
}

m = float(input('Insira um valor em metros: ')) # valor em metros

km = m * 0.001 # metros convertido para quilometros
hm = m * 0.01 # metros convertido para hm
dam = m * 0.1 # metros convertido para dam
dm = m * 10 # metros convertido para dm 
cm = m * 100 # metros convertido para centimetros
mm = m * 1000 # metros convertido para milimetros

print('{}{}{} metros é igual a: \n{}{}{} cm \n{}{}{} mm'.format(
cores['amarelo'], m, cores['limpa'], # metro
cores['verde'], cm, cores['limpa'], # cm 
cores['verde'], mm, cores['limpa'] # mm
))
print('Igual a {}{}{} dm, \n{}{:.1f}{} dam, \n{}{:.2f}{} hm'.format(
cores['verde'], dm, cores['limpa'], # dm
cores['verde'], dam, cores['limpa'], # dam
cores['verde'], hm, cores['limpa'] # hm
))
print('Por fim {}{}{} metros é igual a {}{:.3f}{} km'.format(
cores['amarelo'], m, cores['limpa'], # metro
cores['verde'], km, cores['limpa'] # km
)) 
