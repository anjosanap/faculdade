v = 10 * [0]
i= 0

while i < 10:
    v[i] = int(input('V[%d] = ' % i))
    i += 1
m = v[0]
i = 0

while i < 10:
    if v[i] < m:
        m = v[i]
    else:
        i += 1

print('Menor: ', m)
