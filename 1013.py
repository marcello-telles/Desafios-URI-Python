inp = input().split()
a, b, c = float(inp[0]), float(inp[1]), float(inp[2])
maiorAB = (a+b+abs(a-b))/2
maiorABC = (maiorAB+c+abs(maiorAB-c))/2
print('%d eh o maior' % maiorABC)
