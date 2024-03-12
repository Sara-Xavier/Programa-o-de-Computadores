consumo_g = int(input())
distancia = int(input())
espaco_tanque = int(input())

abastecimento = (distancia/consumo_g)
combustivel_final = abastecimento - espaco_tanque

if combustivel_final < 0:
    print(0.0)
else:
    print(f'{combustivel_final:.1f}')