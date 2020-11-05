def main():
    entrada_usuario = input()
    conta_digitos(entrada_usuario)


def conta_digitos(entrada_usuario):
    digitos = 0
    for _ in entrada_usuario:
        digitos += 1
    print(digitos)


main()
