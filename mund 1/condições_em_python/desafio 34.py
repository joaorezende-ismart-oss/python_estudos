print('===aumento salarial===')
salario = float(input('Qual o salario atual do funcionario: R$'))
if salario <= 1250.00:
    novo_salario = salario + salario * 15/100
    print('O novo salario do funcionario será R${:.2f}'.format(novo_salario))
else:
    novo_salario = salario + salario * 10/100
    print('O novo salario deste funcionario será de R${:.2f}'.format(novo_salario))
