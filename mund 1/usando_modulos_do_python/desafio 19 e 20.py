from random import shuffle, choice
print('{0}sortei de aluno{0}'.format('='*10))
aluno1 = input('Qual o nome do aluno ')
aluno2 = input('Qual o nome do aluno ')
aluno3 = input('Qual o nome do aluno ')
aluno4 = input('Qual o nome do aluno ')
alunos = [aluno1, aluno2, aluno3, aluno4]
aluno_escolhido = choice(alunos)
print('O aluno escolhido para apagar o quadro foi: {}'.format(aluno_escolhido))
print('Agora este professor quer sortear a ordem de apresentação de um trabalho')
shuffle(alunos)
print('A lista para a apresentação será assim: {}'.format(alunos))