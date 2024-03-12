x = list(map(int, input().split()))
 
x.sort()
 
c, b, a = x
 
if (a >= b + c):
    print("n")
elif (a * a == b * b + c * c):
    print("r")
elif  (a * a <= b * b + c * c):
    print("a")
elif  (a * a >= b * b + c * c):
    print("o")