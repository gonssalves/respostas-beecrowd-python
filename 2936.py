gramas = [300, 1500, 600, 1000, 150]
l = []

for i in gramas:
    porcoes = int(input())
    total= i * porcoes    
    l.append(total)
    
print(sum(l) + 225) 
