entrada = input("")

lista = entrada.split()

codigo = int(lista[0])
quant = int(lista[1])

if codigo == 1:
    total = quant * 4.00
    print("Total: R$ %.2f" % total)

elif codigo == 2:
    total = quant * 4.50
    print("Total: R$ %.2f" % total)

elif codigo == 3:
    total = quant * 5.00
    print("Total: R$ %.2f" % total)

elif codigo == 4:
    total = quant * 2.00
    print("Total: R$ %.2f" % total)

elif codigo == 5:
    total = quant * 1.50
    print("Total: R$ %.2f" % total)
