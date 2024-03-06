c,q = map(int,input().split())

hotdog=4.00*q
salada=4.5*q
xbacon=5*q
torrada=2*q
refri=1.5*q

if(c == 1):
    print("Total: R$",f'{hotdog:.2f}')
if(c == 2):
    print("Total: R$",f'{salada:.2f}')
if(c == 3):
    print("Total: R$",f'{xbacon:.2f}')
if(c == 4):
    print("Total: R$",f'{torrada:.2f}')
if(c == 5):
    print("Total: R$",f'{refri:.2f}')