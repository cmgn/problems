#!/usr/bin/env python3

from fractions import Fraction

def is_prime(n):
    if n < 2:
        return False
    elif n < 4:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    elif n < 25:
        return True
    i = 5
    while i*i < n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def get_list_of_numbers(s):
    bases = [2, 8, 10, 16]
    results = []
    for base in bases:
        try:
            results.append(int(s, base))
        except ValueError:
            pass
    return results


def main():
    t = int(input())
    while t:
        l = get_list_of_numbers(input())
        n, m = len(l), sum(is_prime(x) for x in l)
        f = str(Fraction(m, n))
        if "/" not in f:
            print(f + "/1")
        else:
            print(f)
        t -= 1


if __name__ == '__main__':
    main()