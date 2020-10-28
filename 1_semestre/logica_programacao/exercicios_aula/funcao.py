
def quociente(x, y):
    q = 0
    while x >= y:
        x -= y
        q += 1
    return q


a = int(input('a: '))
b = int(input('b: '))
q = quociente(a, b)
print('%d // %d = %d' % (a, b, q))
