inp1, inp2 = input().split(), input().split()
cod1, qtd1, unit1 = int(inp1[0]), int(inp1[1]), float(inp1[2])
cod2, qtd2, unit2 = int(inp2[0]), int(inp2[1]), float(inp2[2])
print('VALOR A PAGAR: R$ %.2f' %(qtd1*unit1+qtd2*unit2))
