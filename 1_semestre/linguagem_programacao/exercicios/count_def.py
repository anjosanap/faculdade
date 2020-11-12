import random


def verifica_aluno(fileira, cadeira):
    return random.randint(0, 1)


def percorre_cadeiras(fileira):
    soma_parcial = 0
    cadeira = 1
    while cadeira <= 3:
        tem_aluno = verifica_aluno(fileira, cadeira)
        print('Verificando cadeira {}: {}'.format(cadeira, tem_aluno))
        soma_parcial += tem_aluno
        cadeira += 1
    return soma_parcial


def percorre_fileiras(sala):
    soma = 0
    fileira = 1
    while fileira <= 5:
        print('contando afileira', fileira)
        soma_parcial = percorre_cadeiras(fileira)
        print('A fileira {} tem {} alunos.'.format(fileira, soma_parcial))
        soma += soma_parcial
        fileira += 1
    print('A sala {} tem {} alunos:'.format(sala, soma))


percorre_fileiras('B314')
print('fim')
