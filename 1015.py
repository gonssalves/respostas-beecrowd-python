p1 = input()
l1 = p1.split()

x1 = l1[0]
y1 = l1[1]

x1 = float(x1)
y1 = float(y1)

p2 = input()
l2 = p2.split()

x2 = l2[0]
y2 = l2[1]

x2 = float(x2)
y2 = float(y2)

distancia = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

print("%.4f" % distancia)
