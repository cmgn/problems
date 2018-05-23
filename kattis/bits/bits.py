#!/usr/bin/env python3

from sys import stdin

def keyfunc(n):
    return bin(n)[2:].count("1")

stdin.readline()  # ignore number of test cases
for line in stdin:
    digits = [c for c in line.strip()]
    prefixes = [int("".join(digits[:i+1])) for i in range(len(digits))]
    results = [keyfunc(prefix) for prefix in prefixes]
    print(max(results))
