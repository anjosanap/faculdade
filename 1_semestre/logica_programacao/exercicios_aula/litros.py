litros = float(input())
tipo = input()


def total():
    if tipo == 'a':
        valor = litros * 3.8997

    else:
        if tipo == 'd':
            valor = litros * 3.6543
        else:
            valor = litros * 4.4009

    print('valor: R$', round(valor, 2))
    return


total()