def ocorrencias(x, v, n):
    qtd = 0
    i = 0
    while i < n:
        if v[i] == x:
            qtd += 1
        i += 1
    return qtd


def preenche(v, n):
    i = 0
    while i < n:
        v[i] = int(input('v[%d] = ' % i))
        i += 1


n = 10
v = n * [0]
preenche(v, n)
x = int(input('Valor buscado: '))
ocor = ocorrencias(x, v, n)
print('Ocorrências de %d no vetor: %d' % (x, ocor))
