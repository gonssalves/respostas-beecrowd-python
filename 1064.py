######POSITIVOS E MÉDIA
positivos = 0
count = 0
for i in range(6):
    num = float(input())
    if num > 0:
        count += 1
        positivos += num

media = positivos / count

print(f'{count} valores positivos')
print(f'{media:.1f}')
