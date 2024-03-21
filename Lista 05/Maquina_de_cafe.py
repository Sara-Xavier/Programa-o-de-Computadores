primeiro_andar = int(input())
segundo_andar = int(input())
terceiro_andar = int(input())
 
minutos_no_primeiro_andar = (segundo_andar * 2) + (terceiro_andar * 4)
minutos_no_segundo_andar = (primeiro_andar * 2) + (terceiro_andar * 2)
minutos_no_terceiro_andar = (primeiro_andar * 4) + (segundo_andar * 2)
 
if minutos_no_primeiro_andar <= minutos_no_segundo_andar and minutos_no_primeiro_andar <= minutos_no_terceiro_andar:
    print(minutos_no_primeiro_andar)
elif minutos_no_segundo_andar <= minutos_no_primeiro_andar and minutos_no_segundo_andar <= minutos_no_terceiro_andar:
    print(minutos_no_segundo_andar)
elif minutos_no_terceiro_andar <= minutos_no_primeiro_andar and minutos_no_terceiro_andar <= minutos_no_segundo_andar:
    print(minutos_no_terceiro_andar)