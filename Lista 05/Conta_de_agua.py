consumo = int(input())
assinatura_basica = 7

if consumo > 10:
    if consumo <= 30:
        assinatura_basica += (consumo - 10) *1
    elif consumo <= 100:
        assinatura_basica += (30 - 10) * 1
        assinatura_basica += (consumo - 30) * 2
    else:
        assinatura_basica += (30 - 10) * 1
        assinatura_basica += (100 - 30) * 2
        assinatura_basica += (consumo - 100) * 5


print(assinatura_basica)
        
