
calculo = [int(x) for x in input().split(' ')]

if ((calculo[0] + calculo[1] < calculo[2]) | (calculo[0] + calculo[2] < calculo[1]) | (calculo[1] + calculo[2] < calculo[0])):
  print("N")
else:
  print("S")