#!/usr/bin/env python3


from collections import deque


class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = set()
        self.color = None
    
    def add_edge(self, target, cost):
        self.edges.add((target, cost))

    def color_exists(self, color):
        for vertex in self.edges:
            if vertex[0].color == color:
                return True
        return False


def color_graph(src):
    queue = deque([src])
    max_color = 0
    seen = {src}
    while queue:
        current_node = queue.popleft()
        if not current_node.color:
            i = 1
            while current_node.color_exists(i):
                i += 1
            current_node.color = i
            if i > max_color:
                max_color = i
        for (neighbour, _) in current_node.edges:
            if neighbour in seen:
                continue
            seen.add(neighbour)
            queue.append(neighbour)
    return max_color


def main():
    number_of_vertices = int(input())
    vertices = []
    for vert in range(number_of_vertices):
        vertices.append(Node(vert))
    for connected_to in range(number_of_vertices):
        edges = map(int, input().split())
        for edge in edges:
            vertices[connected_to].add_edge(vertices[edge], 1)
            vertices[edge].add_edge(vertices[connected_to], 1)
    print(color_graph(vertices[0]))


if __name__ == '__main__':
    main()
