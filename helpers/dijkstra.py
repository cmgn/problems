#!/usr/bin/env python3


import heapq


class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []
    
    def add_edge(self, target, cost):
        self.edges.append((target, cost))


def dijkstra(src, target):
    distances = {src: 0}
    queue = [(0, src)]
    while queue:
        cost_so_far, node = heapq.heappop(queue)
        if distances[node] < cost_so_far:
            continue
        elif node.value == target:
            return cost_so_far
        for (neighbour, cost) in node.edges:
            if neighbour in distances and \
                distances[neighbour] <= cost_so_far + cost:
                continue
            distances[neighbour] = cost_so_far + cost
            heapq.heappush(queue, (cost_so_far + cost, neighbour))
