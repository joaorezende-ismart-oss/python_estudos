from emoji import emojize

cores = {
'limpa': '\033[m',
'verde': '\033[32m',
'vermelho': '\033[31m',
'amarelo': '\033[33m',
'azul_sublinhado': '\033[4;34m'
}

print('{}{}Emprestimo bancario{}{}'.format(cores['azul_sublinhado'], '-=-' * 7, '-=-' * 7, cores['limpa']))

valor_imovel = float(input('{}Qual o valor do imovel a ser adqurido: R$'.format(cores['amarelo'])))
salario_comprador = float(input('Qual o salario do individul que ira fazer a compra: R$'))
pagamento_anos = float(input('Em quanto anos será pago o imovel:{} '.format(cores['limpa'])))

prestação_mensal = valor_imovel / pagamento_anos

if prestação_mensal <= salario_comprador * 30 / 100:
    print('{}Vocẽ pode comprar esse imovel!{}'.format(cores['verde'], cores['limpa']))
    print('O valor mensal a ser pago será de, R${}'.format(prestação_mensal))
else:
    print('{}Não é possivel comprar esse imovel no momento{}'.format(cores['vermelho'], cores['limpa']))
print(emojize('Agradecemos a preferencia! :beaming_face_with_smiling_eyes:'))                   
