n = int(input())
x = int(input())

num = 1
m = 0
count = 0

while m < x:
    m = num * n
    if m < x:
        count += 1
    num += 1

print(f'O numero {n} tem {count} multiplos menores que {x}.')
