b = int(input())
t = int(input())
x = 160 * 70
h =  ((b + t)* 70) / 2
z = x - h
 
if z > h:
    print(2)
 
elif z < h: 
    print(1)
else:
    print(0)