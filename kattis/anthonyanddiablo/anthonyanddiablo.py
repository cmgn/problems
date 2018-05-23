#!/usr/bin/env python
# https://open.kattis.com/problems/anthonyanddiablo

from math import pi

a, n = map(float, input().split())

radius = n / (2*pi)
area = pi * radius ** 2

if area >= a:
    print("Diablo is happy!")
else:
    print("Need more materials!")
