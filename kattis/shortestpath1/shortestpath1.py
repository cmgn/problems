#!/usr/bin/env python3


from heapq import heappop, heappush


def dijkstra(a, s):
    d = {}
    q = [(0, s)]
    while q:
        c, u = heappop(q)
        if u in d: continue
        d[u] = c
        for v, w in a[u]:
            if v not in d: heappush(q, (c + w, v))
    return d


n, m, q, s = [int(x) for x in input().split()]
while n or m or q or s:
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = input().split()
        g[int(u)].append((int(v), int(w)))
    d = dijkstra(g, s)
    for _ in range(q):
        r = int(input())
        print(d[r] if r in d else "Impossible")
    print()
    n, m, q, s = [int(x) for x in input().split()]
