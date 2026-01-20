from time import sleep

cores = {
"limpa": '\033[m',
"amarelo": '\033[33m',
"azul": '\033[34m',
"verde": '\033[32m'
}

resposta_usuario = input('Digite algo: ').strip()
resposta_usuario1 = f'\033[34m{resposta_usuario}\033[m'

print('analisando...')
sleep(2)

if resposta_usuario1.isnumeric() == True:
    resposta_usuario1 = int(resposta_usuario1)
    print(f'O tipo primitivo do valor, {resposta_usuario1} é {cores["amarelo"]}int{cores["limpa"]}')

elif resposta_usuario1.title() == 'True' and 'False':
    print(f'O tipo primitivo do valor, {resposta_usuario1} é {cores["amarelo"]}bool{cores["limpa"]}')

elif resposta_usuario1.upper().isupper() == True:
    print(f'O tipo primitivo do valor, {resposta_usuario1} é {cores["amarelo"]}str{cores["limpa"]}')
    print(f'{cores["verde"]}A resposta é alphanumerica(contem letras e numeros): {resposta_usuario1.isalnum()}')
    print(f'A resposta é composta por espaços: {resposta_usuario1.isspace()}')
    print(f'A resposta contem apenas letras minusculas: {resposta_usuario1.islower()}') 
    print(f'A reposta contem apenas letras maiusculas: {resposta_usuario1.isupper()}{cores["limpa"]}')

else: 
    resposta_usuario1 = float(resposta_usuario1)
    print(f'O tipo primitivo do valor, {resposta_usuario1} é {cores["amarelo"]}float{cores["limpa"]}')
