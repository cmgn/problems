#!/usr/bin/env python3

import sys
import math


def main():
    while True:
        r, h, s = map(float, input().split())
        if r == h == s == 0:
            break
        angle = 360 - math.degrees(2 * math.acos(r/h))
        arc = 2 * r * math.pi * angle/360
        sides = 2 * math.sqrt(h * h - r * r)
        print('{:.2f}'.format((arc + sides) * (1 + s / 100)))


if __name__ == '__main__':
    main()

