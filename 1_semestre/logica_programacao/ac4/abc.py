def misterio(a, b):
    while a > 0:
        c = 1
        while c <= a:
            print(b)
            c += 1
        b -= 1
        a -= 1
    return a + b


print(misterio(4, 7))
