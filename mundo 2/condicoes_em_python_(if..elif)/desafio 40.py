cores = {
"limpa": '\033[m',
"magenta": '\033[35m',
"amarelo": '\033[33m'
} 

nome_aluno = input(f'{cores["amarelo"]}Qual o nome completo do aluno:{cores["limpa"]} ').title()

nota_1 = float(input('Nota do aluno no primeiro semestre: ')) 
nota_2 = float(input('Nota do aluno no segundo semestre: '))
media = (nota_1 + nota_2) / 2 # media das duas notas

if media < 5:
    print(f'O aluno, {cores["magenta"]}{nome_aluno}{cores["limpa"]} ,está reprovado no ano letivo!')
elif media >= 5 and media <= 6.9:
    print(f'O aluno, {cores["magenta"]}{nome_aluno}{cores["limpa"]}, está de recuperação no ano letivo')
else: 
    print(f'O aluno, {cores["magenta"]}{nome_aluno}{cores["limpa"]}, está aprovado nesse ano letivo')
