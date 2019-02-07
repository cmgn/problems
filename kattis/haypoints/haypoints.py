#!/usr/bin/env python3

from sys import stdin


lines = stdin.readlines()

n, m = [int(x) for x in lines[0].split()]

values = {}

i = 1
for _ in range(n):
    name, value = lines[i].split()
    values[name] = int(value)
    i += 1

for _ in range(m):
    total = 0
    while lines[i] != ".\n":
        words = lines[i].split()
        total += sum(values.get(word, 0) for word in words)
        i += 1
    i += 1
    print(total)

