#!/usr/bin/env python3

from collections import OrderedDict


def main():
    teams = OrderedDict()
    n = int(input())
    for _ in range(n):
        a, b = input().split()
        if a not in teams and len(teams) < 12:
            teams[a] = b
    print("\n".join(a + " " + b for a, b in teams.items()))


if __name__ == '__main__':
    main()
