seg = int(input())
hora = seg // 3600
seg = seg % 3600
minuto = seg // 60
seg = seg % 60
print('%d:%d:%d' % (hora, minuto, seg))
