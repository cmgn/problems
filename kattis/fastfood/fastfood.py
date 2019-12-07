
n = int(input())
for _ in range(n):
    n, m = map(int, input().split())
    required = {}
    for _ in range(n):
        _, *stickers, value = map(int, input().split())
        required[tuple(stickers)] = value
    inventory = {(i + 1): v
                 for i, v in enumerate(map(int, input().split()))}
    total = sum(val * min(inventory[k] for k in ks)
                for ks, val in required.items())
    print(total)
