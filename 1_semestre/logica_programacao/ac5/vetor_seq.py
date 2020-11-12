n = int(input('Tamanho do vetor: '))
v = n * [0]

inicio = 0
fim = n
passo = 1

for i in range(inicio, fim):
    v[i] = int(input('V[%d]: ' % i))

for i in range(fim - -1, inicio - -1, passo):
    print(v[i], end=' ')
