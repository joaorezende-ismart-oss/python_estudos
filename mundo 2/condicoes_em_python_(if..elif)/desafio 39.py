from datetime import date
from webbrowser import open
from time import sleep

cores = {
"limpa": '\033[m',
"amarelo": '\033[33m',
"vermelho": '\033[31m',
"verde": '\033[32m',
"azul": '\033[34m'
}

link_alistamento_militar = 'https://alistamento.eb.mil.br' # link alistamento militar

ano_nasc = int(input('Qual o seu ano de nascimento: ')) # ano de nascimento do usuario
idade_atual = (date.today().year) - ano_nasc # idade atual do usuario

if idade_atual < 18: # resposta para menores de 18 anos
    idade_18 = 18 - idade_atual # anos faltando para completar 18 anos

    print(f'{cores["amarelo"]}Vocẽ ainda não esta na época de se alistar ao serviço militar{cores["limpa"]}')
    print(f'Você podera alistar-se daqui {idade_18} anos quando estiver com 18 anos')

elif idade_atual == 18: # resposta para usuarios de 18 anos

    print(f'{cores["amarelo"]}Esta na época de se alistar para o serviço militar!{cores["limpa"]}')
    print(f'Acesse o site oficial {link_alistamento_militar} ou procure a junta militar mais proxima a sua residencia')
    
    sleep(1)
    print('Veja abaixo os itens que são necessarios para a inscrição:')
    print(f'{cores["verde"]}Certidão de nascimento \nComprovante de residencia \nDocumento oficial com foto \nCPF {cores["limpa"]}')

    sleep(1)
    decisão = input(f'{cores["azul"]}Deseja abrir o site o site de alistamento? \n[S/n]{cores["limpa"]}').upper() # abrir o site de inscrição militar

    if decisão == 'S':
        print('Abrindo site...')
        sleep(2)
        open(link_alistamento_militar)

    else:
        print('Não perca tempo e se aliste o mais rapido possivel!')
        print('O exercito brasileiro precisa de você')

else:
    print('Ja passou da época de alistar-se no exercito brasileiro!')
    sleep(1)
    print(f'{cores["amarelo"]}Caso não tenha se alistado no exercito, veja algumas das restrições que são geradas a você:{cores["limpa"]}')
    print(f'{cores["verde"]}Impedimento de obter passaporte \nProibição de obter carteira de trabalho \nRestrição para obter registro profissional{cores["limpa"]}')
    print('Entre muitas outras coisas...')
    print(f'{cores["vermelho"]}Compareça a junta militar mais proxima para regularizar sua situação!{cores["limpa"]}')

print('Agradecemos o interesse em ingressar')
