INF = float("inf")


def main():
    n, m, q, s = map(int, raw_input().split()) 
    while n or m or q or s:
        g = []
        for _ in range(m):
            u, v, c = map(int, raw_input().split())
            g.append((u, v, c))
        d = [INF] * n
        d[s] = 0

        for _ in range(n):
            for u, v, c in g:
                if d[u] == INF:
                    continue
                if d[u] + c < d[v]:
                    d[v] = d[u] + c

        while True:
            w = 0
            for u, v, c in g:
                if d[v] == INF or d[u] == INF:
                    continue
                if d[u] + c < d[v]:
                    d[v] = -INF 
                    w += 1
            if not w:
                break

        for _ in range(q):
            u = input()
            c = d[u]
            if c == float("inf"):
                print "Impossible"
            elif c == float("-inf"):
                print "-Infinity"
            else:
                print c

        print
        n, m, q, s = map(int, raw_input().split()) 


if __name__ == "__main__":
    main()

