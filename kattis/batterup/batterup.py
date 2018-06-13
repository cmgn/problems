#!/usr/bin/env python3

input()
xs = [int(x) for x in input().split() if int(x) != -1]
print(sum(xs) / len(xs))
