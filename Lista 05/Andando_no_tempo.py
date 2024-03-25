a, b, c = map(int, input().split())
#condições para viajar para o presente:
if (a + c == b) or \
   (b + c == a) or \
   (a + b == c) or \
   (a == b)     or \
   (a == c)     or \
   (c == b):
    print('S')

else: 
   print('N')

