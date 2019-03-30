import sys


def expand(s, left, right):
    substrings = set()
    while left >= 0 and right < len(s) and s[left] == s[right]:
        substrings.add(s[left:right + 1])
        left -= 1
        right += 1
    return substrings


def palindromic_substrings(s):
    substrings = set()
    for i in range(len(s)):
        substrings |= expand(s, i, i)
        substrings |= expand(s, i, i + 1)
    return [s for s in substrings if len(s) > 1]


def main():
    for line in sys.stdin:
        substrings = palindromic_substrings(line[:-1])
        substrings.sort()
        print("\n".join(substrings))
        print()


if __name__ == "__main__":
    main()
