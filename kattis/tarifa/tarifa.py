#!/usr/bin/env python3


def main():
    monthly_allowance = int(input())
    number_of_months = int(input())
    total_allowance = 0
    for _ in range(number_of_months):
        total_allowance += monthly_allowance - int(input())
    print(total_allowance + monthly_allowance)


if __name__ == '__main__':
    main()
