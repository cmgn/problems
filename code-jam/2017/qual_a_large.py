#!/usr/bin/env python3


number_of_cases = int(input())

for case in range(number_of_cases):
    state, size = input().split()
    size = int(size)
    state = list(state)
    flips = 0
    for i in range(len(state)-size+1):
        if state[i] == "+":
            continue
        for j in range(size):
            state[i+j] = "-" if state[i+j] == "+" else "+"
        flips += 1
    if not all((c == "+" for c in state)):
        print(f"Case #{case+1}: IMPOSSIBLE")
    else:
        print(f"Case #{case+1}: {flips}")
