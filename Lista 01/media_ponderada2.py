v1, v2 = input().split()
p1, p2 = input().split()
v1 = int(v1)
v2 = int(v2)
p1 = int(p1)
p2 = int(p2)


media_poderada = ((v1 * p1) + (v2 * p2)) // (p1 + p2)
print(media_poderada)