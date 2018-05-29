#!/usr/bin/env python3


class UnionFind(object):
    def __init__(self):
        self.unions = {}
        self.sizes = {}
        self.num_forests = 0

    def add_node(self, a):
        self.num_forests += 1
        self.unions[a] = a
        self.sizes[a] = 1
    
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
        self.edges.append((src, dst, cost))
        self.edges.append((dst, src, cost))

    def compute_mst(self):
        uf = UnionFind()
        for i in range(self.num_vert):
            uf.add_node(i)
        self.edges.sort(key=lambda e: e[2])
        total_cost = 0
        i = 0
        while i < len(self.edges) and uf.num_forests != 1:
            src, dst, cost = self.edges[i]
            if uf.find(src) != uf.find(dst):
                total_cost += cost
                uf.union(src, dst)
            i += 1
        return -1 if i >= len(self.edges) else total_cost

m = MST(4)
m.add_edge(0, 1, 2)
m.add_edge(1, 3, 7)
m.add_edge(2, 3, 8)
m.add_edge(0, 2, 5)
m.add_edge(0, 3, 3)
m.add_edge(1, 2, 1)
print(m.compute_mst())