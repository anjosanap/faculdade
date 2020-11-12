"""
Crie uma função que receba como parâmetros um valor inteiro
x, um vetor de inteiros v e seu tamanho n. A função deve
devolver um valor inteiro indicando seu índice da primeira ocorrência
de x em v. Observação: caso x não esteja em v, devolver -1
"""


# VERSAO WHILE
def busca1(x, v, n):
    i = 0
    while i < n:
        if x == v[i]:
            return i
        i += 1
    return -1


# VERSAO FOR
def busca2(x, v, n):
    for i in range(n):
        if x == v[i]:
            return i
    return -1
