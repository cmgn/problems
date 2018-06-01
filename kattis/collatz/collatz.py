#!/usr/bin/env python3


def main():
    a, b = map(int, input().split())
    while a and b:
        x, y = a, b
        seen = {}

        seen[a] = 0
        counter = 0
        while a != 1 and a != b:
            a = 3*a + 1 if a & 1 else a//2
            counter += 1
            seen[a] = counter

        counter = 0
        while b != 1 and b not in seen:
            b = 3*b + 1 if b & 1 else b//2
            counter += 1

        print(f"{x} needs {seen[b]} steps, {y} needs"
              f" {counter} steps, they meet at {b}")

        a, b = map(int, input().split())


if __name__ == '__main__':
    main()
