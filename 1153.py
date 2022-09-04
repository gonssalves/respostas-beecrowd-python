def fatorial(n):
    if n == 0: return 1
    else: return fatorial(n-1) * n
    
inp = int(input())

resultado = fatorial(inp)
print(resultado)
