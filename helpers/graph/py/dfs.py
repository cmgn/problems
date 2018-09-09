#!/usr/bin/env python3


class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []
    
    def add_edge(self, target, cost):
        self.edges.append((target, cost))


def depth_first_search(src, to_find):
    stack = [src]
    seen = {src}
    while stack:
        current_node = stack.pop()
        if current_node.value == to_find:
            return current_node
        for (neighbour, _) in current_node.edges:
            if neighbour in seen:
                continue
            seen.add(neighbour)
            stack.append(neighbour)
    return None
