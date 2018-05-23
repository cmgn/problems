#!/usr/bin/env python3

s = input()
while s != "0 0":
    a, b = map(int, s.split())
    print (a // b, a % b, "/", b)
    s = input()
