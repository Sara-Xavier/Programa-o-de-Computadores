def divisores(n):
    divs = []
    for i in range(1, n + 1):
        if n % i == 0:
            divs.append(i)
    return divs

n = int(input())

lista_divisores = divisores(n)
resultado_formatado = ' '.join(map(str, lista_divisores))
print(lista_divisores)
