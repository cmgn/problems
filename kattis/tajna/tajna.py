message = input()

n = len(message)
r, c = max(
    [(r, c) for r in range(n + 1) for c in range(n + 1) if r * c == n and r <= c],
    key=lambda t: t[0],
)
for i in range(r):
    for j in range(c):
        print(message[r * j + i], end="")
print("")
