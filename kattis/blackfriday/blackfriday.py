#!/usr/bin/env python3


from collections import Counter


def main():
    n = int(input())
    participants = [int(x) for x in input().split()]
    numbers = Counter(participants)
    numbers = [n for n in numbers if numbers[n] == 1]
    if numbers:
        print(participants.index(max(numbers)) + 1)
    else:
        print("none")
    



if __name__ == '__main__':
    main()
