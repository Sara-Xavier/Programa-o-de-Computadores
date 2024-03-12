A_1_1 , A_1_2 = map(int,input().split())
A_2_1 , A_2_2 = map(int,input().split())
P1, P2 = map(int,input().split())
 
media_A_1 = ((A_1_1 * P1) + (A_1_2 * P2 )) // (P1 + P2)
media_A_2 = ((A_2_1 * P1) + (A_2_2 * P2 )) // (P1 + P2)
 
if media_A_1 >= media_A_2:
    print("1")
else:
    print("2")