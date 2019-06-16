LEFT = 0
UP = 1
RIGHT = 2
DOWN = 3


def right():
    for i in range(4):
        row = board[i]
        maximum_pos = 3
        for j in range(2, -1, -1):
            while j < maximum_pos:
                if row[j] != 0 and row[j + 1] == row[j]:
                    row[j + 1] *= 2
                    row[j] = 0
                    maximum_pos = j
                elif row[j + 1] == 0:
                    row[j + 1] = row[j]
                    row[j] = 0
                j += 1


def reverse():
    for i, row in enumerate(board):
        board[i] = row[::-1]


def transpose():
    global board
    board = list(map(list, zip(*board)))


def left():
    reverse()
    right()
    reverse()


def up():
    transpose()
    left()
    transpose()


def down():
    transpose()
    right()
    transpose()


directions = [left, up, right, down]
board = []
for i in range(4):
    board.append([int(x) for x in input().split()])
direction = int(input())
directions[direction]()
for x in board:
    for y in x:
        print(y, end=" ")
    print()
