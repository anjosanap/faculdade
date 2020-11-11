def count_list():
    entrada = input()
    lista = entrada.split()

    inteiros = []

    for n in lista:
        inteiros.append(int(n))

    while True:
        comandos = input()

        if 'inserir' in comandos:
            valor = int(comandos.split()[1])
            inteiros.append((valor))

        elif 'remover' in comandos:
            valor = int(comandos.split()[1])
            inteiros.remove((valor))

        elif comandos == 'parcial':
            print(*sorted(inteiros), sep=' ')

        else:
            print(*sorted(inteiros), sep=' ')
            exit()


count_list()
