import heapq
import collections


def main():
    n, m, q, s = map(int, input().split())
    while n or m or q or s:
        graph = collections.defaultdict(list)
        best = [float("inf")] * n
        for _ in range(m):
            u, v, t, p, w = map(int, input().split())
            graph[u].append((v, t, p, w))
        h = [(0, s)]
        while h:
            c, u = heapq.heappop(h)
            if best[u] <= c:
                continue
            best[u] = c
            for v, t, p, w in graph[u]:
                nc = c
                if c <= t:
                    nc = t
                elif not p:
                    continue
                elif (c - t) % p != 0:
                    nc = c + p - ((c - t) % p)
                if best[v] <= nc:
                    continue
                heapq.heappush(h, (nc + w, v))
        for _ in range(q):
            q = int(input())
            if best[q] == float("inf"):
                print("Impossible")
            else:
                print(best[q])
        print()
        n, m, q, s = map(int, input().split())


if __name__ == "__main__":
    main()
