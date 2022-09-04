inp = int(input(""))
count = 0

for i in range(inp, inp*3):
    if i%2 != 0:
        count += 1
        print(i)
        if count > 5:
            break
