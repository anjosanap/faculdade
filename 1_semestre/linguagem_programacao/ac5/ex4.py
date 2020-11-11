def compras():
    cod_produto = []
    unidades = []
    precos = []
    total = []

    while True:
        try:
            entrada = input()
            itens = entrada.split()

            codigo = itens[0]
            if codigo == '0':
                break

            quantidade = int(itens[1])
            preco = float(itens[2])
            custo = quantidade * preco

            cod_produto.append(codigo)
            unidades.append(quantidade)
            precos.append(preco)
            total.append(custo)
        except EOFError:
            break

    if not cod_produto:
        print('nao tem compras')

    else:
        custos_sorted = sorted(total)
        caro = custos_sorted[- 1]
        aux = total.index(caro)
        cod = cod_produto[aux]
        qtd = unidades[aux]

        print(f'Item mais caro\nCodigo: {cod}\nQuantidade: {qtd}\nCusto: {caro:.2F}')


compras()
