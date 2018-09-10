#!/usr/bin/env python3

def sum_digits(n):
    total = 0
    while n:
        total += n % 10
        n //= 10
    return total


n = int(input())
while n:
    sum_n = sum_digits(n)
    k = 11
    while sum_digits(n*k) != sum_n:
        k += 1
    print(k)
    n = int(input())
