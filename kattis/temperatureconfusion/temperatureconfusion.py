from math import gcd

a, b = map(int, input().split("/"))
a = (a - 32*b) * 5
b *= 9
c = gcd(a, b)
print(f"{a//c}/{b//c}")
