a, b , c = map(int, input().split())

if a + b + c > 0 and abs(a) + abs(b) + abs(c) >= max(abs(a), abs(b), abs(c)):
    print("S")  
else:
    print("N")