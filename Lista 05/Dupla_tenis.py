a = int(input())
b = int(input())
c = int(input())
d = int(input())

# nivel_1_possivel = a + b
# nivel_2_possivel = a + c
# nivel_3_possivel = a + d
# nivel_4_possivel = b + c
# nivel_5_possivel = b + d
# nivel_6_possivel = c + d

diferencas = [
    abs((a + b) - (c + d)),
    abs((a + c) - (b + d)),
    abs((a + d) - (b + c))
]
menor_diferenca = min(diferencas)

print(menor_diferenca)