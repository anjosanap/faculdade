n = int(input())


def validation():
    if n % 2 != 0:
        print("O numero", n, "eh impar!")
    else:
        print("O numero", n, "eh par!")
    return


validation()
