#!/usr/bin/env python3


number_of_cases = int(input())


for case in range(number_of_cases):
    n = [int(x) for x in input()]
    N = len(n)
    for i in range(N - 1, 0, -1):
        if n[i] >= n[i-1]:
            continue
        n[i-1] -= 1
        for j in range(i, N):
            n[j] = 9
    n = "".join(map(str, [int(c) for c in n]))
    print(f"Case #{case+1}: {int(n)}")
