def bem_vindo():
    print('Bem vindo! Vamos calcular a média :)')

def retorna_media(num1, num2, num3):
    media = (num1 + num2 + num3) / 3
    return media

bem_vindo()

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))

resposta = retorna_media(a, b, c)
print('A média é: ', round(resposta, 2))