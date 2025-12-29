num1 = float(input('Esoclha um numero: '))
num2 = float(input('Escolha um segundo numero: '))
num3 = float(input('Escolha um terceiro numero: '))
# Tentativa inicial de resolução (não utilizada)
# Mantida apenas para estudo e comparação com a solução final
""" if num1 > num2 > num3:
    print('O maior numero é {}'.format(num1))
else:                                                  
    if num2 > num3: 
        print('O maior numero é {}'.format(num2))
    else:
        print('O maior numero é {}'.format(num3)) """
# solução final
# maior numero
maior = num1
if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3
print('O maior numero é o {}'.format(maior))
# menor numero 
menor = num1
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3
print('O menor numero é o {}'.format(menor))
