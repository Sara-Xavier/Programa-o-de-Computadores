D = int(input()) #Distância
V = int(input()) #Velocidade em KM/H
calculo = (D / V)
horas = int(calculo)
minutos = int((calculo - int(calculo)) * 60)

print(f"{(horas):02d}:{(minutos):02d}")

