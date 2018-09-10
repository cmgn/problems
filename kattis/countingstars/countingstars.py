from sys import stdin


groups = 0
case = 1

def floodfill(grid, i, j):
    global groups
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


try:
    while True:
        height, width = map(int, input().split())
        grid = [list(input()) for _ in range(height)]
        for i in range(height):
            for j in range(width):
                if grid[i][j] == "-":
                    groups += 1
                    floodfill(grid, i, j)
        print("Case {:d}: {:d}".format(case, groups))
        groups = 0
        case += 1
except EOFError:
    pass
