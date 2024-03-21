creditos = list(map(int, input().split()))
#condições para viajar para o presente:
if (creditos[0] + creditos[2] == creditos[1])  or (creditos[1] + creditos[2] == creditos[0]) or (creditos[0] + creditos[1] == creditos[2]) or (creditos[0] - creditos[2] == 0) or (creditos[0] - creditos[1] == 0) or (creditos[1] - creditos[2] == 0):
    print('S')

elif (creditos[0] > creditos[1] + creditos[2]) or (creditos[1] > creditos[0] + creditos[2]) or (creditos[2] > creditos[1] + creditos[0]):
    print("N")