#!usr/bin/env python3

from string import ascii_lowercase

ascii_set = set(ascii_lowercase)
for _ in range(int(input())):
    line = input().lower()
    missing = ascii_set - set(filter(str.isalpha, line))
    if missing:
        print("missing {}".format("".join(sorted(missing))))
    else:
        print("pangram")
