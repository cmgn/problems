#!/usr/bin/env python3


from collections import defaultdict
from heapq import heappop, heappush


n, t = map(int, input().split())
customers = defaultdict(list)

for _ in range(n):
  cash, time = map(int, input().split())
  customers[time].append(cash)

amounts = []
total = 0

for _t in reversed(range(t)):
    for price in customers[_t]:
        heappush(amounts, -price)
    if amounts:
        total += heappop(amounts)

print(-total)