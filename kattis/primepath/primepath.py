#!/usr/bin/env python3


import collections
import math


def genprimes(n=10000):
    prime = [True] * (n + 1)
    prime[1] = False
    upto = int(math.sqrt(n)) + 1
    for p in range(2, upto):
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
    return [i for i in range(1000, n + 1) if prime[i]]


def diff(x, y):
    d = 0
    while x and y:
        d += int(x % 10 != y % 10)
        x //= 10
        y //= 10
    return d == 1


def mkgraph(primes):
    graph = collections.defaultdict(set)
    for i in range(len(primes)):
        p = primes[i]
        for j in range(i, len(primes)):
            q = primes[j]
            if diff(p, q):
                graph[p].add(q)
                graph[q].add(p)
    return graph


def findpath(graph, p, q):
    queue = collections.deque([p])
    pred = {p: None}
    while queue:
        u = queue.popleft()
        if u == q:
            break
        for v in graph[u]:
            if v not in pred:
                pred[v] = u
                queue.append(v)
    if q not in pred:
        return []
    result = []
    curr = q
    while curr is not None:
        result.append(curr)
        curr = pred[curr]
    return result[::-1]


def main():
    # Given that 'g' will always be the same, it's possible to inline it.
    # This brings it down to ~~ 0.04s
    g = mkgraph(genprimes())
    n = int(input())
    for i in range(n):
        p, q = map(int, input().split())
        if p == q:
            print(0)
        else:
            path = findpath(g, p, q)
            if not path:
                print("Impossible")
            else:
                print(len(path) - 1)


if __name__ == "__main__":
    main()
