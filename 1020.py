tot = int(input())
tmp = tot % 365
print(tot // 365, "ano(s)")
print(tmp // 30, "mes(es)")
print(tmp % 30, "dia(s)")
