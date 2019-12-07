#!/usr/bin/env python3

def main():
    n = 1
    while True:
        s = input()
        if s == 'END':
            break
        gaps = s.split('*')
        size = len(gaps[1])
        if any(len(g) != size for g in gaps[1:-1]):
            print(n, 'NOT EVEN')
        else:
            print(n, 'EVEN')
        n += 1


if __name__ == '__main__':
    main()

