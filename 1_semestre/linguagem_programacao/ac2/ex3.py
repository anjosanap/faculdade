a = int(input())
b = int(input())


def validate():
    if a > b:
        print("A eh maior")
    elif a == b:
        print("iguais")
    else:
        print("B eh maior")
    return


validate()
