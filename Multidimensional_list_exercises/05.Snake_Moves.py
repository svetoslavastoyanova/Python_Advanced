from collections import deque
rows, cols = [int(x) for x in input().split()]
matrix = []
string = deque(input())
for row in range(rows):
    matrix.append([])
    for col in range(cols):
        matrix[row].append("")

for row in range(rows):
    for col in range(cols):
        first_char = string.popleft()
        if row % 2 != 0:
            col = cols-1-col
        matrix[row][col] = first_char
        string.append(first_char)

for row in matrix:
    print(''.join(row))