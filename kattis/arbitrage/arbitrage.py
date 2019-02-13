from sys import stdin



lines = stdin.readlines()
g = 0
n = int(lines[0])
while n > 0:
    g += 1
    currencies = lines[g].split()
    g += 1
    currency_map = {v: j for j, v in enumerate(currencies)}
    graph = [[0] * len(currencies) for currency in currencies]
    for _ in xrange(int(lines[g])):
        g += 1
        a, b, c = lines[g].split()
        p = c.index(":")
        c, d = int(c[:p]), int(c[p+1:])
        graph[currency_map[a]][currency_map[b]] = float(d)/c
    g += 1
    N = len(graph)
    for k in xrange(N):
        for i in xrange(N):
            for j in xrange(N):
                if graph[i][j] < graph[i][k] * graph[k][j]:
                    graph[i][j] = graph[i][k] * graph[k][j]
    for i in xrange(N):
        if graph[i][i] > 1:
            print("Arbitrage")
            break
    else:
        print("Ok")
    n = int(lines[g])

