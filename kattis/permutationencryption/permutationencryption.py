#!/usr/bin/env python3


s = input()
while s != "0":
    n, *p = [int(x) for x in s.split()]
    s = input()
    if len(s) % n != 0:
        s += " " * (n - (len(s) % n))
    gs = [list(s[i:i+n]) for i in range(0, len(s), n)]
    for k, g in enumerate(gs):
        l = [" "] * len(g)
        for _k, _p in enumerate(p):
            l[_k] = g[_p-1]
        gs[k] = "".join(l)
    print("'" + "".join(g for g in gs) + "'")
    s = input()