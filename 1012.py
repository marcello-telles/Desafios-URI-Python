pi = 3.14159
inp = input().split()
a, b, c = float(inp[0]), float(inp[1]), float(inp[2])
triang = a * c / 2
circ = pi * c**2
trap = (a + b) * c / 2
quad = b**2
retang = a * b
print('TRIANGULO: %.3f' % (triang))
print('CIRCULO: %.3f' % (circ))
print('TRAPEZIO: %.3f' % (trap))
print('QUADRADO: %.3f' % (quad))
print('RETANGULO: %.3f' % (retang))
