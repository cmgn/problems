#!/usr/bin/env python3


n, m = int(input()), int(input())

a = (360 - n) + m
while a > 180:
    a -= 360
print(a)
