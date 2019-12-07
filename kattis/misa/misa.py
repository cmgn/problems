def neighbours(church, x0, y0):
    for i in range(-1, +2):
        for j in range(-1, +2):
            x1 = x0 + i
            y1 = y0 + j
            if x1 < 0 or x1 >= len(church):
                continue
            if y1 < 0 or y1 >= len(church[0]):
                continue
            if x1 == x0 and y1 == y0:
                continue
            yield x1, y1


def count_neighbours(church, x0, y0):
    return sum(church[x1][y1] == "o" for x1, y1 in neighbours(church, x0, y0))


def main():
    n, m = map(int, input().split())
    board = [input() for _ in range(n)]
    total = 0

    best_count = 0

    for i in range(n):
        for j in range(m):
            if board[i][j] == "o":
                total += count_neighbours(board, i, j)
            else:
                best_count = max(best_count, count_neighbours(board, i, j))

    print(best_count + total // 2)


if __name__ == "__main__":
    main()
