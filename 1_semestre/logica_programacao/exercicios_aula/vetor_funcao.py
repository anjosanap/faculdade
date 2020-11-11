def menor(v, n):
    m = v[0]
    i = 1
    while i < n:
        if v[i] < m:
            m = v[i]
        i += 1
    return m


def preenche(v, n):
    i = 0
    while i < n:
        v[i] = int(input('Vetor[%d] = ' % i))
        i += 1
    return


n = 10
v = n * [0]
preenche(v, n)
m = menor(v, n)

print('Menor: ', m)
