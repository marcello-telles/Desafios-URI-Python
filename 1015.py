import math
ent1, ent2 = input(), input()
x1 = float(ent1.split(' ')[0])
y1 = float(ent1.split(' ')[1])
x2 = float(ent2.split(' ')[0])
y2 = float(ent2.split(' ')[1])
print("%.4f" %(math.sqrt((x2-x1)**2 + (y2-y1)**2)))
