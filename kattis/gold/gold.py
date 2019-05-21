from collections import deque

GOLD = "G"
TRAP = "T"
WALL = "#"
PLYR = "P"

width, height = map(int, input().split())
grid = []
for i in range(height):
    grid.append(list(input()))
    if PLYR in grid[-1]:
        start = (i, grid[-1].index(PLYR))

score = 0
queue = deque([start])
while queue:
    i, j = queue.popleft()
    if grid[i][j] == WALL:
        continue
    if grid[i][j] == GOLD:
        score += 1
    if (
        grid[i - 1][j] != TRAP
        and grid[i + 1][j] != TRAP
        and grid[i][j - 1] != TRAP
        and grid[i][j + 1] != TRAP
    ):
        queue.extend([(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)])
    grid[i][j] = WALL

print(score)
