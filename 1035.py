num = input()

l = num.split()

a = int(l[0])
b = int(l[1])
c = int(l[2])
d = int(l[3])

soma1 = c + d
soma2 = a + b
resto = a % 2

if b > c and d > a and soma1 > soma2 and c > 0 and d > 0 and resto == 0:
    print("Valores aceitos")

else:
    print("Valores nao aceitos")
