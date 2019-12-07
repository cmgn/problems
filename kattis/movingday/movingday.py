n, V = map(int, input().split())
biggest = 0
for _ in range(n):
    i, j, k = map(int, input().split())
    biggest = max(biggest, i*j*k)
print(biggest - V)
