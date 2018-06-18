#!/usr/bin/env python3


n = int(input())
while n:
    bits = ["?"] * 32
    for _ in range(n):
        instr, *args = input().split()
        a = bits[31-int(args[0])]
        if instr in ("SET", "CLEAR"):
            bits[31-int(args[0])] = int(instr == "SET")
        elif instr == "AND":
            b = bits[31-int(args[1])]
            if a == 0 or b == 0:
                bits[31-int(args[0])] = 0
            elif b == "?":
                bits[31-int(args[0])] = "?"
        elif instr == "OR":
            b = bits[31-int(args[1])]
            if a == 1 or b == 1:
                bits[31-int(args[0])] = 1
            elif b == "?":
                bits[31-int(args[0])] = "?"
    print("".join(map(str, bits)))
    n = int(input())
