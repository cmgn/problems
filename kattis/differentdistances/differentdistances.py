#!/usr/bin/env python3.7


def main():
    s = input()
    while s != "0":
        x1, y1, x2, y2, p = map(float, s.split())
        a = abs(x1 - x2) ** p
        b = abs(y1 - y2) ** p
        print("{:.10f}".format((a + b) ** (1/p)))
        s = input()


if __name__ == "__main__":
    main()
