def flood(planet, x, y):
    stack = [(x, y)]
    while stack:
        (x, y) = stack.pop()
        if x < 0 or x >= len(planet):
            continue
        if y < 0 or y >= len(planet[0]):
            continue
        if planet[x][y] in 'XW':
            continue
        planet[x][y] = 'X'
        stack.extend([
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1),
        ])


def main():
    calls = 0
    n, m = map(int, input().split())
    planet = [list(input()) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if planet[i][j] == 'L':
                flood(planet, i, j)
                calls += 1
    print(calls)


if __name__ == "__main__":
    main()
