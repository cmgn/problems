"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

only have to check 11, 13, 14, 16, 17, 18, 19, 20
"""
#!/usr/bin/env python3


divisors = (11, 13, 14, 16, 17, 18, 19, 20)


def divisible_by_all(n):
    for divisor in divisors:
        if n % divisor != 0:
            return False
    return True


def main():
    n = 20
    while not divisible_by_all(n):
        n += 20
    print(n)


if __name__ == '__main__':
    main()
