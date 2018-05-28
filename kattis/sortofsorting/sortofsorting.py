#!/usr/bin/env python3


def main():
    n = int(input())
    while n:
        names = [input() for _ in range(n)]
        for name in sorted(names, key=lambda s: s[:2]):
          print(name)
        print()
        n = int(input())


if __name__ == '__main__':
    main()
