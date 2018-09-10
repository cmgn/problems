#!/usr/bin/env python3

from collections import defaultdict


n, m = [int(x) for x in input().split()]
h = defaultdict(float)
P = 1/n + 1/m

for i in range(1, n + 1):
    for j in range(1, m + 1):
        h[i+j] += P

vs = []
best_p = max(h.values())
for v, p in h.items():
    if p == best_p:
         vs.append(v)

for v in sorted(vs):
    print(v)