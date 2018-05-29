#!/usr/bin/env python3


from collections import defaultdict
from functools import reduce


n = int(input())
while n:
    hashes = defaultdict(list)
    sentences = set()
    for i in range(n):
        s = input()
        hashes[reduce(int.__xor__, map(ord, s), 0)].append(s)
        sentences.add(s)
    # slow but works
    print(len(sentences),
          sum(sum(1 for a in hash_ for b in hash_ if a != b)//2 for hash_ in hashes.values()))
    n = int(input())
