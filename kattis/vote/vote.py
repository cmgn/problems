#!/usr/bin/env python3


from collections import defaultdict


n = int(input())
for _ in range(n):
    m = int(input())
    total_votes = 0
    candidates = defaultdict(list)

    for candidate in range(m):
        votes = int(input())
        total_votes += votes
        candidates[votes].append(candidate + 1)

    max_votes = max(candidates.keys())
    if len(candidates[max_votes]) > 1:
        print("no winner")
        continue
    proportion = max_votes / total_votes
    if proportion <= 0.5:
        print("minority winner " + str(candidates[max_votes][0]))
    else:
        print("majority winner " + str(candidates[max_votes][0]))
