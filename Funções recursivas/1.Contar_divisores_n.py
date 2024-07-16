# 1- Escreva uma função recursiva que receba um inteiro n, não negativo, e retorne a quantidade
# de divisores de n. Assinatura da função: def conta_divisores(n)

def conta_divisores(n, div = None, lista = None): #Usei None para não precisar criar função auxiliar, para fazer diferente dos exemplos dos slides
    if lista is None:                             #eu quis incrementar, então criei uma lista onde todos os números divisores de N aparecem
        lista = []
    
    if div is None:
        div = n

    if div == 1:
        return 1 #se div = 1, retorna 1
    
    if div == 0:
        return lista

    if n % div == 0:
        lista.append(div)

    return 1 + conta_divisores(n, div - 1, lista)
    #se n for divisível por div, soma 1 e chama recursivamente div -1


  

n = int(input())
lista_divisores = [1,]
conta_divisores(n, n, lista_divisores)
lista_divisores.sort()
print(len(lista_divisores)) #print da quantidade de divisores
print(lista_divisores)



