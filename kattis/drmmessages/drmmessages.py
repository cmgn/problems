#!/usr/bin/env python3

offset = ord("A")
m = input()
a, b = m[:len(m)//2], m[len(m)//2:]
sum_a, sum_b = sum(ord(c) - offset for c in a), sum(ord(c) - offset for c in b)
a = "".join(chr(offset + ((ord(c) - offset + sum_a) % 26)) for c in a)
b = "".join(chr(offset + ((ord(c) - offset + sum_b) % 26)) for c in b)
s = "".join(chr(offset + ((ord(x) + ord(y) - 2*offset) % 26)) for (x, y) in zip(a, b))
print(s)
