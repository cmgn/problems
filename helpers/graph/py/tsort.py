#!/usr/bin/env python3


class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []
    
    def add_edge(self, dst):
        self.edges.append(dst)


def topological_sort(u):
    seen = set()
    stack = []
    def dfs(u):
        seen.add(u)
        for v in u.edges:
            if v not in seen:
                dfs(v)
        stack.append(u)
    dfs(u)
    for v in u.edges:
        if v not in seen:
            dfs(v)
    stack.reverse()
    return stack


a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
a.add_edge(b)
a.add_edge(c)
b.add_edge(d)
c.add_edge(d)
c.add_edge(e)
print(*map(lambda x: getattr(x, "value"), topological_sort(a)))
