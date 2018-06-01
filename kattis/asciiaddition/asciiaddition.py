#!/usr/bin/env python3


from sys import stdin


SYMBOLS = """
xxxxxx...xx...xx...xx...xx...xxxxxx
....x....x....x....x....x....x....x
xxxxx....x....xxxxxxx....x....xxxxx
xxxxx....x....xxxxxx....x....xxxxxx
x...xx...xx...xxxxxx....x....x....x
xxxxxx....x....xxxxx....x....xxxxxx
xxxxxx....x....xxxxxx...xx...xxxxxx
xxxxx....x....x....x....x....x....x
xxxxxx...xx...xxxxxxx...xx...xxxxxx
xxxxxx...xx...xxxxxx....x....xxxxxx
.......x....x..xxxxx..x....x.......
"""


def main():
    content = stdin.read()
    lookup = SYMBOLS.split()
    rows = content.split()
    i = 0
    symbols = []
    for i in range(0, len(rows[0]), 6):
        symbols.append("".join(rows[row][i:i+5] for row in range(len(rows))))
    result = [lookup.index(symbol) for symbol in symbols]
    result = eval("".join([str(x) if x < 10 else "+" for x in result]))
    output = [[] for _ in range(7)]
    for char in str(result):
        symbol = lookup[int(char)]
        for i in range(0, len(symbol), 5):
            output[i//5].extend(symbol[i:i+5] + ".")
    print("\n".join("".join(row[:-1]) for row in output))


if __name__ == '__main__':
    main()