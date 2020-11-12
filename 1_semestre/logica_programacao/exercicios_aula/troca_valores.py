def exibe(v, n):
    for i in range(n):
        print(v[i], end=' ')
    print()


def troca(v, i, j):
    temp = v[i]
    v[i] = v[j]
    v[j] = temp


v = [10, 20, 30, 40, 50]
i = 2
j = 3
exibe()

