def quociente(a, b):
    q = 0
    while a >= b:
        a -= b
        q += 1
    return q


def resto(a, b):
    while a >= b:
        a -= b
    return a


x = int(input('dividendo: '))
y = int(input('divisor: '))
z = quociente(x, y)
print('quociente: %d' % z)
z = resto(x, y)
print('resto: %d' % z)
