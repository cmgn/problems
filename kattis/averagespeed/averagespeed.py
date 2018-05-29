#!/usr/bin/env python3

from sys import stdin


def convert_to_seconds(s):
    h, m, s = map(int, s.split(":"))
    return h * 60 * 60 + m * 60 + s


current_speed = 0
last_time = 0
distance_covered = 0

for line in stdin:
    line = line.split()
    current_time = convert_to_seconds(line[0])
    distance_covered += (current_time - last_time) * current_speed
    if len(line) == 2:
        current_speed = int(line[1]) / (60 * 60)
    else:
        print("{:s} {:.2f} km".format(line[0], distance_covered))
    last_time = current_time
