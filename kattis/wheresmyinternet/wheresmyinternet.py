#!/usr/bin/env python3


class UnionFind(object):
    def __init__(self):
        self.unions = {}

    def add_node(self, a):
        self.unions[a] = a
    
    def find(self, a):
        while a != self.unions[a]:
            self.unions[a] = self.unions[self.unions[a]]
            a = self.unions[a]
        return a

    def union(self, a, b):
        a_parent = self.find(a)
        b_parent = self.find(b)
        if a_parent == "1":
            self.unions[b_parent] = a_parent
        else:
            self.unions[a_parent] = b_parent


network = UnionFind()
m, n = map(int, input().split())

for i in range(n):
    a, b = input().split()
    if a not in network.unions:
        network.add_node(a)
    if b not in network.unions:
        network.add_node(b)
    network.union(a, b)

connected = 1
for i in range(2, m + 1):
    i = str(i)
    if i not in network.unions or network.find(i) != "1":
        print(i)
        connected = 0

if connected:
    print("Connected")
