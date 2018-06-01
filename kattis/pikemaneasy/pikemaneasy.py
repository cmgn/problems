#!/usr/bin/env python3


from sys import stdin


def main():
    N, T, A, B, C, t0 = [int(x) for x in stdin.read().split()]
    times = [t0]
    for _ in range(N-1):
        times.append((A * times[-1] + B) % C + 1)
    times.sort(reverse=True)
    current_time = 0
    penalty = 0
    solved = 0
    while times and current_time + times[-1] <= T:
        current_time += times.pop()
        penalty += current_time
        solved += 1
    print(solved, penalty % 1000000007)


if __name__ == '__main__':
    main()