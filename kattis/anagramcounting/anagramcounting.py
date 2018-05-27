#!/usr/bin/env python3


from math import factorial
from functools import reduce
from sys import stdin


for word in stdin:
    word = word.strip()
    characters = [word.count(c) for c in set(word)]
    numerator = factorial(len(word))
    denom = reduce(int.__mul__, (factorial(n) for n in characters))
    print(numerator // denom)
