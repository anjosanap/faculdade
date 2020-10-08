a = float(input())
b = float(input())
c = float(input())


if not (a < b + c and b < a + c and c < a + b):
    print('inválido')
else:
    if a == b and b == c:
        print('equilátero')
    else:
        if a == b or a == c or b == c:
            print('isósceles')
        else:
            print('escaleno')
