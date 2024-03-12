A, G, R_a, R_g = map(float,input().split())

calculo = (G * R_a ) / R_g

if calculo <= A:
    print("G")
else:
    print("A")