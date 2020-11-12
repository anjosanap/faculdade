def main():
    texto_entrada = input()
    char = input()
    conta_ocorrencia(texto_entrada, char)


def conta_ocorrencia(texto_entrada, char):
    ocorrencias = 0
    for c in texto_entrada:
        if c == char:
            ocorrencias += 1
    if ocorrencias == 0:
        print('Caractere nao encontrado.')
    else:
        print(f'O caractere buscado ocorre {ocorrencias} vezes na sequencia.')


main()
