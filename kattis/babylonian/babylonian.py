#!/usr/bin/env python3


n = int(input())


for _ in range(n):
    xs = [int(x) if x else 0 for x in input().split(",")]
    total = 0
    for k, v in enumerate(reversed(xs)):
        total += v * int(60 ** k)
    print(total)
