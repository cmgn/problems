#!/usr/bin/env python3


def triangle_exists(adj_matrix, i):
    for j in range(len(adj_matrix)):
        for k in range(j, len(adj_matrix)):
            if adj_matrix[i][j] and adj_matrix[i][k] and adj_matrix[j][k]:
                return True
    return False


num_vert = int(input())
while num_vert != -1:
    adj_matrix = []
    for i in range(num_vert):
        adj_matrix.append([int(x) for x in input().split()])
    weak_vertices = []
    for i in range(num_vert):
        if not triangle_exists(adj_matrix, i):
            weak_vertices.append(i)
    print(" ".join(map(str, weak_vertices)))
    num_vert = int(input())