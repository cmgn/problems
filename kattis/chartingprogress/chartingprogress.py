#!/usr/bin/env python3


from sys import stdin


def main():
    lines = [line.strip() for line in stdin]
    i = 0
    while i < len(lines):
        heights = {}
        total = 0
        while i < len(lines) and lines[i]:
            line_count = lines[i].count("*")
            total += line_count
            heights[i] = line_count
            i += 1
        passed = 0
        for amount in heights.values():
            total -= amount
            print(total * "." + "*" * amount + passed * ".")
            passed += amount
        print()
        i += 1


if __name__ == '__main__':
    main()
