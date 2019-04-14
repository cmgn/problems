ncases = int(input())
for i in range(ncases):
    k, b, n = map(int, input().split())
    total = 0
    while n > 0:
        n, digit = divmod(n, b)
        total += digit * digit
    print(k, total)

