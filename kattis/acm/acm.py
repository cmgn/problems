#!/usr/bin/env python3


from collections import defaultdict


penalties = defaultdict(int)
solved = set()
time_penalty = 0

line = input()
while line != "-1":
    time, problem_id, result = line.split()
    time = int(time)
    if result == "right":
        time_penalty += time
        time_penalty += penalties[problem_id] * 20
        solved.add(problem_id)
    else:
        penalties[problem_id] += 1
    line = input()


print(len(solved), time_penalty)
