peca1 = input()
l = peca1.split()
qnt1 = []
vl1 = []

qnt1.append(l[1])
vl1.append(l[2])

q1 = str(qnt1).strip("'[]'")
q1 = float(q1)

v1 = str(vl1).strip("'[]'")
v1 = float(v1)

valor1 = q1 * v1


peca2 = input()
l = peca2.split()
qnt2 = []
vl2 = []

qnt2.append(l[1])
vl2.append(l[2])

q2 = str(qnt2).strip("'[]'")
q2 = float(q2)

v2 = str(vl2).strip("'[]'")
v2 = float(v2)

valor2 = q2 * v2

valor_total = valor1 + valor2

print("VALOR A PAGAR: R$ %.2f" % valor_total)
