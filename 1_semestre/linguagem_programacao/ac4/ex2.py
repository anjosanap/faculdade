def calculo_tabuada(number):
    for n in range(1, 10):
        resultado = number * n
        print(f"{number} x {n} = {resultado}")


init_num = int(input())
while init_num > 9 or init_num <= 0:
    print('Insira um número inicial entre 1 e 9')
    init_num = int(input())

end_num = int(input())
while end_num > 9 or end_num <= 0:
    print('Insira um número final entre 1 e 9')
    end_num = int(input())

if init_num > end_num:
    print('Nenhuma tabuada nesse intervalo')
else:
    for n in range(init_num, end_num + 1):
        calculo_tabuada(n)
        print()
