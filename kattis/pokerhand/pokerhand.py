cards = input().split()
counts = {}

for card in cards:
    rank = card[0]
    counts[rank] = counts.get(rank, 0) + 1

print(counts[max(counts, key=lambda k: counts[k])])
