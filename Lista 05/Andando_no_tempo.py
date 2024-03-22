a, b, c = map(int, input().split())
# 0 1 2
#condições para viajar para o presente:
if (a + c == b) or \
   (b + c == a) or \
   (a + b == c) or \
   (a - c == 0) or \
   (a - b == 0) or \
   (b - c == 0):
    print('S')

elif (a > b + c) or \
     (b > a + c) or \
     (c > b + a) or \
     (c > a + b) or \
     (a + b + c == 0):
      print("N")
      
elif (a == 0 and b == 0) or \
     (a == 0 and c == 0) or \
     (b == 0 and c == 0):
        print('N')