#!/usr/bin/env python3


t = int(input())
for _ in range(t):
    input()
    n = int(input())
    t = 0
    for _ in range(n):
        t += int(input())
    print("YES" if t % n == 0 else "NO")