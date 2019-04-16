from sys import stdin

lines = stdin.readlines()
points = [tuple(float(x) for x in lines[i].split())
          for i in range(1, len(lines))]

area = 0
for i in range(1, len(points)):
    x2, y2 = points[i]
    x1, y1 = points[i - 1]
    area += min(y1, y2) * (x2 - x1) + 0.5 * (x2 - x1) * abs(y2 - y1)
print(area / 1000)
