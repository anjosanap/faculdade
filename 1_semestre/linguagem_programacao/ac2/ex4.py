n1 = float(input())
n2 = float(input())
n3 = float(input())

frequencia = float(input())

media = round(((n1 * 2) + (n2 * 2) + (n3 * 3)) / (2 + 2 + 3), 1)
presenca = "{:.0%}".format(frequencia)


def notas():
    print("Frequencia:", presenca)
    print("Media: {0:.1f}".format(media))

    if frequencia < 0.75:
        print("Aluno reprovado por faltas!")

    else:
        if media > 9:
            print("Aluno aprovado com louvor!")

        else:
            if 9 >= media >= 6:
                print("Aluno aprovado!")

            else:
                if 6 > media >= 4:
                    print("Aluno de recuperação!")

                else:
                    if media < 4:
                        print("Aluno reprovado!")

    return


notas()
