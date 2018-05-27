#!/usr/bin/env python3

from sys import stdin


def main():
    for line in stdin:
        xs = [int(x) for x in line.split()]
        sum_of_numbers = sum(xs)
        i = 0
        while i < len(xs) and sum_of_numbers - xs[i] != xs[i]:
            i += 1
        print(xs[i])


if __name__ == '__main__':
    main()
