notas = [100, 50, 20, 10, 5, 2, 1]
n = int(input())
print(n)
for i in notas:
    print("%d nota(s) de R$ %d,00" % (n // i, i))
    n = n % i
