#!/usr/bin/env python3


def main():
    _, capacity, k = map(int, input().split())
    socks = [int(x) for x in input().split()]
    socks.sort()
    needed = 1
    amount = 1
    start = socks[0]
    for sock in socks[1:]:
        if sock - start > k or amount == capacity:
            needed += 1
            amount = 0
            start = sock
        amount += 1
    print(needed)


if __name__ == '__main__':
    main()
