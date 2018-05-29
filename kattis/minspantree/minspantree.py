#!/usr/bin/env python3


import heapq


class UnionFind(object):
    def __init__(self, n):
        self.unions = {}
        self.sizes = {}
        self.num_forests = n
        for i in range(n):
            self.unions[i] = i
            self.sizes[i] = 1
    
    def find(self, a):
        a_parent = self.unions[a]
        if a != a_parent:
            self.unions[a] = self.find(a_parent)
        return self.unions[a]

    def union(self, a, b):
        a_parent = self.find(a)
        b_parent = self.find(b)
        if a_parent == b_parent:
            return
        if self.sizes[a_parent] > self.sizes[b_parent]:
            a_parent, b_parent = b_parent, a_parent
        self.sizes[a_parent] += self.sizes[b_parent]
        self.unions[b_parent] = a_parent
        self.num_forests -= 1



class MST(object):
    def __init__(self, n):
        self.num_vert = n
        self.edges = []

    def add_edge(self, src, dst, cost):
        heapq.heappush(self.edges, (cost, (src, dst)))
        heapq.heappush(self.edges, (cost, (dst, src)))

    def compute_mst(self):
        uf = UnionFind(self.num_vert)
        edges = []
        total_cost = 0
        while self.edges and uf.num_forests != 1:
            cost, (src, dst) = heapq.heappop(self.edges)
            if uf.find(src) != uf.find(dst):
                total_cost += cost
                edges.append((src, dst))
                uf.union(src, dst)
        return -1 if not self.edges else (total_cost, edges)



def main():
    s = input()
    while s != "0 0":
        n, m = map(int, s.split())
        mst = MST(n)
        for _ in range(m):
            mst.add_edge(*[int(x) for x in input().split()])
        t = mst.compute_mst()
        if t == -1:
            print("Impossible")
        else:
            print(t[0])
            for (a, b) in sorted(t[1]):
                print(a, b)
        s = input()


if __name__ == '__main__':
    main()