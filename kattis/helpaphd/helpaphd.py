#!/usr/bin/env python3

for _ in range(int(input())):
    line = input()
    if "+" in line:
        a, b = map(int, line.split("+"))
        print(a + b)
    else:
        print("skipped")
