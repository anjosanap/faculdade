def entrada():
    n = int(input())
    while n <= 0:
        n = int(input())
    return n


def qtd_divisores(y):
    qtd = 0
    divisor = 1
    while divisor <= y:
        if y % divisor == 0:
            qtd += 1
        divisor += 1
    return qtd


x = entrada()
qtd = qtd_divisores(x)
print(x, 'tem', qtd, 'divisores')
