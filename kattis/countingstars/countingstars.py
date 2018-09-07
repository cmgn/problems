from sys import stdin

def fill(grid, i, j):
    to_visit = [(i, j)]
    while to_visit:
        i, j = to_visit.pop()
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            continue
        elif grid[i][j] == "#":
            continue
        grid[i][j] = "#"
        to_visit.extend([
            (i, j+1), (i, j-1),
            (i+1, j), (i-1, j),
        ])

def solve(grid):
    groups = 0
    h, w = len(grid), len(grid[0])
    for i in range(h):
        for j in range(w):
            if grid[i][j] == "-":
                groups += 1
                fill(grid, i, j)
    return groups


try:
    case = 1
    while True:
        height, width = map(int, input().split())
        grid = [list(input()) for _ in range(height)]
        groups = solve(grid)
        print("Case {:d}: {:d}".format(case, groups))
        case += 1
except EOFError:
    pass
