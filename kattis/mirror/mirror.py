#!/usr/bin/env python3


def main():
    t = int(input())
    for test in range(t):
        n, m = map(int, input().split())
        output = []
        for _ in range(n):
            output.append(input()[::-1])
        print("Test " + str(test + 1))
        for item in reversed(output):
            print(item)


if __name__ == '__main__':
    main()