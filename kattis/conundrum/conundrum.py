#!/usr/bin/env python3

word = "PER"
string = input().upper()
total = 0
for k, v in enumerate(string):
    total += (v != word[k % 3])
print(total)
