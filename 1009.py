nome = input()
salario_fixo = float(input())
total_vendas = float(input())
comissao = total_vendas * 0.15
salario_comissao = salario_fixo + comissao

print("TOTAL = R$ %.2f" % salario_comissao)
