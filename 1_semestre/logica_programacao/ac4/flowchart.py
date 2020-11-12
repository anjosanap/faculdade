# x = int(input())
# y = int(input())

x = 100
y = 200

i = 0

bomdia = 0
boatarde = 0
boanoite = 0
while i < x:
    print('bom dia')
    bomdia += 1
    j = 0

    while j < y:
        boatarde += 1
        print('boa tarde')
        j += 1
    i += 1

boanoite += 1
print(bomdia, 'bom dia')
print(boatarde, 'boa tarde')
print(boanoite, 'boa noite')
