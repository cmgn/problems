#!/usr/bin/env python3


from collections import deque


class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []
    
    def add_edge(self, target, cost):
        self.edges.append((target, cost))


def breadth_first_search(src, to_find):
    queue = deque(src)
    seen = {src}
    while queue:
        current_node = queue.popleft()
        if current_node.value == to_find:
            return current_node
        for (neighbour, _) in current_node.edges:
            if neighbour in seen:
                continue
            seen.add(neighbour)
            queue.append(neighbour)
    return None
