#!/usr/bin/env python3


from functools import reduce


def main():
    r = [2, 3, 5, 7, 11, 13, 17, 19]
    maximum = 1
    total = 0
    for k, v in enumerate([int(x) for x in input().split()]):
        total += maximum * v
        maximum *= r[k]
    print(maximum - (total + 1))


if __name__ == "__main__":
    main()

