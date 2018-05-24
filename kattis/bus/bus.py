#!/usr/bin/env python3

for _ in range(int(input())):
    m = int(input()) - 1
    people = 1
    for _ in range(m):
        people = (people + 0.5) * 2
    print(int(people))
