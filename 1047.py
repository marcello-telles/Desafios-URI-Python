inp = input().split()
h1, m1, h2, m2 = int(inp[0]), int(inp[1]), int(inp[2]), int(inp[3])
min = m2 - m1
hr = h2 - h1
if m2 < m1:
    min = min + 60

if h2 < h1:
    if min > 0:
        hr = hr + 23
    else:
        hr = hr + 24
else:
    if h2 == h1 and min == 0:
        hr = 24
    else:
        if m2 < m1:
            hr = hr - 1
print('O JOGO DUROU% d HORA(S) E %d MINUTO(S)' %(hr, min))
