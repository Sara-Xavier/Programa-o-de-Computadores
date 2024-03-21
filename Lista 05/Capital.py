areas = list(map(int, input().split()))
 
if (areas[0] * areas[1] == areas[2] * areas[3]) or (areas[2] * areas[1] == areas[0] * areas[3] or areas[3] * areas[1] == areas[2] * areas[0]) :
    print("S")  
else:
    print("N")  

#malz Jorgiano, no que eu conseguir colocar listas pra eu praticar, vou colocar.