from sys import stdin


def colour(c, r):
    return (r + c) % 2


def is_diagonal(c0, r0, c1, r1):
    return c0 + r0 == c1 + r1 or c0 + r1 == c1 + r0


def valid(c0, r0):
    return 0 <= c0 <= 7 and 0 <= r0 <= 7


def pprint(c0, r0):
    return f"{chr(c0+ord('A'))} {r0 + 1}"


def diagonals(c0, r0):
    for i in range(0, 8):
        for j in range(0, 8):
            if is_diagonal(c0, r0, i, j):
                yield (i, j)


lines = stdin.readlines()[1:]
for line in map(str.strip, lines):
    c0, r0, c1, r1 = line.split()

    c0 = ord(c0) - ord("A")
    c1 = ord(c1) - ord("A")
    r0 = int(r0) - 1
    r1 = int(r1) - 1

    if colour(c0, r0) != colour(c1, r1):
        print("Impossible")
    elif c0 == c1 and r0 == r1:
        print("0 " + pprint(c0, r0))
    elif is_diagonal(c0, r0, c1, r1):
        print("1 " + pprint(c0, r0) + " " + pprint(c1, r1))
    else:
        for c2, r2 in diagonals(c0, r0):
            if is_diagonal(c2, r2, c1, r1):
                print("3 " + " ".join((pprint(c0, r0), pprint(c2, r2), pprint(c1, r1))))
                break
