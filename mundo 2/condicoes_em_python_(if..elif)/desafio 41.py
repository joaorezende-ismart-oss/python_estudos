from datetime import date

cores = {
"limpa": '\033[m',
"azul": '\033[34m',
"amarelo": '\033[33m'
}

ano_nascimento = int(input('Qual o ano de nascimento do atleta: '))
idade_atual = date.today().year - ano_nascimento

if idade_atual <= 9: # atleta MIRIM
    print(f'Como o atleta tem {cores["azul"]}{idade_atual}{cores["limpa"]},a sua categoria será {cores["amarelo"]}MIRIM{cores["limpa"]}')

elif idade_atual > 9 and idade_atual <= 14: # atleta INFANTIL
    print(f'O atleta tem {cores["azul"]}{idade_atual}{cores["limpa"]} anos então ele se encontra contra na classificação {cores["amarelo"]}INFANTIL{cores["limpa"]}')

elif idade_atual > 14 and idade_atual <= 19: # atleta JUNIOR
    print(f'Tendo {cores["azul"]}{idade_atual}{cores["limpa"]} anos, o atleta está na classificação {cores["amarelo"]}JUNIOR{cores["limpa"]}')

elif idade_atual > 19 and idade_atual <= 21: # atleta SENIOR
    print(f'Com {cores["azul"]}{idade_atual}{cores["limpa"]} anos, o classificação para este atleta é a {cores["amarelo"]}SENIOR{cores["limpa"]}')

else: # atleta MASTER
    print(f'O atleta contem {cores["azul"]}{idade_atual}{cores["limpa"]} anos, o que o coloca na classificação mais alta, {cores["amarelo"]}MASTER{cores["limpa"]}')
