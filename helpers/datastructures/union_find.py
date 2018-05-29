#!/usr/bin/env python3


class UnionFind(object):
    def __init__(self):
        self.unions = {}
        self.sizes = {}

    def add_node(self, a):
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
