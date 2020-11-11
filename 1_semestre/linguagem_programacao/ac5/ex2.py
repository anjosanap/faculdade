def sorteio():
    num = input()
    number = num.split()

    alunos = []
    n = number[0]
    k = number[1]

    for i in range(1, int(n) + 1):
        nomes = input()
        alunos.append(nomes)
        alunos.sort()

    print(alunos[int(k) - 1])


sorteio()
