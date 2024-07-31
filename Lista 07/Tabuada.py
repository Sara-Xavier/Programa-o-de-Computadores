def tabuada(numeros, n):
    
    if n < 0:
        return False
    else: 
        return [x * n for x in numeros]



numeros = [1,2,3,4,5,6,7,8,9,10]
n = int(input())
z = tabuada(numeros, n)

for i in range(len(numeros)):
    print(f"{numeros[i]} x {n} = {z[i]}")

