#!/usr/bin/env python3


for case in range(int(input())):
    t = [int(x) for x in  input().split()]
    n = t[0]
    students = t[1:]
    average = sum(students) / n
    above_a = len([s for s in students if s > average]) / n
    print("{:.3f}%".format(above_a * 100))
