#!/usr/bin/env python3


lookup = {
    "a": "2", "b": "22", "c": "222",
    "d": "3", "e": "33", "f": "333",
    "g": "4", "h": "44", "i": "444",
    "j": "5", "k": "55", "l": "555",
    "m": "6", "n": "66", "o": "666",
    "p": "7", "q": "77", "r": "777",
    "s": "7777", "t": "8", "u": "88",
    "v": "888", "w": "9", "x": "99",
    "y": "999", "z": "9999"," ": "0", 
}


def main():
    n = int(input())
    for i in range(n):
        s = input()
        b = [lookup[s[0]]]
        for c in s[1:]:
            d = lookup[c]
            if d[0] == b[-1][0]:
                b.append(" ")
            b.append(d)
        print("Case #{}: {}".format(i + 1, "".join(b)))


if __name__ == '__main__':
    main()
