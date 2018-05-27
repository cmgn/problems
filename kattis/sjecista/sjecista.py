#!/usr/bin/env python3
# https://en.wikipedia.org/wiki/Pentatope_number


n = int(input())

if n == 3:
    print(0)
else:
    n -= 3
    m = n * (n + 1) * (n + 2) * (n + 3)
    m //= 24
    print(m)
