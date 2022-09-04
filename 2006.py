tipo_cha = input()
respostas = input()

lista = respostas.split()

count = 0

for n in lista:
    if n == tipo_cha:
        count += 1
        
print(count)
