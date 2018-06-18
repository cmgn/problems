#!/usr/bin/env python3


from collections import deque


def main():
    c = 0
    n = int(input())
    while n:
        names = [input() for _ in range(n)]
        queue = deque()
        for k, name in enumerate(reversed(names)):
            if n & 1:
                [queue.appendleft, queue.append][k & 1](name)
            else:
                [queue.append, queue.appendleft][k & 1](name)
        print("SET " + str(c + 1))
        print("\n".join(queue))
        c += 1
        n = int(input())


if __name__ == '__main__':
    main()
