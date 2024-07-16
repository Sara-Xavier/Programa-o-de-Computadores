def primo(n):
    if n <= 1:
        return False

    qtd = 0
    for i in range(1, n + 1):
        if n % i == 0:
            qtd += 1

    return qtd == 2

n = int(input())
x = primo(n)
print(x)
