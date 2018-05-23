#!/usr/bin/env python3


from functools import reduce
from collections import defaultdict


def product(l): return 


for _ in range(int(input())):
    lookup = defaultdict(list)
    for _ in range(int(input())):
        item, category = input().split()
        lookup[category].append(item)
    # -1 because there must be at least one item on the spy
    try:
        print(reduce(int.__mul__, ([len(lookup[category]) + 1 for category in lookup])) - 1)
    except TypeError:  # thrown if there are 0 categories
        print(0)
