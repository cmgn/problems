#!/usr/bin/env python3

def sum_digits(s):
    return sum(int(c) for c in str(s))


def main():
    l = int(input())
    d = int(input())
    x = int(input())

    i = l
    while i <= d and sum_digits(i) != x:
        i += 1
    print(i)

    i = d
    while i >= l and sum_digits(i) != x:
        i -= 1
    print(i) 

if __name__ == '__main__':
    main()
