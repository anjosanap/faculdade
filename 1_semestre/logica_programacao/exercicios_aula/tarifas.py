tipo = input('Tipo: ')
quantidade = int(input('Quantidade: '))

if tipo == 'D':
    if quantidade <= 50:
        tarifa = 200.00
    else:
        tarifa = 120.00
else:
    if quantidade <= 50:
        tarifa = 100.00
    else:
        tarifa = 80.00

total = quantidade * tarifa
print('Tarifa: R$ %.2f' % tarifa)
print('Total: R$ %.2f' % total)