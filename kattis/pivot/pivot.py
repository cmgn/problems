#!/usr/bin/env python3


def main():
    input()
    xs = [int(x) for x in input().split()]
    n = len(xs)

    highest_left = [xs[0]] * n
    for i in range(n):
        if highest_left[i-1] < xs[i]:
            highest_left[i] = xs[i]
        else:
            highest_left[i] = highest_left[i-1]
    
    lowest_right = [xs[-1]] * n
    for i in range(n - 2, -1, -1):
        if lowest_right[i+1] > xs[i]:
            lowest_right[i] = xs[i]
        else:
            lowest_right[i] = lowest_right[i+1]
    
    cnt = 0
    for i in range(n):
        if lowest_right[i] == highest_left[i]:
            cnt += 1

    print(cnt)


main()
