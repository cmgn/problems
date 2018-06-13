#!/usr/bin/env python3


s = input()
o = []
i = 0
while i < len(s):
    seq = s[i:i+3]
    if "R" in seq and "B" in seq and "L" in seq:
        o.append("C")
        i += 3
        continue
    # using a dict would end up slowing this down
    elif s[i] == "R":
        o.append("S")
    elif s[i] == "B":
        o.append("K")
    else:
        o.append("H")
    i += 1


print("".join(o))
