#!/usr/bin/env python3


def is_arithmetic(a):
    d = a[0] - a[1]
    i = 1
    while i < len(a) and a[i-1] - a[i] == d:
        i += 1
    return i >= len(a)


n = int(input())
for _ in range(n):
    a = [int(x) for x in input().split()][1:]
    if is_arithmetic(a):
        print("arithmetic")
        continue
    a.sort()
    if is_arithmetic(a):
        print("permuted arithmetic")
    else:
        print("non-arithmetic")
