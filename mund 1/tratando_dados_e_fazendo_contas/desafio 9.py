m = float(input('Me fale um valor em metros: '))
km = m * 0.001
hm = m * 0.01
dam = m * 0.1
dm = m * 10
c = m * 100
mm = m * 1000
print('{} metros é igual a: \n{} cm e \n{} mm'.format(m, c, mm))
print('É igual a {} dm, \n{:.1f} dam, \n{:.2f} hm'.format(dm, dam, hm))
print('Por fim {} metros é igual a {:.3f} km'.format(m, km))
