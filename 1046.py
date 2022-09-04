horas = input().split()
l = [int(i) for i in horas]

if l[1] < l[0]:
    dif = 24 -l[0]
    duracao = dif + l[1]
    print(f'O JOGO DUROU {duracao} HORA(S)')
elif l[1] > l[0]:
    duracao = l[1] - l[0]
    print(f'O JOGO DUROU {duracao} HORA(S)')
else: 
    print(f'O JOGO DUROU 24 HORA(S)')
     
