valor_item = int(input())
quantidade = int(input())
pagamento = int(input())

calculo = (valor_item * quantidade)
troco = pagamento - calculo
print(f"A pagar: {calculo}")
print(f"Troco  : {troco}")