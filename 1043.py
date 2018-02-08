inp = input().split()
a, b, c = float(inp[0]), float(inp[1]), float(inp[2])
if (a > abs(b - c) and a < b + c):
    print('Perimetro = %.1f' %(a+b+c))
else:
    area = ((a+b)*c)/2
    print('Area = %.1f' % area)
