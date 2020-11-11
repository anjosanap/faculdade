"""Crie uma função que receba como parâmetros um valor inteiro x, um vetor de inteiros v e seu tamanho n. A função deve
devolver um valor booleano indicando se x está em v. """


# VERSAO WHILE
def busca1(x, v, n):
    i = 0
    while i < n:
        if x == v[i]:
            return True
        return False


# VERSAO FOR
def busca2(x, v, n):
    for i in range(n):
        if x == v[i]:
            return True
        return False
