A,B,C,D, = map(int, input().split())

if (A + B > C and A + C > B and C + B > A) or (A + B > D and A + D > B and D + B > A) or (A + C > D and A + D > C and D + C > A):
    print("S")
 
elif (B + D > C and B + C > D and D + C > B):
    print("S")
else:
    print("N")
