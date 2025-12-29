viagem_km = float(input('Quanto km terá está viagem: km'))
if viagem_km <= 200:
    preço = viagem_km * 0.5
    print('Sua viagem custara {}'.format(preço))
    if preço <= 65:
        print('Ela está realmente barata')
    else:
        print('Ela está bem cara não?')
else: 
    preço = viagem_km * 0.45
    print('Sua viagem custara {}'.format(preço))
    if preço <= 245:
        print('Ela está barata')
    else:
        print('Ela está ficando cara!')
print('Tenha uma boa viagem!')
