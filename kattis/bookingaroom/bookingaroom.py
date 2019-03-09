#!/usr/bin/env python3.7


def main():
    r, n = map(int, input().split())
    unused = set(range(1, r + 1))
    for i in range(n):
        unused.remove(int(input()))
    if unused:
        print(unused.pop())
    else:
        print("too late")


if __name__ == "__main__":
    main()
