dias_alugados = int(input('Por quantos dias o carro foi alugado: '))
km_rodados = float(input('Quantos km o carro rodou em quanto alugado: '))
dia_preço = dias_alugados * 60
km_preço = km_rodados * 0.15
preço_final = km_preço + dia_preço
print('Um carro que rodou {}km e ficou alugado por {} dias, de ser pago por ele: R${:.2f}'.format(km_rodados, dias_alugados, preço_final))
