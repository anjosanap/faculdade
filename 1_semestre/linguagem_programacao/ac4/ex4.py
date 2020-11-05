def main():
    entrada_usuario = input()
    conta_characteres(entrada_usuario)


def conta_characteres(entrada_usuario):
    char = 0
    for _ in entrada_usuario:
        char += 1
    print(char)


main()
