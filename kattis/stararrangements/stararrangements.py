#!/usr/bin/env python3


n = int(input())

print(str(n) + ":")

for i in range(2, n):
    if n % (2*i-1) in (0, i):
        print("{},{}".format(i, i-1))
    if n % i == 0:
        print("{},{}".format(i, i))
