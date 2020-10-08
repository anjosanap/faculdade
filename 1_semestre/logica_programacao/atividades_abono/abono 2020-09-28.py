sb = float(input())
tempo = int(input())
emp = float(input())


def banco():
    if sb > 2000:
        if tempo > 2:
            juros = emp * 0.15
        else:
            juros = emp * 0.20
        print(emp + juros)
        return

    else:
        print('Empréstimo negado')


banco()
