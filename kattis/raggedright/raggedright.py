#!/usr/bin/env python3


from sys import stdin


lines = [line.strip() for line in stdin]
n = len(max(lines, key=len))
raggedness = [(n - len(l))**2 for l in lines[:-1]]
print(int(sum(raggedness)))