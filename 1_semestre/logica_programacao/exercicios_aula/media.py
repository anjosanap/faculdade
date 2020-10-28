def exibe_media (n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    print(media)


def retorna_media(num1, num2, num3):
    media = (num1 + num2 + num3)
    return media


a = int(input('A: '))
b = int(input('B: '))
c = int(input('C: '))

x = exibe_media(a, b, c)
print(x)

y = retorna_media(a, b, c)
print(y)