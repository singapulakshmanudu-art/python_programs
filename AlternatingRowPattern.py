n = 5
for i in range(4):
    if i % 2 == 0:
        print(*range(1, n + 1))
    else:
        print(*range(n, 0, -1))
