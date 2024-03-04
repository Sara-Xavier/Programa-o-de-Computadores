nome = input()
salario_base = float(input())
total_vendas = float(input())
nome_strip = nome.strip()


calculo = (salario_base + (0.15 * total_vendas))


print(f"{nome_strip}" [0:21])
print(f"R$ {calculo:.2f}")