#!/usr/bin/env python3


from sys import stdin

values = {}
rev_values = {}

def equation(eqs):
    if not all([eqs[i] in rev_values for i in range(0, len(eqs), 2)]):
        return "unknown"
    a = rev_values[eqs[0]]
    for i in range(1, len(eqs), 2):
        op = eqs[i]
        b = rev_values[eqs[i+1]]
        if op == "+":
            a += b
        else:
            a -= b
    return values[a] if a in values else "unknown"


for line in stdin:
    cmd, *rest = line.split()
    if cmd == "clear":
        values = {}
        rev_values = {}
    elif cmd == "def":
        a, b = rest[0], int(rest[1])
        if a in rev_values:
            del values[rev_values[a]]
        rev_values[a] = b
        values[b] = a
    else:
        print(" ".join(rest), equation(rest[:-1]))
