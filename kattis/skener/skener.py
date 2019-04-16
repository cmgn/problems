r, c, zr, zc = map(int, input().split())

for _ in range(r):
    s = input()
    for _ in range(zr):
        for c in s:
            print(c * zc, end="")
        print()

