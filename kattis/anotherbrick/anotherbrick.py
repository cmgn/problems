#!/usr/bin/env python3

height, width, num_bricks = map(int, input().split())
bricks = [int(x) for x in input().split()]

c_h = 0 #  current height
c_w = 0 #    ...   width
i = 0
while i < len(bricks) and (bricks[i] + c_w) <= width and c_h != height:
    if c_w + bricks[i] == width:
        c_w = 0
        c_h += 1
    else:
        c_w += bricks[i]
    i += 1

print(c_h == height and "YES" or "NO")