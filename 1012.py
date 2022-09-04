entrada = input()
l = entrada.split()

a = l[0].strip("'[]")
b = l[1].strip("'[]")
c = l[2].strip("'[]")

a = float(a)
b = float(b)
c = float(c)


triangulo = (c * a) / 2
circulo = 3.14159 * (c**2)
trapezio = ((a+b) * c) / 2
quadrado = b**2
retangulo = a * b

print("TRIANGULO: %.3f" % triangulo)
print("CIRCULO: %.3f" % circulo)
print("TRAPEZIO: %.3f" % trapezio)
print("QUADRADO: %.3f" % quadrado)
print("RETANGULO: %.3f" % retangulo)

