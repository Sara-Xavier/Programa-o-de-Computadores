nome = input()
nome_strip = nome.strip()
horas_trabalhadas = int(input())
pagamento = float(input())

calculo = (horas_trabalhadas * pagamento)


print(f"{nome_strip}" [0:21])
print(f"R$ {calculo:.2f}")