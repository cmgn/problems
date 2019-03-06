from math import sqrt

n = int(input())
for _ in range(n):
    s = input()
    l = len(s)
    m = int(sqrt(l))
    for j in range(m - 1, -1, -1):
        for i in range(m):
            print(s[i * m + j], end="")
    print()
