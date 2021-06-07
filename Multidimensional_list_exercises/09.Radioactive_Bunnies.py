from collections import deque
def first_position(matrix, searched):
    for i, row in enumerate(matrix):
        for j, col in enumerate(matrix):
            if col == searched:
                return i, j


rows, cols = [int(x) for x in input().split()]
matrix = [list(input()) for _ in range(rows)]
first_position = first_position(matrix, "P")
lairs = deque(input())
while True:
    lair = lairs.popleft()
    if lair == "U":
        if first_position + 1 in range(rows):
            first_position = matrix[first_position + 1]

    elif lair == "D":
        pass
    elif lair == "R":
        pass
    elif lair == "L":
        pass
    lairs.append(lair)

