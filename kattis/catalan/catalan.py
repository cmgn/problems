#!/usr/bin/env python3


from math import factorial


n = int(input())
for _ in range(n):
    m = int(input())
    print(int((factorial(2 * m))//(factorial(m + 1) * factorial(m))))