from sys import stdin


def find_safe(graph, colours, safe, vertex):
    for neighbour in graph[vertex]:
        if colours[neighbour] != -1:
            safe[colours[neighbour]] = False


def try_colour(graph, max_colours, colours, vertex):
    if vertex >= len(graph):
        return True
    safe = [True] * max_colours
    find_safe(graph, colours, safe, vertex)
    for colour in xrange(max_colours):
        if safe[colour]:
            colours[vertex] = colour
            if try_colour(graph, max_colours, colours, vertex + 1):
                return True
    colours[vertex] = -1
    return False

def main():
    lines = stdin.readlines()
    n = int(lines[0])
    g = [[int(x) for x in lines[i + 1].split()]
         for i in xrange(n)]

    colours = [-1] * n
    c = 2
    while True:
        if try_colour(g, c, colours, 0):
            print(c)
            break
        c += 1

if __name__ == "__main__":
    main()

