from math import pi

r, m, c = map(float, input().split())
while r or m or c:
    print(pi * r*r, (2*r * 2*r) * c/m)
    r, m, c = map(float, input().split())
