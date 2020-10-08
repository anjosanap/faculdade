salario = float(input())


def inss():
    if salario <= 1751.81:
        desconto = round(salario * 0.08, 2)
        print("Desconto do INSS: R$", "%.2f" % desconto)
    else:
        if 1751.82 <= salario <= 2919.72:
            desconto = round(salario * 0.09, 2)
            print("Desconto do INSS: R$", "%.2f" % desconto)
        else:
            if 2919.72 < salario <= 5839.45:
                desconto = salario * 0.11
            else:
                if salario > 5839.45:
                    desconto = 5839.45 * 0.11

            print("Desconto do INSS: R$", "%.2f" % desconto)


inss()
