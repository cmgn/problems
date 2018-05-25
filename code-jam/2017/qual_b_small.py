#!/usr/bin/env python3


number_of_cases = int(input())


def is_sorted(s):
    i = 1
    while i < len(s) and s[i] >= s[i-1]:
        i += 1
    return i >= len(s)


for case in range(number_of_cases):
    n = int(input())
    while not is_sorted(str(n)):
        n -= 1
    print(f"Case #{case+1}: {n}")
