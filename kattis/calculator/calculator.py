#!/usr/bin/env python3

from sys import stdin


for line in stdin:
    result = eval(line)
    print("{:.2f}".format(result))

