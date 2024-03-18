refeicao_disponivel = list(map(int, input().split()))
refeicao_requisitada = list(map(int, input().split()))

nao_atendidos = [max(0, refeicao_requisitada[i] - refeicao_disponivel[i]) for i in range(3)]

total = sum(nao_atendidos)
print(total)