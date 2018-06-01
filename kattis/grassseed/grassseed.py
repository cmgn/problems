#!/usr/bin/env python3

def main():
    cost = float(input())
    total = 0
    for _ in range(int(input())):
        w, h = map(float, input().split())
        total += w * h
    print(total * cost)


if __name__ == '__main__':
    main()
